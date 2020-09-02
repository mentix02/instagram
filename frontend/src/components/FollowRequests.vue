<template>
  <v-row>
    <v-col lg="8" order-lg="2" offset-lg="2">
      <v-list>
        <v-subheader><h2>Follow Requests</h2></v-subheader>
        <FollowRequest
          :key="index"
          :id="request.id"
          :name="request.requester.name"
          :picture="request.requester.picture"
          :username="request.requester.username"
          v-for="(request, index) in this.$store.state.requests"
        />
      </v-list>
    </v-col>
  </v-row>
</template>

<script>
import { followRequests } from "@/api/feed";
import FollowRequest from "@/components/FollowRequest";

export default {
  name: "FollowRequests",
  components: { FollowRequest },
  mounted() {
    if (this.$store.state.requests === null) {
      followRequests()
        .then(data => this.$store.commit("setRequests", data))
        .catch(err => console.log(err));
    }
  }
};
</script>
