<template>
  <v-card width="450" class="mx-auto">
    <v-list-item>
      <router-link
        :to="{ name: 'Profile', params: { username: user.username } }"
      >
        <v-list-item-avatar class="mr-2">
          <v-img :src="user.picture" />
        </v-list-item-avatar>
      </router-link>
      <v-list-item-content class="ml-0">
        <v-list-item-title>
          <router-link
            style="text-decoration: none; color: black"
            :to="{ name: 'Profile', params: { username: user.username } }"
          >
            {{ user.username }}
          </router-link>
        </v-list-item-title>
      </v-list-item-content>
      <v-spacer></v-spacer>
      <v-btn icon>
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn>
    </v-list-item>
    <v-carousel height="350" :continuous="false" hide-delimiter-background>
      <v-carousel-item v-for="image in images">
        <v-img height="350" :src="image.file"></v-img>
      </v-carousel-item>
    </v-carousel>
    <v-card-actions class="pb-0">
      <v-btn
        icon
        @click="like"
        :ripple="false"
        :color="is_liked ? 'red' : 'black'"
      >
        <v-icon>
          {{ is_liked ? "mdi-heart" : "mdi-heart-outline" }}
        </v-icon>
      </v-btn>
      <v-btn icon color="black">
        <v-icon>mdi-send-outline</v-icon>
      </v-btn>
      <v-btn icon color="black">
        <v-icon>mdi-comment-outline</v-icon>
      </v-btn>
      <v-spacer></v-spacer>
      <v-btn icon @click="bookmark" color="black">
        <v-icon>
          {{ is_bookmarked ? "mdi-bookmark" : "mdi-bookmark-outline" }}
        </v-icon>
      </v-btn>
    </v-card-actions>
    <v-card-subtitle class="px-0 py-0 ml-4">
      {{ likes }} likes
    </v-card-subtitle>
    <v-card-text style="padding-top: 2px; color: black;">
      {{ caption }}
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: "FeedPostItem",
  props: {
    user: Object,
    likes: Number,
    images: Array,
    postId: Number,
    caption: String,
    is_liked: Boolean,
    is_bookmarked: Boolean
  },
  methods: {
    like() {
      const dispatchMethod = this.is_liked ? "unlikePost" : "likePost";
      this.$store.dispatch(dispatchMethod, this.postId);
    },
    bookmark() {
      const dispatchMethod = this.is_bookmarked
        ? "removeBookmarkPost"
        : "bookmarkPost";
      this.$store.dispatch(dispatchMethod, this.postId);
    }
  }
};
</script>
