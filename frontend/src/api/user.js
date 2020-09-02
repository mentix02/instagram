import axios from "axios";

const BASE_URL = "/api/user";
axios.defaults.headers.common["Content-Type"] = "multipart/form-data";

export const getProfileDetail = username => {
  const token = localStorage.getItem("token");
  if (token) axios.defaults.headers.common["Authorization"] = `Token ${token}`;
  return axios
    .get(`${BASE_URL}/detail/${username}/`)
    .then(res => res.data)
    .catch(err => err.response);
};

export const getFollowers = username =>
  axios
    .get(`${BASE_URL}/followers/${username}/`)
    .then(res => res.data)
    .catch(err => err.response);

export const getFollowing = username =>
  axios
    .get(`${BASE_URL}/following/${username}/`)
    .then(res => res.data)
    .catch(err => err.response);

export const getUserPosts = username =>
  axios
    .get(`${BASE_URL}/posts/${username}/`)
    .then(res => res.data)
    .catch(err => err.response);
