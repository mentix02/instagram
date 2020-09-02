<template>
  <v-app>
    <Navigation
      v-if="this.$store.getters.isAuthenticated"
      :class="
        this.$store.getters.isAuthenticated ? 'pt-6 pb-12' : 'hidden-sm-and-up'
      "
    />
    <div :class="this.$store.getters.isAuthenticated ? '' : 'hidden-sm-and-up'">
      <br /><br />
    </div>
    <v-main>
      <v-container>
        <div class="mt-sm-0">
          <router-view />
        </div>
      </v-container>
    </v-main>
    <ActionNavbar
      :class="this.$store.getters.isAuthenticated ? '' : 'hidden-sm-and-up'"
    />
  </v-app>
</template>

<script>
import Navigation from "@/components/Navigation";
import ActionNavbar from "@/components/ActionNavbar";

export default {
  name: "App",
  components: { ActionNavbar, Navigation }
};
</script>
