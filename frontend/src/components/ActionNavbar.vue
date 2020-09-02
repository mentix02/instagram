<template>
  <div>
    <v-bottom-navigation color="green" app grow fixed horizontal hide-on-scroll>
      <v-btn @click="sheet = true">
        <span>Add Post</span>
        <v-icon>mdi-plus</v-icon>
      </v-btn>
      <v-btn exact :to="{ name: 'Bookmarks' }">
        <span>Bookmarks</span>
        <v-icon>mdi-bookmark</v-icon>
      </v-btn>
    </v-bottom-navigation>
    <v-bottom-sheet v-model="sheet" inset>
      <v-sheet class="text-center" height="400px">
        <v-row align="center" justify="center">
          <v-col lg="6" sm="12">
            <v-form
              class="my-4"
              lazy-validation
              ref="uploadForm"
              v-model="uploadFormValid"
              enctype="multipart/form-data"
            >
              <uploader
                autofocus
                type=""
                title=""
                accept="image/*"
                :autoUpload="false"
                v-model="imageList"
                :enableCompress="false"
              />
              <v-textarea
                solo
                required
                rows="5"
                auto-grow
                hide-details
                :counter="500"
                v-model="caption"
                label="Post caption"
                :rules="captionRules"
              ></v-textarea>
              <v-btn
                dark
                color="green"
                @click="uploadImage"
                class="text-center mt-4"
              >
                Upload
              </v-btn>
            </v-form>
          </v-col>
        </v-row>
      </v-sheet>
    </v-bottom-sheet>
  </div>
</template>

<script>
import Uploader from "vux-uploader-component";
import FileUpload from "@/components/FileUpload";

export default {
  name: "ActionNavbar",
  components: {
    Uploader,
    FileUpload
  },
  data: () => ({
    caption: "",
    sheet: false,
    imageList: [],
    captionRules: [],
    uploadFormValid: true,
    formData: new FormData()
  }),
  methods: {
    uploadImage() {
      let data = { images: [], caption: this.caption };
      this.imageList.forEach(image => {
        data.images.push(image);
      });
      this.$store
        .dispatch("uploadPost", data)
        .then(value => {
          if (value.error) console.log(value.error);
        })
        .catch(reason => console.log("reason", reason))
        .finally(() => {
          this.caption = "";
          this.sheet = false;
          this.imageList = [];
          this.formData = new FormData();
        });
    }
  }
};
</script>
