import * as React from 'react'
import Box from '@mui/material/Box'
import Grid from '@mui/material/Grid'
import Button from '@mui/material/Button'
import Card from '@mui/material/Card'
import CardActions from '@mui/material/CardActions'
import CardContent from '@mui/material/CardContent'
import CardMedia from '@mui/material/CardMedia'
import Typography from '@mui/material/Typography'
import TESTHOST from '../backend/backendAPI'

const axios = require('axios').default

// const Item = styled(Paper)(({ theme }) => ({
//   ...theme.typography.body2,
//   padding: theme.spacing(1),
//   textAlign: 'center',
//   color: theme.palette.text.secondary
// }))

function ProjectCard({ setView, value, setProject, ...props }) {
  const [projectInfo, setInfo] = React.useState({
    project_name: value.project_name,
    description: value.description,
    pid: value.pid
  })
  const handleEdit = () => {
    console.log(value)
    setProject(value)
    setView('projectEdit')
  }
  return (
      <Card style={{ height: '30%', width: '20%', margin: 16, padding: 10 }}>
        <CardMedia
          component='img'
          height='140'
          image=''
          alt='project image'
        />
        <CardContent>
          <Typography gutterBottom variant='h5' component='div'>
            {projectInfo.project_name ? projectInfo.project_name : 'Project'}
          </Typography>
          <Typography variant='body2' color='text.secondary'>
            {projectInfo.description ? projectInfo.description : 'You have created a new project! Add any descriptions through the edit button.'}
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

function ProjectList({ setView, setProject, ...props }) {
  const [numProjects, setNumProjects] = React.useState([])
  React.useEffect(() => {
    axios({
      method: 'get',
      url: TESTHOST + '/projects/getprojects/?token=' + localStorage.token
    }).then((res) => {
      console.log(res.data)
      setNumProjects(res.data)
    })
  }, [])
  const handleAddProject = () => {
    axios({
      method: 'post',
      url: TESTHOST + '/projects/createproject/',
      data: {
        project_name: "",
		    description: "",
        token: localStorage.getItem('token')
      }
    }).then((res) => {
      setNumProjects([...numProjects, res.data])
      console.log(res.data)
    })
    // setNumProjects([...numProjects, numProjects.length + 1])
  }
  return (
    <div>
      <div>
        <Button variant='contained' style={{ margin: 16 }} onClick={handleAddProject}>+ New Project</Button>
      </div>
      <Box sx={{ flexGrow: 1 }} style={{ margin: 16 }}>
        <Grid container spacing={2} style={{ display: 'flex', flexDirection: 'row', justifyContent: 'start' }}>
          {numProjects && numProjects.map((value) => (
            <ProjectCard key={value.pid} setView={setView} value={value} setProject={setProject}/>
          ))}
        </Grid>
      </Box>
    </div>
  )
}

export default ProjectList
