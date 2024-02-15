const router=require("express").Router();
const login=require("../models/loginmodel");

const path=require('path');
const multer=require('multer');


router.post("/signup",async(req,res)=>{
    try{
        const data=req.body;
        const newlogin=new login(data);
        await newlogin.save().then(()=>{
            res.status(200).json({message:"signed up successfully"});   
        })
    }
    catch(error){
        console.log(error);
    }
});

router.post("/login", async (req, res) => {
  try {
    const { username, password } = req.body;


    const user = await login.findOne({ 'username':username, 'password':password });

    if (user) {
      res.status(200).json({ message: "Login successful" });
    } else {
    
      res.status(401).json({ message: "Invalid username or password" });
    }
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: "Internal Server Error" });
  }
});

router.post('/upload', (req, res) => {
  if (req.files === null) {
      return res.status(400).json({ msg: 'No file uploaded' });  
  }
  const theFile = req.files.file;


  console.log(theFile); 
  theFile.mv(`${__dirname}/public/uploads/${theFile.name}`, err => {
        if (err) {
            console.log(err);
            return res.status(500).send(err); 
        }
    }); 




    res.json({ 
        fileName: theFile.name,
        filePath: `/uploads/${theFile.name}`
    })


})





module.exports=router;