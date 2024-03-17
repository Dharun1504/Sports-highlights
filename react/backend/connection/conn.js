const mongoose=require("mongoose");
mongoose.connect("mongodb://0.0.0.0/SportsHighlight").then(()=>console.log("connected"));