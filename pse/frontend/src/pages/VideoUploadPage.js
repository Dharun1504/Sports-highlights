import React, { useState } from "react";
import axios from "axios";
import "../styles/VideoUploadStyles.css";

export default function FileUpload() {
    const [file, setFile] = useState("");

    const handleChange = (e) => {
        setFile(e.target.files[0]);
    };

    const onSubmit = async (e) => {
        e.preventDefault();
        const formData = new FormData();
        formData.append("file", file);
        try {
            await axios.post("/api/v1/upload", formData, {
                headers: {
                    "Content-type": "multipart/form-data",
                },
            });
        } catch (err) {
            if (err.response.status === 500) {
                console.log("error 500, server");
            }
            if (err.response.status === 400) {
                console.log(err.response.data.msg);
            }
        }
    };

    return (
        <div className="file-upload-container">
            <form className="file-upload-form" onSubmit={onSubmit}>
                
                <label>Upload Video Here: <input className="file-input" type="file" id="customFile" onChange={handleChange} />{" "}</label>
                <label>Video Duration: <input type="number" min="2" max="10" className="time-limit"     ></input></label>
                <button className="submit-button" type="submit">Submit</button>
            </form>
        </div>
    )
}
