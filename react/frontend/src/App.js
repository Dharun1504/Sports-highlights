import React,{useState} from 'react';
import {BrowserRouter,Routes,Route,Navigate} from 'react-router-dom';
import './App.css';
import Login from './pages/loginpage';
import Upload from './pages/VideoUploadPage';
import Home from './pages/Homepage';
import Signup from './pages/signuppage';
import VideoPage from './pages/VideoPage';
function App() {
  const [ authenticated ,setAuthenticated] =useState(false) ;
  return (
    <>
      <BrowserRouter>
      <Routes>
          <Route path ='/' element={<Login setAuthenticated={setAuthenticated} />}/>
          <Route path='/upload' element={<Upload/> }/>
          <Route path='/home' element={<Home/>}/>
          <Route path='/signup' element={<Signup></Signup>}/>
          <Route
          path="/video/:videoId"  
          element={<VideoPage key="videoId" />}
        />  

      </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
