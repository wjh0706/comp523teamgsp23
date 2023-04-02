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
import TESTHOST from '../backend/backendAPI'

const axios = require('axios').default


function SceneEdit({setView, scene, setScene, setTake, ...props}) {
    const [numTakes, setNumTakes] = React.useState([])
    const [info, setInfo] = React.useState(scene)
    React.useEffect(() => {
        axios({
            method: 'get',
            url: TESTHOST + '/takes/gettakes/?token=' + localStorage.token + '&sid=' + info.sid
        }).then((res) => {
            console.log(res.data)
            setNumTakes(res.data)
        })
    }, [])
    const handleAddTake = () => {
        axios({
            method: 'post',
            url: TESTHOST + '/takes/createtake/',
            data: {
                sid: info.sid,
                token: localStorage.getItem('token')
            }
        }).then((res) => {
            setNumTakes([...numTakes, res.data])
            console.log(res.data)
        })
    }

    const handleChange = (type, event) => {
        if (type === 'name') {
            setInfo({...info, scene_name: event.target.value})
        } else if (type === 'description') {
            setInfo({...info, description: event.target.value})
        }
    }

    const handleSave = () => {
        axios({
            method: 'patch',
            url: TESTHOST + '/scenes/editscene/',
            data: {
                scene_name: info.scene_name,
                description: info.description,
                token: localStorage.getItem('token'),
                sid: info.sid
            }
        }).then((res) => {
            setScene(info)
            setView('projectEdit')
        })
    }
    const handleCancel = () => {
        setView('projectEdit')
    }
    const handleDelete = () => {
        axios({
            method: 'delete',
            url: TESTHOST + '/scenes/deletescene/',
            data: {
                token: localStorage.getItem('token'),
                sid: info.sid
            }
        }).then((res) => {
            setScene(info)
            console.log(res.data)
            setView('projectEdit')
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
                            <InputLabel htmlFor="filled-adornment-scene-name">Scene Name:</InputLabel>
                            <FilledInput
                                id="filled-adornment-scene-name"
                                startAdornment={<InputAdornment position="start"></InputAdornment>}
                                value={info.scene_name}
                                onChange={(e) => {
                                    handleChange('name', e)
                                }}
                            />
                        </FormControl>
                        <FormControl fullWidth sx={{m: 1}} variant="filled">
                            <InputLabel htmlFor="filled-adornment-scene-description">Scene Description:</InputLabel>
                            <FilledInput
                                id="filled-adornment-Scene-description"
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
                            Takes
                        </Typography></Grid>
                        <Grid item><Button variant='contained' style={{margin: 16}} size="large"
                                           onClick={handleAddTake}>+ New Take</Button></Grid>
                    </Grid>
                    <Grid container spacing={1}
                          style={{display: 'flex', flexDirection: 'row', justifyContent: 'start'}}>
                        {numTakes && numTakes.map((value) => (
                            <TakeCard key={value.tid} setView={setView} value={value} setTake={setTake}/>
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
                            Delete Scene
                        </Button>
                    </Grid>
                </Box>
            </Stack>
        </div>
    )
}

function TakeCard({setView, value, setTake, ...props}) {
    const handleEdit = () => {
        setTake(value)
        setView('takeEdit')
    }
    return (
        <Card style={{height: '30%', width: '20%', margin: 16, padding: 10}}>
            <CardMedia
                component='img'
                height='140'
                image=''
                alt='take image'
            />
            <CardContent>
                <Typography gutterBottom variant='h5' component='div'>
                    {value.take_name ? value.take_name : 'Take'}
                </Typography>
                <Typography variant='body2' color='text.secondary'>
                    {value.description ? value.description : 'You have created a new Take! Add any descriptions through the edit button.'}
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
                </Grid>
            </CardActions>
        </Card>
    )
}

export default SceneEdit