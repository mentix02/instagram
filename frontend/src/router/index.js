import Vue from "vue";
import VueRouter from "vue-router";

import store from "@/store";
import Home from "@/views/Home.vue";

Vue.use(VueRouter);

const requiresNoAuth = true;

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/explore",
    name: "Explore",
    component: () => import("../views/Explore")
  },
  {
    path: "/notifications",
    name: "Notifications",
    component: () => import("../views/Notifications")
  },
  {
    name: "Bookmarks",
    path: "/bookmarks",
    component: () => import("../views/Bookmarks")
  },
  {
    name: "Login",
    path: "/login",
    meta: { requiresNoAuth },
    component: () => import("../views/Login")
  },
  {
    name: "Register",
    path: "/register",
    meta: { requiresNoAuth },
    component: () => import("../views/Register")
  },
  {
    name: "Profile",
    path: "/:username",
    component: () => import("../views/Profile")
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

router.beforeEach((to, from, next) => {
  if (store.getters.isAuthenticated) {
    if (to.matched.some(record => record.meta.requiresNoAuth)) {
      next({ name: "Home" });
    } else {
      next();
    }
  } else {
    if (to.matched.some(record => record.meta.requiresNoAuth)) {
      next();
    } else {
      next({ name: "Login" });
    }
  }
});

export default router;
