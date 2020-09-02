<template>
  <v-container>
    <v-progress-linear color="primary" v-if="loading" indeterminate />
    <v-row v-else>
      <v-col :key="index" v-for="(post, index) in posts" lg="4">
        <v-hover v-slot:default="{ hover }">
          <v-img :src="post.images[0].file" height="350">
            <v-fade-transition>
              <div
                v-if="hover"
                style="height: 100%;"
                class="d-flex transition-fast-in-fast-out black v-card--reveal white--text"
              >
                <v-icon class="mr-3" color="white">mdi-heart</v-icon>
                {{ post.num_vote_up }}
              </div>
            </v-fade-transition>
          </v-img>
        </v-hover>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { getUserPosts } from "@/api/user";

export default {
  name: "PostGrid",
  data: () => ({
    posts: [],
    loading: true
  }),
  props: {
    username: String
  },
  mounted() {
    getUserPosts(this.username)
      .then(posts => (this.posts = posts))
      .finally(() => (this.loading = false));
  }
};
</script>

<style scoped>
.v-card--reveal {
  bottom: 0;
  width: 100%;
  opacity: 0.7;
  align-items: center;
  position: absolute;
  justify-content: center;
}
</style>
