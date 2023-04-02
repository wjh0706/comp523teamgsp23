import * as React from 'react'
import Box from '@mui/material/Box'
import Input from '@mui/material/Input'
import InputLabel from '@mui/material/InputLabel'
import InputAdornment from '@mui/material/InputAdornment'
import FormControl from '@mui/material/FormControl'
import AccountCircle from '@mui/icons-material/AccountCircle'
import Visibility from '@mui/icons-material/Visibility'
import VisibilityOff from '@mui/icons-material/VisibilityOff'
import Button from '@mui/material/Button'
import Card from '@mui/material/Card'
import CardContent from '@mui/material/CardContent'
import IconButton from '@mui/material/IconButton'
import Grid from '@mui/material/Grid'
import Alert from '@mui/material/Alert'
import TESTHOST from '../backend/backendAPI'

const axios = require('axios').default

function Login({ setView, setTabValue, ...props }) {
  const [values, setValues] = React.useState({
    username: '',
    password: ''
  })
  const [userInfo, setUserInfo] = React.useState(null)
  const [error, setError] = React.useState(false)
  const [showPassword, setShowPassword] = React.useState(false)
  

  React.useEffect(() => {
    if (userInfo !== null) {
      localStorage.setItem('token', userInfo.token)
      console.log(localStorage.getItem('token'))
    }
  }, [userInfo])
  const handleChange = (type, event) => {
    if (type === 'password') {
      setValues({ ...values, password: event.target.value })
    } else if (type === 'username') {
      setValues({ ...values, username: event.target.value })
    }
  }
  const handleClickShowPassword = () => {
    setShowPassword(!showPassword)
  }
  const handleMouseDownPassword = (event) => {
    event.preventDefault()
  }

  const handlelogin = () => {
    axios({
      method: 'post',
      url: TESTHOST + '/login/',
      data: values
    }).then((response) => {
      setError(false)
      console.log(response)
      setUserInfo(response.data)
      setTabValue('projects')
    }).catch(() => {
      setError(true)
    })
  }

  return (
    <div style={{ height: '100vh', display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
      <Card style={{ height: '40%', width: '30%', padding: '1%' }}>
        <CardContent>
          <FormControl sx={{ m: 1, width: '100%' }} variant='standard'>
            <InputLabel htmlFor='input-with-icon-adornment'>
              Username:
            </InputLabel>
            <Input
              value={values.username}
              onChange={(e) => { handleChange('username', e) }}
            />
          </FormControl>
          <FormControl sx={{ m: 1, width: '100%' }} variant='standard'>
            <InputLabel htmlFor='standard-adornment-password'>Password</InputLabel>
            <Input
              id='standard-adornment-password'
              type={showPassword ? 'text' : 'password'}
              value={values.password}
              onChange={(e) => { handleChange('password', e) }}
              endAdornment={
                <InputAdornment position='end'>
                  <IconButton
                    aria-label='toggle password visibility'
                    onClick={handleClickShowPassword}
                    onMouseDown={handleMouseDownPassword}
                  >
                    {showPassword ? <VisibilityOff /> : <Visibility />}
                  </IconButton>
                </InputAdornment>
              }
            />
          </FormControl>
          {error && <Alert severity="error">Username and Password do not match. Please try again.</Alert>}
          <div style={{ width: '100%', display: 'flex', flexDirection: 'row', justifyContent: 'space-evenly', marginTop: '10%' }}>
            <Button variant='outlined' disableElevation onClick={() => { setView('signup') }} style={{ marginTop: 5 }}>
              Sign up
            </Button>
            <Button variant='contained' disableElevation onClick={handlelogin} style={{ marginTop: 5 }}>
              Log in
            </Button>
          </div>
        </CardContent>
      </Card>
    </div>
  )
}

function Signup({ setView, ...props }) {
  const [values, setValues] = React.useState({
    email: '',
    username: '',
    password: ''
  })
  const [showPassword, setShowPassword] = React.useState(false)
  const [error, setError] = React.useState(false)
  const handleChange = (type, event) => {
    if (type === 'password') {
      setValues({ ...values, password: event.target.value })
    } else if (type === 'email') {
      setValues({ ...values, email: event.target.value })
    } else if (type === 'username') {
      setValues({ ...values, username: event.target.value })
    }
  }
  const handleClickShowPassword = () => {
    setShowPassword(!showPassword)
  }
  const handleMouseDownPassword = (event) => {
    event.preventDefault()
  }
  const handleSignup = () => {
    axios({
      method: 'post',
      url: TESTHOST + '/register/',
      data: values
    }).then((response) => {
      setError(false)
      setView('login')
    }).catch(() => {
      setError(true)
    })
  }

  return (
    <div style={{ height: '100vh', display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
      <Card style={{ height: '40%', width: '30%', padding: '1%' }}>
        <CardContent>
          <FormControl sx={{ m: 1, width: '100%' }} variant='standard'>
            <InputLabel htmlFor='standard-adornment-password'>Email</InputLabel>
            <Input
              // type={values.showPassword ? 'text' : 'password'}
              value={values.email}
              onChange={(e) => { handleChange('email', e) }}
            />
          </FormControl>
          <FormControl sx={{ m: 1, width: '100%' }} variant='standard'>
            <InputLabel htmlFor='input-with-icon-adornment'>
              Username:
            </InputLabel>
            <Input
              // type={values.showPassword ? 'text' : 'password'}
              value={values.username}
              onChange={(e) => { handleChange('username', e) }}
            />
          </FormControl>
          <FormControl sx={{ m: 1, width: '100%' }} variant='standard'>
            <InputLabel htmlFor='standard-adornment-password'>Password</InputLabel>
            <Input
              id='standard-adornment-password'
              type={showPassword ? 'text' : 'password'}
              value={values.password}
              onChange={(e) => { handleChange('password', e) }}
              endAdornment={
                <InputAdornment position='end'>
                  <IconButton
                    aria-label='toggle password visibility'
                    onClick={handleClickShowPassword}
                    onMouseDown={handleMouseDownPassword}
                  >
                    {showPassword ? <VisibilityOff /> : <Visibility />}
                  </IconButton>
                </InputAdornment>
              }
            />
          </FormControl>
          {error && <Alert severity="error">Please try again.</Alert>}
          <div style={{ width: '100%', display: 'flex', flexDirection: 'row', justifyContent: 'space-evenly', marginTop: '10%' }}>
            <Button variant='outlined' disableElevation onClick={handleSignup} style={{ marginTop: 5 }}>
              Submit
            </Button>
            <Button variant='contained' disableElevation onClick={() => { setView('login') }} style={{ marginTop: 5 }}>
              Cancel
            </Button>
          </div>
        </CardContent>
      </Card>
    </div>
  )
}

function User({ setTabValue, ...props }) {
  const [view, setView] = React.useState('login')
  return (
    <div>
      {view === 'login' && <Login setView={setView} setTabValue={setTabValue} />}
      {view === 'signup' && <Signup setView={setView} />}
    </div>
  )
}
export default User