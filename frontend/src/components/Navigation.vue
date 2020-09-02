<template>
  <v-app-bar fixed flat dense color="white" class="mb-10">
    <v-toolbar-title style="font-family: 'Billabong', cursive;">
      <router-link to="/" style="text-decoration: none; color: black">
        <p class="ml-sm-1 ml-lg-6" style="font-size: 40px">Instagram</p>
      </router-link>
    </v-toolbar-title>
    <v-spacer></v-spacer>
    <v-row dense justify="center" class="hidden-sm-and-down">
      <v-col offset-lg="1" lg="6">
        <v-text-field
          solo
          class="pt-0 mt-0"
          clearable
          single-line
          type="search"
          label="search"
          prepend-inner-icon="mdi-magnify"
        />
      </v-col>
    </v-row>
    <v-spacer></v-spacer>
    <div class="mr-6">
      <v-btn
        icon
        large
        :key="index"
        color="black"
        :ripple="false"
        active-class="no-active"
        :to="navLink.to"
        v-for="(navLink, index) in navLinks"
      >
        <v-badge
          overlap
          bordered
          color="red"
          :content="numNotifications"
          :value="navLink.to.name === 'Notifications' && numNotifications > 0"
        >
          <v-icon>
            {{ route === navLink.to.name ? navLink.icon : navLink.activeIcon }}
          </v-icon>
        </v-badge>
      </v-btn>
    </div>
  </v-app-bar>
</template>

<script>
import { followRequests } from "@/api/feed";

const genRoute = (name, params = null) =>
  params === null ? { name } : { name, params };

const genLink = (name, icon) => ({
  icon: icon,
  to: genRoute(name),
  activeIcon: `${icon}-outline`
});

export default {
  name: "Navigation",
  computed: {
    numNotifications() {
      if (this.$store.state.requests === null)
        followRequests()
          .then(data => this.$store.commit("setRequests", data))
          .catch(err => console.log(err));
      return this.$store.getters.notificationLength;
    },
    route() {
      return this.$route.name;
    },
    navLinks() {
      let links = [
        genLink("Home", "mdi-home"),
        genLink("Explore", "mdi-compass"),
        genLink("Notifications", "mdi-heart")
      ];
      if (this.$store.state.username !== null)
        links.push({
          to: genRoute("Profile", {
            username: this.$store.state.username
          }),
          icon: "mdi-account",
          activeIcon: "mdi-account-outline"
        });
      return links;
    }
  }
};
</script>

<style>
.v-btn--active.no-active::before {
  opacity: 0 !important;
}
</style>
