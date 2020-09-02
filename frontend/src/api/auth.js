import axios from "axios";

axios.defaults.headers.common["Content-Type"] = "multipart/form-data";

export const logIn = (username, password) => {
  let formData = new FormData();
  formData.set("username", username);
  formData.set("password", password);

  const url = `http://127.0.0.1:8000/api/user/token/`;

  return axios
    .post(url, formData)
    .then(res => res.data)
    .catch(err => err.response);
};
