import axios from 'axios';

const api = axios.create({
  baseURL: 'http://127.0.0.1:8001', // URL do seu servidor
});

export default api;