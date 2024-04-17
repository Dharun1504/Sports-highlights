import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import Sidebar from './Sidebar';
import '../styles/homepage.css';

const Home = () => {
  const [videos, setVideos] = useState([]);

  useEffect(() => {
    const fetchMp4Files = async () => {
      try {
        const response = await fetch('/api/mp4Files');
        if (!response.ok) {
          throw new Error('Failed to fetch MP4 files');
        }
        const data = await response.json();
        setVideos(data);

      } catch (error) {
        console.error(error);
      }
    };

    fetchMp4Files();
  }, []);

  function VideoCard({ video }) {
    if (!video.video_) {
      return null;
    }

    return (
      <div className="video-card">
        <Link to={`/video/${video.video_}`}>
          <video className="video" >
            <source src={`http://localhost:8080/video/${video.video_}`} type="video/mp4" />
          </video>
        </Link>
        <h2 className="video-title">{video.video_}</h2>
      </div>
    );
  }

  return (
    <div>
      <header className="header-container">
        <h1>Sports Highlights App</h1>
      </header>
      <div className="content">
        <Sidebar />
        <div className="video-container">
          {videos.length > 0 &&
            videos.map((video, index) => (
              <VideoCard key={index} video={video} />
            ))}
        </div>
      </div>
    </div>
  );
};

export default Home;
