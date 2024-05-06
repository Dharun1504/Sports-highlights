import React from 'react';
import { Form, Input, Button, message } from 'antd';
import { Link, useNavigate } from 'react-router-dom';
import axios from 'axios';
import '../styles/LoginPage.css';

const LoginPage = ({ setAuthenticated }) => {
  const navigate = useNavigate();
  
  const onFinishHandler = async (values) => {
    try {
      const formattedValues = {
        username: values.username,
        password: values.password,
      };
      
      const res = await axios.post('/api/v1/login', formattedValues);

      if (res.data.message === 'Login successful') {
        message.success('Login Successful!');
        setAuthenticated(true);
        navigate('/home');
      } else {
        message.error(res.data.message);
        setAuthenticated(false);
      }
    } catch (error) {
      console.log(error);
      message.error('Something went wrong');
      setAuthenticated(false);
    }
  };

  return (
    <div className='login-container'>
      <div className='login-form-container'>
        <h1 className='login-heading'><em>Login</em></h1>
        <Form onFinish={onFinishHandler} layout="vertical">
          <Form.Item label='Username' name='username' rules={[{ required: true, message: 'Username is required' }]}>
            <Input className='input-field' placeholder='Enter your username' />
          </Form.Item>
          <Form.Item label='Password' name='password' rules={[{ required: true, message: 'Password is required' }]}>
            <Input.Password className='input-field' placeholder='Enter your password' />
          </Form.Item>
          <Form.Item>
            <Button type='primary' htmlType='submit' className='login-button'>
              LOGIN
            </Button>
          </Form.Item>
          <Form.Item>
            <span>Don't have an account? <Link to='/register' className='register-link'>Register now!</Link></span>
          </Form.Item>
        </Form>
      </div>
    </div>
  );
};

export default LoginPage;
