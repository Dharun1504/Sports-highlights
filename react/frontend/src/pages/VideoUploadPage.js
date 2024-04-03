import React, { useEffect, useState } from "react";
import axios from "axios";
import "../styles/VideoUploadStyles.css";
import Aos from "aos";
import 'aos/dist/aos.css';
export default function FileUpload() {

    useEffect(() => {
		Aos.init({duration:2000});
	}, []);

    const [file, setFile] = useState("");
    const [pathOutput,setPathOutput] = useState("");
    const handleChange = (e) => {
        setFile(e.target.files[0]);
    };
    const [userQuery,setUserQuery] = useState("");
    const onSubmit1 = async (e) => {
        e.preventDefault();
        const formData = new FormData();  
        formData.append("file", file);
        try {
            // console.log(formData);
            const path = await axios.post("/api/v1/upload", formData, {
                headers: {
                    "Content-type": "multipart/form-data",
                }, 
            });
            const new_path =await axios.post("http://localhost:5000/data",{path:path.data.filePath,userQuery:userQuery})
            setPathOutput(new_path.data)
            console.log(new_path.data)

        } catch (err) {
            console.log(err)
        }
    };

    return (
        <div className="file-upload-container" >
            <form className="file-upload-form" data-aos = 'fade-up' onSubmit={(e)=>onSubmit1(e)}>
                
                <label>
                    <input onChange={(e)=>setUserQuery(e.target.value)} value={userQuery}/>
                    <input className="file-input" type="file" id="customFile" onChange={handleChange} />{" "}</label>
                {/* <label>Video Duration: <input type="number" min="2" max="10" className="time-limit"     ></input></label> */}
                <button className="submit-button" type="submit">Submit</button>
            </form>
            {/* <video height={300} controls data-aos = 'fade-up'>
                        <source src={"http://localhost:8080/video/"+"1710664150380877.mp4"} type="video/mp4"/>
            </video> */}
            {
                !!pathOutput &&(
                    <video height={300} controls data-aos = 'fade-up'>
                        <source src={"http://localhost:8080/video/"+pathOutput+".mp4"} type="video/mp4"/>
                    </video>
                ) 
            }
            
        </div>
    )
}
