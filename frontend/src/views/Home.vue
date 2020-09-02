<template>
  <v-container>
    <v-row align="center" justify="center">
      <v-col lg="8" sm="12">
        <v-progress-linear color="purple" indeterminate v-if="loading" />
        <p
          class="text-center mt-4"
          style="font-size: 22px"
          v-if="!loading && posts !== null && posts.length === 0"
        >
          No posts to display... maybe follow some people?
        </p>
        <FeedPostItem
          v-else
          :key="index"
          class="mb-8"
          :user="post.user"
          :post-id="post.id"
          :images="post.images"
          :caption="post.caption"
          :is_liked="post.is_liked"
          :likes="post.num_vote_up"
          v-for="(post, index) in posts"
          :is_bookmarked="post.is_bookmarked"
        />
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
import { getFeedPosts } from "@/api/post";
import FeedPostItem from "@/components/FeedPostItem";

export default {
  name: "Home",
  data: () => ({
    loading: true
  }),
  components: { FeedPostItem },
  computed: {
    posts() {
      return this.$store.state.posts;
    }
  },
  mounted() {
    if (this.$store.state.posts === null) {
      getFeedPosts()
        .then(data => {
          if (data.length >= 0) this.$store.commit("setPosts", data);
          else console.log(data);
        })
        .finally();
    }
    this.loading = false;
  }
};
</script>
