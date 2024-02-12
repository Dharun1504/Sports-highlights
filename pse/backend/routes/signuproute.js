const router=require("express").Router();
const login=require("../models/loginmodel");
const multer=require('multer');
const path=require('path');


const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, './uploads'); 
  },
  filename: (req, file, cb) => {
    cb(null, Date.now() + path.extname(file.originalname));
  },
});

const upload = multer({ storage });
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

router.post('/upload', upload.single('file'), (req, res) => {
  
  res.status(200).json({ message: 'File uploaded successfully!' });
});



module.exports=router;