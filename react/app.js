const express=require("express");
const app=express();
var path = require('path');
require("./backend/connection/conn");
const signuproute=require("./backend/routes/signuproute");
const fileUpload = require('express-fileupload');
app.use(fileUpload());

app.use(express.json());
app.use("/api/v1",signuproute);
console.log(path.join(__dirname , "public","Videos"))
app.use("/video", express.static(path.join(__dirname , "public","Videos")))
const port = process.env.PORT || 8080
app.listen(port ,()=>{
    console.log("Server started",port);
});
