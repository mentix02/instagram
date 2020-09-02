import axios from "axios";

const BASE_URL = "/api";
const token = localStorage.getItem("token");

if (token) {
  axios.defaults.headers.common["Authorization"] = `Token ${token}`;
}
axios.defaults.headers.common["Content-Type"] = "multipart/form-data";

export const getFeedPosts = () => {
  // Token has to be placed in common headers again since after login
  // this is the first method that is called.
  const token = localStorage.getItem("token");
  axios.defaults.headers.common["Authorization"] = `Token ${token}`;

  const url = `${BASE_URL}/feed/posts/`;
  return axios
    .get(url)
    .then(res => res.data)
    .catch(err => err.response);
};

export const unlikePost = postId => {
  const url = `${BASE_URL}/like/delete/${postId}/`;
  return axios
    .delete(url)
    .then(res => res.data)
    .catch(err => err.response);
};

export const likePost = postId => {
  const url = `${BASE_URL}/like/create/`;

  let formData = new FormData();
  formData.set("post", postId);
  return axios
    .post(url, formData)
    .then(res => res.data)
    .catch(err => err.response);
};

export const removeBookmark = postId => {
  const url = `${BASE_URL}/bookmark/delete/${postId}/`;
  return axios
    .delete(url)
    .then(res => res.data)
    .catch(err => err.response);
};

export const bookmarkPost = postId => {
  const url = `${BASE_URL}/bookmark/create/`;

  let formData = new FormData();
  formData.set("post", postId);

  return axios
    .post(url, formData)
    .then(res => res.data)
    .catch(err => err.response);
};

export const createPost = data => {
  const url = `${BASE_URL}/post/create/`;

  let formData = new FormData();
  formData.set("caption", data.caption);

  data.images.forEach(image =>
    formData.append("images", image.blob, image.name)
  );

  return axios
    .post(url, formData)
    .then(res => res.data)
    .catch(err => err.response);
};
