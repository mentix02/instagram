<template>
  <uploader name="images" title="" v-model="imageList" />
</template>

<script>
import Uploader from "vux-uploader-component";
export default {
  name: "FileUpload",
  components: { Uploader },
  data: () => ({ imageList: [] })
};
</script>
