import React,{useState} from 'react';
import {BrowserRouter,Routes,Route,Navigate} from 'react-router-dom';
import './App.css';
import Login from './pages/loginpage';
import Upload from './pages/VideoUploadPage';
function App() {
  const [ authenticated ,setAuthenticated] =useState(false) ;
  return (
    <>
      <BrowserRouter>
      <Routes>
          <Route path ='/' element={<Login setAuthenticated={setAuthenticated} />}/>
          <Route path='/upload' element={authenticated ? <Upload/> : <Navigate to='/' />}
          />
      </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
