const express=require("express");
const app=express();
require("./backend/connection/conn");
const signuproute=require("./backend/routes/signuproute");


app.use(express.json());
app.use("/api/v1",signuproute);
const port = process.env.PORT || 8080
app.listen(port ,()=>{
    console.log("Server started",port);
});
