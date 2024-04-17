import React from 'react';
import { Form, Input, Button, message } from 'antd';
import { Link, useNavigate } from 'react-router-dom';
import axios from 'axios';
import '../styles/SignupPage.css'; // Create a separate CSS file for the signup page styles

const SignupPage = () => {
  const navigate = useNavigate();
  
  const onFinishHandler = async (values) => {
    try {
        const formattedValues = {
            username: values.username,
            password: values.password,
          };
      const res = await axios.post('/api/v1/signup', formattedValues);

      if (res.data.message === 'signed up successfully') {
        message.success('Sign Up Successful!');
        navigate('/home');
      } else {
        message.error(res.data.message);
      }
    } catch (error) {
      console.log(error);
      message.error('Something went wrong');
    }
  };

  return (
    <div className='signup-container'>
      <div className='signup-form-container'>
        <h1 className='signup-heading'><em>Sign Up</em></h1>
        <Form onFinish={onFinishHandler} layout="vertical">
          <Form.Item label='Username' name='username' rules={[{ required: true, message: 'Username is required' }]}>
            <Input className='input-field' placeholder='Enter your username' />
          </Form.Item>
          <Form.Item label='Password' name='password' rules={[{ required: true, message: 'Password is required' }]}>
            <Input.Password className='input-field' placeholder='Enter your password' />
          </Form.Item>
          <Form.Item>
            <Button type='primary' htmlType='submit' className='signup-button'>
              SIGN UP
            </Button>
          </Form.Item>
          <Form.Item>
            <span>Already have an account? <Link to='/login' className='login-link'>Login here!</Link></span>
          </Form.Item>
        </Form>
      </div>
    </div>
  );
};

export default SignupPage;
