<template>
  <v-list-item two-line>
    <v-list-item-avatar>
      <v-img :src="picture" />
    </v-list-item-avatar>
    <v-list-item-content>
      <v-list-item-title>{{ username }}</v-list-item-title>
      <v-list-item-subtitle>{{ name }}</v-list-item-subtitle>

      <!--      <v-btn small outlined>reject</v-btn>-->
    </v-list-item-content>
    <v-list-item-action>
      <v-btn @click="reject" :ripple="false" small outlined>REJECT</v-btn>
    </v-list-item-action>
    <v-list-item-action>
      <v-btn
        small
        dark
        color="blue"
        elevation="0"
        @click="accept"
        :ripple="false"
      >
        ACCEPT
      </v-btn>
    </v-list-item-action>
  </v-list-item>
</template>

<script>
export default {
  name: "FollowRequest",
  props: {
    id: Number,
    name: String,
    picture: String,
    username: String
  },
  methods: {
    accept() {
      this.$store.dispatch("acceptRequest", this.id);
    },
    reject() {
      this.$store.dispatch("rejectRequest", this.id);
    }
  }
};
</script>
