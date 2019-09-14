<template>
  <div class="app flex-row align-items-center" >
    <div class="container">
      <b-row class="justify-content-center">
        <b-col md="8">
          <b-card-group>
            <b-card no-body class="p-4" style="background: linear-gradient(to right, #c2e59c, #64b3f4);">
              <b-card-body>
                <b-form id="mainForm">
                  <h1>Prijava</h1>
                  <p class="text-muted" style="font-color:red;">Prijavi se na svoji račun</p>
                  <b-input-group class="mb-3">
                    <b-input-group-prepend>
                      <b-input-group-text>
                        <i class="icon-user"></i>
                      </b-input-group-text>
                    </b-input-group-prepend>
                    <b-form-input
                      onfocus="this.value=''"
                      v-model="username"
                      type="text"
                      class="form-control"
                      placeholder="Korisničko ime"
                      autocomplete="username email"
                      required
                    />
                  </b-input-group>
                  <b-input-group class="mb-4">
                    <b-input-group-prepend>
                      <b-input-group-text>
                        <i class="icon-lock"></i>
                      </b-input-group-text>
                    </b-input-group-prepend>
                    <b-form-input
                      onfocus="this.value=''"
                      v-model="password"
                      type="password"
                      class="form-control"
                      placeholder="Lozinka"
                      autocomplete="current-password"
                      required
                    />
                  </b-input-group>
                  <b-row>
                    <b-col lg="12">
                      <b-form-group
                        description
                        label="ADMIN"
                        label-for="basicText"
                        :label-cols="2"
                      >
                        <c-switch
                          style="margin-top: 8px; margin-left: 20px;"
                          class="mx-1"
                          size="sm"
                          color="primary"
                          v-model="isAdmin"
                          variant="pill"
                        />
                      </b-form-group>
                    </b-col>
                  </b-row>
                  <b-row>
                    <b-col cols="6">
                      <b-button
                        type="submit"
                        :disabled="isLoading"
                        @click="login"
                        variant="primary"
                        class="px-4"
                      >
                        <span v-if="isLoading">
                          <i class="fa fa-spin fa-spinner"></i> Loging in...
                        </span>
                        <span v-if="!isLoading">Login</span>
                      </b-button>
                    </b-col>
                    <b-col cols="6" class="text-right">
                      <!-- <b-button variant="link" class="px-0">Forgot password?</b-button> -->
                    </b-col>
                  </b-row>
                </b-form>
              </b-card-body>
            </b-card>
            <!-- <b-card no-body class="text-white bg-primary py-5 d-md-down-none" style="width:44%">
              <b-card-body class="text-center">
                <div>
                  <h2>Sign up</h2>
                  <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
                  <b-button variant="primary" class="active mt-3">Register Now!</b-button>
                </div>
              </b-card-body>
            </b-card>-->
          </b-card-group>
        </b-col>
      </b-row>
    </div>
  </div>
</template>

<script>
import { Switch as cSwitch } from "@coreui/vue";
import axios from "axios";
export default {
  name: "Login",
  components: {
    cSwitch
  },
  mounted() {},
  data() {
    return {
      username: "",
      password: "",
      isAdmin: false,
      isLoading: false
    };
  },
  methods: {
    login(args) {
      let form = document.getElementById("mainForm");
      if (!form.checkValidity()) {
        args.srcElement.click();
        return;
      }
      args.preventDefault();
      this.isLoading = true;
      axios
        .post("/api/Login", {
          username: this.username,
          password: this.password,
          isadmin: this.isAdmin
        })
        .then(res => {
          console.log(res.data);
          this.isLoading = false;
          if (res.data.error == "") {
            // this.$router.push("/");
            this.$store
              .dispatch("login", {
                token: null,
                userDetails: res.data.userObject
              })
              .then(ok => {});
          } else {
            this.username = "";
            this.password = "";
            this.isAdmin = false;

            this.$toasted.error(res.data.error, { duration: 2000 });
          }
        })
        .catch(err => {
          console.log(err);
          this.isLoading = false;
          this.$toasted.error(err, { duration: 2000 });
        });
    }
  }
};
</script>