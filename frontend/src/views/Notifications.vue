<template>
  <v-container>
    <FollowRequests />
  </v-container>
</template>
<script>
import FollowRequests from "@/components/FollowRequests";

export default {
  name: "Notifications",
  components: { FollowRequests }
};
</script>
