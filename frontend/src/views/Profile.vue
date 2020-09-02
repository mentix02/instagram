<template>
  <v-container>
    <br />
    <v-row v-if="user !== null">
      <v-col sm="12" lg="2" offset-lg="2">
        <v-avatar width="200" height="200">
          <v-img :src="user.picture" />
        </v-avatar>
      </v-col>
      <v-col lg="5" offset-lg="1" order-lg="2" class="px-lg-12">
        <p class="mb-2" style="font-weight: 300; font-size: 28px;">
          <span class="mr-4">{{ user.username }}</span>
          <v-btn class="mr-4" small :ripple="false" outlined v-if="currentUser">
            Edit Profile
          </v-btn>
          <v-btn
            small
            outlined
            class="mr-4"
            :ripple="false"
            @click="handleUnfollowClick"
            v-else-if="user.being_followed"
          >
            UNFOLLOW
          </v-btn>
          <v-btn
            dark
            small
            v-else-if="!displayRequested"
            color="blue"
            class="mr-4"
            :ripple="false"
            @click="handleFollowClick"
          >
            <b>FOLLOW</b>
          </v-btn>
          <v-btn v-else small outlined :ripple="false">
            REQUESTED
          </v-btn>
          <v-btn
            icon
            :ripple="false"
            v-if="currentUser"
            @click.stop="settingsDialogue = true"
          >
            <v-icon>mdi-cog</v-icon>
          </v-btn>
          <v-dialog
            width="300"
            v-if="currentUser"
            v-model="settingsDialogue"
            style="border-radius: 25px !important;"
          >
            <v-list>
              <v-list-item @click="logout">
                <v-list-item-title class="text-center red--text">
                  Logout
                </v-list-item-title>
              </v-list-item>
            </v-list>
          </v-dialog>
        </p>
        <v-row>
          <v-col cols="4">
            <b>{{ user.post_count }}</b> posts
          </v-col>
          <v-col cols="4" @click="handleFollowUsersList(true)">
            <b>{{ user.follower_count }}</b> followers
          </v-col>
          <v-col cols="4" @click="handleFollowUsersList(false)">
            <b>{{ user.following_count }}</b> following
          </v-col>
          <v-dialog scrollable width="300" v-model="usersDialogue">
            <v-progress-linear v-if="dialogueLoading" color="primary" />
            <v-list v-else-if="users.length !== 0">
              <v-list-item
                :key="index"
                v-if="users.length !== 0"
                @click.stop="followersDialogue = false"
                v-for="(fUser, index) in users"
                :to="{ name: 'Profile', params: { username: fUser.username } }"
              >
                <v-list-item-avatar>
                  <v-img :src="fUser.picture" />
                </v-list-item-avatar>
                <v-list-item-content>
                  <v-list-item-title>{{ fUser.username }}</v-list-item-title>
                  <v-list-item-subtitle>
                    {{ fUser.name }}
                  </v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
            </v-list>
          </v-dialog>
        </v-row>
        <v-row>
          <v-col>
            <h3>{{ user.name }}</h3>
            <p>{{ user.bio }}</p>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
    <PostGrid v-if="loadPostGrid" :username="this.user.username" />
    <h3 class="text-center" v-else>follow this user to see their posts</h3>
  </v-container>
</template>

<script>
import { userFollowAction } from "@/api/feed";
import { getFollowers, getFollowing, getProfileDetail } from "@/api/user";
import PostGrid from "@/components/PostGrid";

export default {
  name: "Profile",
  components: { PostGrid },
  data: () => ({
    users: [],
    user: null,
    usersDialogue: false,
    dialogueLoading: true,
    displayRequested: false,
    settingsDialogue: false
  }),
  mounted() {
    getProfileDetail(this.$route.params.username)
      .then(data => {
        if (data.being_followed === null) this.displayRequested = true;
        this.user = data;
      })
      .catch(err => console.log(err));
  },
  watch: {
    $route: function() {
      if (this.user.username !== this.$route.params.username) {
        getProfileDetail(this.$route.params.username)
          .then(data => (this.user = data))
          .catch(err => console.log(err));
      }
    }
  },
  computed: {
    loadPostGrid() {
      if (this.user === null) return false;
      else
        return (
          !this.user.private ||
          this.user.username === this.$store.state.username ||
          this.user.being_followed === true
        );
    },
    currentUser() {
      return this.$route.params.username === this.$store.state.username;
    }
  },
  methods: {
    logout() {
      this.$store.commit("logout");
      this.$router.push({ name: "Login" });
    },
    handleFollowUsersList(followers = true) {
      if (!this.user.being_followed) {
        console.log("nice");
        if (this.$store.state.username !== this.$route.username) return;
      }
      this.usersDialogue = true;
      this.dialogueLoading = true;
      const getter = followers ? getFollowers : getFollowing;
      getter(this.user.username)
        .then(data => {
          console.log(data);
          this.users = data;
        })
        .finally(() => (this.dialogueLoading = false));
    },
    handleUnfollowClick() {
      userFollowAction(this.user.id, false).then(_ => {
        this.user.follower_count = this.user.follower_count - 1;
        this.user.being_followed = false;
      });
    },
    handleFollowClick() {
      userFollowAction(this.user.id).then(_ => {
        if (this.user.private) this.displayRequested = true;
        else {
          this.user.being_followed = true;
          this.user.follower_count = this.user.follower_count + 1;
        }
      });
    }
  }
};
</script>
