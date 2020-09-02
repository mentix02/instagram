import Vue from "vue";
import axios from "axios";

import App from "./App.vue";

import router from "./router";
import store from "./store";
import vuetify from "./plugins/vuetify";

Vue.prototype.$http = axios;
Vue.config.productionTip = false;

const token = localStorage.getItem("token");

if (token) {
  Vue.prototype.$http.defaults.headers.common[
    "Authorization"
  ] = `Token ${token}`;
}

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount("#app");
