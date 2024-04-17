import React, { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import '../styles/VideoPage.css'; 

function VideoPage() {
  const { videoId } = useParams();
  const [vidId,setvidId]=useState(videoId);
  const [videos, setVideos] = useState([]);
  const [relatedVideos, setRelatedVideos] = useState([]);

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

  useEffect(() => {
    if (videos.length > 0) {
      const filteredVideos = videos.filter(video => video.video_ !== videoId);
      setRelatedVideos(filteredVideos);
      setvidId(videoId)
    }
  }, [videos, videoId]); // Update related videos when videoId changes

  return (
    <div>
      <div className="header-container">
        <h1>Sports Highlights App</h1>
      </div>
      <div className="video-page-container">
        <div className="video-player">
            <video controls>
                <source src={`http://localhost:8080/video/${vidId}`} type="video/mp4" />
            </video>
            <h1 className="video-title">{videoId}</h1> 
        </div>

        <div className="related-videos">
          <h2>Next Videos</h2>
          {relatedVideos.map((video, index) => (
            <div className="related-video" key={index}>
              <Link to={`/video/${video.video_}`}>
                <video>
                  <source src={`http://localhost:8080/video/${video.video_}`} type="video/mp4" />
                </video>
              </Link>
              <h3 className="related-video-title">{video.video_}</h3>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default VideoPage;
