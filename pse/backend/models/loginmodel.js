const mongoose=require("mongoose");
const login =new mongoose.Schema({
    username:{type:String,required:true},
    password:{type:String,required:true},
    
});

module.exports=new mongoose.model("login",login);

