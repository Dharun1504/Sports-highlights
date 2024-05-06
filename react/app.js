const express=require("express");
const app=express();
const fs=require('fs');
var path = require('path');
require("./backend/connection/conn");
const signuproute=require("./backend/routes/signuproute");
const fileUpload = require('express-fileupload');
app.use(fileUpload());

app.use(express.json());
app.use("/api/v1",signuproute);
console.log(path.join(__dirname , "public","Videos"))
app.use("/video", express.static(path.join(__dirname , "public","Videos")))
app.get('/api/mp4Files', (req, res) => {
    const mp4Files = [];
  
    
    const publicDir = path.join(__dirname, 'public\\videos');
    fs.readdir(publicDir, (err, files) => {
      if (err) {
        console.error('Error reading directory:', err);
        res.status(500).json({ error: 'Internal Server Error' });
        return;
      }
  
      
      const mp4Files = files
        .filter(file => file.endsWith('.mp4'))
        .map(file => ({ video_: file })); 

      res.json(mp4Files);
    });
  });
const port = process.env.PORT || 8080
app.listen(port ,()=>{
    console.log("Server started",port);
});
