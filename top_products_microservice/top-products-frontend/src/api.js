// api.js (or axiosConfig.js)
import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000/api/api/apiproducts',  // Adjust with your Django backend URL
  timeout: 5000,  // Adjust timeout as needed
  headers: {
    'Content-Type': 'application/json',
    // Add other headers as required by your backend
  }
});

export default api;
