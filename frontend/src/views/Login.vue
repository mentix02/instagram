<template>
  <div>
    <link
      href="https://fonts.googleapis.com/css?family=Indie+Flower|Overpass+Mono"
      rel="stylesheet"
    />

    <div id="wrapper">
      <div class="main-content">
        <div class="header">
          <img alt="Instagram" src="https://i.imgur.com/zqpwkLQ.png" />
        </div>
        <form method="post" @submit.prevent="submitForm" class="l-part">
          <label hidden for="username">Username</label>
          <input
            required
            autofocus
            type="text"
            id="username"
            class="input-1"
            v-model="username"
            autocomplete="off"
            placeholder="Username"
          />
          <div class="overlap-text">
            <label hidden for="password">Password</label>
            <input
              required
              id="password"
              type="password"
              class="input-2"
              v-model="password"
              placeholder="Password"
            />
            <a href="#">Forgot?</a>
          </div>
          <input type="submit" value="Log in" class="btn" />
          <div
            class="red--text"
            v-if="errorMessage"
            style="font-size: 16px; text-align: center;"
          >
            <br />
            {{ errorMessage }}
          </div>
        </form>
      </div>
      <div class="sub-content">
        <div class="s-part">
          Don't have an account? <a href="#">Sign up</a>.
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { logIn } from "@/api/auth";

export default {
  name: "Login",
  data: () => ({
    username: "",
    password: "",
    errorMessage: null
  }),
  methods: {
    submitForm() {
      console.log("submitting!");
      logIn(this.username, this.password).then(data => {
        if (data.data) {
          this.errorMessage = "Invalid credentials provided.";
        } else {
          if (data.token) {
            this.$store.commit("setToken", data.token);
            this.$store.commit("setUsername", this.username);
            this.$router.push({ name: "Home" });
          }
        }
      });
    }
  }
};
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
}

body {
  background-color: #eee;
}

#wrapper {
  width: 500px;
  height: 50%;
  overflow: hidden;
  border: 0 solid #000;
  margin: 50px auto;
  padding: 10px;
}

.main-content {
  width: 350px;
  height: 35%;
  margin: 10px auto;
  background-color: #fff;
  border: 2px solid #e6e6e6;
  padding: 40px 50px;
}

.header {
  border: 0 solid #000;
  margin-bottom: 5px;
}

.header img {
  height: 50px;
  width: 175px;
  margin: auto;
  position: relative;
  left: 40px;
}

.input-1,
.input-2 {
  width: 100%;
  margin-bottom: 5px;
  padding: 8px 12px;
  border: 1px solid #dbdbdb;
  box-sizing: border-box;
  border-radius: 3px;
}

.overlap-text {
  position: relative;
}

.overlap-text a {
  top: 10px;
  right: 10px;
  color: #003569;
  font-size: 14px;
  position: absolute;
  text-decoration: none;
}

.btn {
  width: 100%;
  background-color: #3897f0;
  border: 1px solid #3897f0;
  padding: 5px 12px;
  color: #fff;
  font-weight: bold;
  cursor: pointer;
  border-radius: 3px;
}

.sub-content {
  width: 350px;
  height: 40%;
  margin: 10px auto;
  border: 1px solid #e6e6e6;
  padding: 20px 50px;
  background-color: #fff;
}

.s-part {
  text-align: center;
}

.s-part a {
  text-decoration: none;
  cursor: pointer;
  color: #3897f0;
}
</style>
