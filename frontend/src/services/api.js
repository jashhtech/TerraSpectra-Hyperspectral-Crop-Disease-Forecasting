import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000"
});

export const getHealth = async () => {
  const response = await API.get("/health");
  return response.data;
};

export default API;