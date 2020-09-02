import Vue from "vue";
import Vuex from "vuex";

import {
  likePost,
  unlikePost,
  createPost,
  bookmarkPost,
  removeBookmark
} from "@/api/post";
import { followRequestAction, followRequests } from "@/api/feed";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    posts: null,
    requests: null,
    notifications: [],
    token: localStorage.getItem("token") || null,
    username: localStorage.getItem("username") || null
  },
  actions: {
    acceptRequest({ commit, state }, requestId) {
      const index = state.requests.findIndex(
        request => request.id === requestId
      );
      if (index !== -1)
        followRequestAction(requestId, 1).then(() => {
          commit("removeRequest", index);
        });
    },
    rejectRequest({ commit, state }, requestId) {
      const index = state.requests.findIndex(
        request => request.id === requestId
      );
      if (index !== -1)
        followRequestAction(requestId, 0).then(() => {
          commit("removeRequest", index);
        });
    },
    likePost({ commit, state }, postId) {
      const index = state.posts.findIndex(post => post.id === postId);
      if (index !== -1)
        likePost(postId).then(() => {
          commit("setPostFieldStatus", {
            status: true,
            postIndex: index,
            field: "is_liked"
          });
          commit("setPostFieldStatus", {
            postIndex: index,
            field: "num_vote_up",
            status: state.posts[index].num_vote_up + 1
          });
        });
    },
    unlikePost({ commit, state }, postId) {
      const index = state.posts.findIndex(post => post.id === postId);
      if (index !== -1)
        unlikePost(postId).then(() => {
          commit("setPostFieldStatus", {
            status: false,
            postIndex: index,
            field: "is_liked"
          });
          commit("setPostFieldStatus", {
            postIndex: index,
            field: "num_vote_up",
            status: state.posts[index].num_vote_up - 1
          });
        });
    },
    bookmarkPost({ commit, state }, postId) {
      const index = state.posts.findIndex(post => post.id === postId);
      if (index !== -1)
        bookmarkPost(postId)
          .then(() =>
            commit("setPostFieldStatus", {
              status: true,
              postIndex: index,
              field: "is_bookmarked"
            })
          )
          .catch(err => console.log(err));
    },
    removeBookmarkPost({ commit, state }, postId) {
      const index = state.posts.findIndex(post => post.id === postId);
      if (index !== -1)
        removeBookmark(postId)
          .then(err => {
            console.log(err);
            commit("setPostFieldStatus", {
              status: false,
              postIndex: index,
              field: "is_bookmarked"
            });
          })
          .catch(err => {
            console.log(err);
          });
    },
    uploadPost({ commit }, data) {
      return createPost(data)
        .then(data => {
          console.log(data);
          commit("appendToPosts", data);
          return data;
        })
        .catch(err => err.response);
    }
  },
  mutations: {
    logout(state) {
      state.posts = null;
      state.token = null;
      state.username = null;
      state.requests = null;
      localStorage.clear();
    },
    setUsername(state, username) {
      state.username = username;
      localStorage.setItem("username", username);
      followRequests()
        .then(data => (state.requests = data))
        .catch(err => console.log(err));
    },
    setToken(state, token) {
      state.token = token;
      localStorage.setItem("token", token);
    },
    setPosts(state, posts) {
      state.posts = posts;
    },
    setRequests(state, requests) {
      state.requests = requests;
    },
    removeRequest(state, index) {
      state.requests.splice(index);
    },
    appendToPosts(state, post) {
      state.posts.unshift(post);
    },
    setPostFieldStatus(state, { postIndex, field, status }) {
      state.posts[postIndex][field] = status;
    }
  },
  getters: {
    posts: state => state.posts,
    notificationLength: state => {
      let total = state.notifications.length;
      if (state.requests !== null) total += state.requests.length;
      return total;
    },
    isAuthenticated: state => !!state.token
  }
});
