import React from 'react';
import { Link } from 'react-router-dom';

const Sidebar = () => {
  return (
    <div className="sidebar">
      <Link to="/upload">Upload</Link>
      <Link to="/home">Home</Link>
      <Link to="/watch-history">Watch History</Link>
    </div>
  );
};

export default Sidebar;
