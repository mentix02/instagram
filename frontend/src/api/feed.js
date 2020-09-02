import axios from "axios";

const BASE_URL = "/api/feed";

export const userFollowAction = (userId, follow = true) => {
  // Set authorization headers to authenticate.
  const token = localStorage.getItem("token");
  axios.defaults.headers.common["Authorization"] = `Token ${token}`;

  // Set form data.
  let formData = new FormData();
  formData.set("user_id", userId);

  // Generate url.
  const url = follow ? `${BASE_URL}/follow/` : `${BASE_URL}/unfollow/`;

  // Make request and return response.
  return axios
    .post(url, formData)
    .then(res => res.data)
    .catch(err => err.response);
};

export const followRequests = () => {
  // Set authorization headers to authenticate.
  const token = localStorage.getItem("token");
  axios.defaults.headers.common["Authorization"] = `Token ${token}`;

  return axios
    .get(`${BASE_URL}/requests/`)
    .then(res => res.data)
    .catch(err => err.response);
};

export const followRequestAction = (requestId, accept = 1) => {
  // Set authorization headers to authenticate.
  const token = localStorage.getItem("token");
  axios.defaults.headers.common["Authorization"] = `Token ${token}`;

  // Set form data.
  let formData = new FormData();
  formData.set("action", accept.toString());
  formData.set("follow_request_id", requestId);

  const url = `${BASE_URL}/action/`;

  return axios
    .post(url, formData)
    .then(res => res.data)
    .catch(err => err.response);
};
