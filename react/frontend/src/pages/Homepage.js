import React, { useState, useEffect } from 'react';
import { Link } from "react-router-dom";

function Home() {
    const [videos, setVideos] = useState([]);

    useEffect(() => {
        const videos1 = [{ video_: "1" }, { video_: "2" }, { video_: "3" }, { video_: "4" }];
        setVideos(videos1);
    }, []); // Empty dependency array ensures the effect runs only once after the initial render

    function PlaceVideo({ video, className = null }) {
        if (!video.video_) {
            return null;
        }

        if (!className) {
            className = "object-cover";
        }

        return (
            <video height={300} controls>
                <source src={`http://localhost:8080/video/${video.video_}.mp4`} type="video/mp4" />
            </video>
        );
    }

    return (
        <div className="mt-4">
            {videos.length > 0 &&
                videos.map((video, index) => (
                    <div key={index}>
                        <div className="flex w-32 h-32 bg-gray-300 grow shrink-0">
                            <PlaceVideo video={video} />
                        </div>
                        <div className="grow-0 shrink">
                            <h2 className="text-xl"> {video.video_}</h2>
                        </div>
                    </div>
                ))}
        </div>
    );
}

export default Home;
