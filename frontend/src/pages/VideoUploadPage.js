import React from 'react';
import { Form, Input, Select, Button ,message} from 'antd';
import axios from 'axios';
import '../styles/VideoUploadStyles.css'; 

const { Option } = Select;

const VideoUploadPage = () => {
  const onFinish = async (values) => {
    try {
      const formData = new FormData();
      formData.append('video', values.video.file);

      const response = await axios.post('/api/v1/upload', formData);

      
      console.log('Server Response:', response.data);
      message.success('Video uploaded successfully!');
    } catch (error) {
      console.error('Error uploading video:', error);
      message.error('Error uploading video. Please try again.');
    } 
  
  };

  return (
    <div className='video-upload-container'>
      <Form onFinish={onFinish} className='video-upload-form'>
        <h1 className='form-title'><em>Video Upload Page</em></h1>

        <Form.Item label='Username' name='username' rules={[{ required: true, message: 'Username is required' }]}>
          <Input placeholder='Enter your username' />
        </Form.Item>

        <Form.Item label='Sports Type' name='sportsType' rules={[{ required: true, message: 'Sports type is required' }]}>
          <Select placeholder='Select sports type'>
            <Option value='football'>Football</Option>
            <Option value='basketball'>Basketball</Option>
            <Option value='tennis'>Tennis</Option>
            <Option value='cricket'>Cricket</Option>
          </Select>
        </Form.Item>

        <Form.Item label='Video Upload' name='video'>
          <Input type='file' />
        </Form.Item>

        <Form.Item>
          <Button type='primary' htmlType='submit' className='upload-button'>
            Upload Video
          </Button>
        </Form.Item>
      </Form>
    </div>
  );
};

export default VideoUploadPage;
