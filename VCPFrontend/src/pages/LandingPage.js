import * as React from 'react'
import Button from "@mui/material/Button";
import AppBar from '@mui/material/AppBar'
import Toolbar from '@mui/material/Toolbar'
import Tabs from '@mui/material/Tabs'
import {Typography} from "@mui/material";
import Tab from '@mui/material/Tab'
import { useEffect, useState} from "react";
import ProjectView from '../components/projectView'
import User from '../components/user'

function LandingPage () {
    const [isLogged, setisLogged] = useState(false);
    const [tabValue, setTabValue] = React.useState('vcp')

    useEffect(() => {
        console.log(isLogged)
        checkStorage();
        return () => {};
    }, [isLogged]);
    function checkStorage() {
        if (localStorage.getItem("token")) {
            setisLogged(true);
        } else {
            setisLogged(false);
        }
    }
    const logout = () => {
        localStorage.removeItem("token");
        setisLogged(false);
        setTabValue('vcp')
    };
    const handleChange = (event, newValue) => {
        setTabValue(newValue)
    }
    return (
        <div>
            <div>
                <AppBar position='static' style={{ backgroundColor: '#222222' }}>
                    <Toolbar variant='dense'>
                        <Tabs
                            value={tabValue}
                            onChange={handleChange}
                            textColor='white'
                            indicatorColor='secondary'
                            sx={{ flexGrow: 1 }}
                        >
                            <Tab value='vcp' label='VCP' />
                            <Tab
                                value='projects'
                                label='Projects'
                                disabled={!isLogged}
                            />
                        </Tabs>
                        {!isLogged ? (
                            <Button color="inherit">Log in</Button>
                        ) : (
                            <Button onClick={logout} color="inherit">
                                Log out
                            </Button>
                        )}
                    </Toolbar>
                </AppBar>
            </div>
            <div>
                {tabValue === 'vcp' && <User setTabValue={setTabValue} />}
                {tabValue === 'projects' && <ProjectView />}
            </div>
        </div>
    )
}
export default LandingPage
