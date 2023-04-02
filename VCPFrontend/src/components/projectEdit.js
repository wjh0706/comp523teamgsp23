import * as React from 'react'
import Box from '@mui/material/Box'
import InputLabel from '@mui/material/InputLabel'
import InputAdornment from '@mui/material/InputAdornment'
import FormControl from '@mui/material/FormControl'
import Button from '@mui/material/Button'
import Card from '@mui/material/Card'
import CardContent from '@mui/material/CardContent'
import Grid from '@mui/material/Grid'
import Stack from '@mui/material/Stack'
import FilledInput from '@mui/material/FilledInput'
import CardActions from '@mui/material/CardActions'
import CardMedia from '@mui/material/CardMedia'
import Typography from '@mui/material/Typography'
import DeleteIcon from '@mui/icons-material/Delete'
import ProjectList from './projectList'
import ProjectView from './projectView'
import TESTHOST from '../backend/backendAPI'

const axios = require('axios').default

function ProjectEdit({setView, project, setProject, setScene, ...props}) {
    const [numScenes, setNumScenes] = React.useState([])
    const [info, setInfo] = React.useState(project)
    React.useEffect(() => {
        axios({
            method: 'get',
            url: TESTHOST + '/scenes/getscenes/?token=' + localStorage.token + '&pid=' + info.pid
        }).then((res) => {
            console.log(res.data)
            setNumScenes(res.data)
        })
    }, [])
    const handleAddScene = () => {
        axios({
            method: 'post',
            url: TESTHOST + '/scenes/createscene/',
            data: {
                pid: info.pid,
                token: localStorage.getItem('token')
            }
        }).then((res) => {
            setNumScenes([...numScenes, res.data])
            console.log(res.data)
        })
    }

    const handleSave = () => {
        axios({
            method: 'patch',
            url: TESTHOST + '/projects/editproject/',
            data: {
                project_name: info.project_name,
                description: info.description,
                token: localStorage.getItem('token'),
                pid: info.pid
            }
        }).then((res) => {
            setProject(info)
            setView('projectList')
        })
    }

    const handleChange = (type, event) => {
        if (type === 'name') {
            setInfo({...info, project_name: event.target.value})
        } else if (type === 'description') {
            setInfo({...info, description: event.target.value})
        }
    }
    const handleCancel = () => {
        setView('projectList')
    }
    const handleDelete = () => {
        axios({
            method: 'delete',
            url: TESTHOST + '/projects/deleteproject/',
            data: {
                token: localStorage.getItem('token'),
                pid: info.pid
            }
        }).then((res) => {
            setProject(info)
            console.log(res.data)
            setView('projectList')
        })
    }

    return (
        <div>
            <Stack spacing={1}>
                <Box m={1} pt={1}>
                    <Grid
                        container
                        direction="column"
                        justifyContent="flex-start"
                        alignItems="center"
                        margin="auto"
                    >
                        <FormControl fullWidth sx={{m: 1}} variant="filled">
                            <InputLabel htmlFor="filled-adornment-project-name">Project Name:</InputLabel>
                            <FilledInput
                                id="filled-adornment-project-name"
                                startAdornment={<InputAdornment position="start"></InputAdornment>}
                                value={info.project_name}
                                onChange={(e) => {
                                    handleChange('name', e)
                                }}
                            />
                        </FormControl>
                        <FormControl fullWidth sx={{m: 1}} variant="filled">
                            <InputLabel htmlFor="filled-adornment-project-description">Project Description:</InputLabel>
                            <FilledInput
                                id="filled-adornment-project-description"
                                startAdornment={<InputAdornment position="start"></InputAdornment>}
                                multiline
                                rows={4}
                                value={info.description}
                                onChange={(e) => {
                                    handleChange('description', e)
                                }}
                            />
                        </FormControl>
                    </Grid>
                    <Grid
                        container
                        direction="row"
                        justifyContent="flex-start"
                        spacing={1}
                        alignItems="center"
                        margin="auto"
                    >
                        <Grid item><Button variant="contained" size="large" onClick={handleSave}>Save</Button></Grid>
                        <Grid item><Button variant="outlined" size="large" onClick={handleCancel}>Cancel</Button></Grid>
                    </Grid>
                    <Grid
                        container
                        direction="row"
                        justifyContent="space-between"
                        alignItems="center"
                        margin="auto"
                    >
                        <Grid item><Typography gutterBottom variant='h5' component='div' sx={{m: 1}}>
                            Scenes
                        </Typography></Grid>
                        <Grid item><Button variant='contained' style={{margin: 16}} size="large"
                                           onClick={handleAddScene}>+ New Scene</Button></Grid>
                    </Grid>
                    <Grid container spacing={1}
                          style={{display: 'flex', flexDirection: 'row', justifyContent: 'start'}}>
                        {numScenes && numScenes.map((value) => (
                            <SceneCard key={value.sid} setView={setView} value={value} setScene={setScene}/>
                        ))}
                    </Grid>
                    <Grid
                        container
                        direction="row"
                        justifyContent="flex-end"
                        alignItems="center"
                        margin="auto"
                    >
                        <Button variant="outlined" startIcon={<DeleteIcon/>} size="large" onClick={handleDelete}>
                            Delete Project
                        </Button>
                    </Grid>
                </Box>
            </Stack>
        </div>
    )
}

function SceneCard({setView, value, setScene, ...props}) {
    const handleEdit = () => {
        setScene(value)
        setView('sceneEdit')
    }
    return (
        <Card style={{height: '30%', width: '20%', margin: 16, padding: 10}}>
            <CardMedia
                component='img'
                height='140'
                image=''
                alt='scene image'
            />
            <CardContent>
                <Typography gutterBottom variant='h5' component='div'>
                    {value.scene_name ? value.scene_name : 'Scene'}
                </Typography>
                <Typography variant='body2' color='text.secondary'>
                    {value.description ? value.description : 'You have created a new Scene! Add any descriptions through the edit button.'}
                </Typography>
            </CardContent>
            <CardActions>
                <Grid
                    container
                    direction="row"
                    justifyContent="space-around"
                    spacing={1}
                    alignItems="center"
                    margin="auto"
                >
                    <Grid item><Button variant='contained' onClick={handleEdit}>Edit</Button></Grid>
                    <Grid item><Button variant="outlined">Download Model</Button></Grid>
                </Grid>
            </CardActions>
        </Card>
    )
}

export default ProjectEdit