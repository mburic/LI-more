<template>
  <div class="animated fadeIn">
    <b-row>
      <b-col lg="12">
        <b-card>
          <div slot="header">
            <strong>UPRAVLJANJE KORISNIKA</strong>
            <!-- <div class="card-header-actions">
              <b-link href="#" class="card-header-action btn-close">
                <i class="fa fa-clear"></i> CLEAR ALL
              </b-link>
            </div>-->
          </div>
          <b-row>
            <b-col lg="4" class="list-users">
              <b-list-group style="max-height:70vh;overflow-y:auto;">
                <b-list-group-item
                  v-for="(user,index) in listOfUsers"
                  :key="'litem'+index"
                  @click="selectUser(user)"
                  class="d-flex justify-content-between align-items-center"
                >
                  <b-row>
                    <b-col lg="12">
                      <span>
                        <strong>{{capitalize(user.fname)}} {{capitalize(user.sname)}}</strong>
                      </span>
                      <br />
                      <span>{{user.email}}</span>
                    </b-col>
                  </b-row>

                  <b-badge v-if="user.isadmin" variant="primary" pill>Admin</b-badge>
                </b-list-group-item>

                <center v-if="isLoadingUserList">
                  <span>
                    <i style="font-size:30px;margin:15px;" class="fa fa-spin fa-spinner"></i>
                  </span>
                </center>
              </b-list-group>
            </b-col>
            <b-col lg="8" class="registration-form">
              <b-form id="mainForm">
                <b-form-group description label="IME" label-for="basicText" :label-cols="3">
                  <b-form-input required v-model="userDetails.fname" type="text" placeholder style="background-color:#fff6ae;"></b-form-input>
                </b-form-group>
                <b-form-group description label="PREZIME" label-for="basicText" :label-cols="3">
                  <b-form-input required v-model="userDetails.sname" type="text" placeholder style="background-color:#fff6ae;"></b-form-input>
                </b-form-group>
                <b-form-group description label="EMAIL" label-for="basicText" :label-cols="3">
                  <b-form-input
                    style="background-color:#fff6ae;"
                    required
                    v-model="userDetails.email"
                    type="email"
                    placeholder
                    :disabled="isInEditMode"
                  ></b-form-input>
                </b-form-group>
                <b-form-group description label="LOZINKA" label-for="basicText" :label-cols="3">
                  <b-form-input
                    style="background-color:#fff6ae;"
                    :required="!isInEditMode"
                    v-model="userDetails.password"
                    type="password"
                    placeholder
                  ></b-form-input>
                </b-form-group>
                <b-form-group description label="KORISNIČKO IME" label-for="basicText" :label-cols="3">
                  <b-form-input
                    style="background-color:#fff6ae;"
                    required
                    v-model="userDetails.username"
                    type="text"
                    placeholder
                    :disabled="isInEditMode"
                  ></b-form-input>
                </b-form-group>
                <b-form-group description label="ADMIN" label-for="basicText" :label-cols="3">
                  <c-switch
                    v-model="userDetails.isadmin"
                    class="mx-1"
                    color="primary"
                    variant="pill"
                  />
                </b-form-group>
                <b-form-group description label="ISPOSTAVA" label-for="basicText" :label-cols="3">
                  <b-form-input required v-model="userDetails.ispostava" type="text" placeholder style="background-color:#fff6ae;"></b-form-input>
                </b-form-group>
                <b-form-group description label="KONTAKT" label-for="basicText" :label-cols="3">
                  <b-form-input required v-model="userDetails.kontakt" type="text" placeholder style="background-color:#fff6ae;"></b-form-input>
                </b-form-group>

                <div class="form-actions">
                  <b-button
                    v-if="!isInEditMode"
                    :disabled="isLoading||isLoadingUserList"
                    @click="saveUser"
                    type="submit"
                    style="margin-right:20px"
                    variant="success"
                  >
                    <span v-if="isLoading||isLoadingUserList">
                      <i class="fa fa-spin fa-spinner"></i> SPREMANJE...
                    </span>
                    <span v-if="!(isLoading||isLoadingUserList)">SPREMI</span>
                  </b-button>
                  <b-button
                    @click="updateUser"
                    v-if="isInEditMode"
                    :disabled="isLoading||isLoadingUserList"
                    type="submit"
                    style="margin-right:20px"
                    variant="success"
                  >
                    <span v-if="!isDeleting&&(isLoading||isLoadingUserList)">
                      <i class="fa fa-spin fa-spinner"></i> AŽURIRANJE...
                    </span>
                    <span v-if="!(!isDeleting&&(isLoading||isLoadingUserList))">AŽURIRAJ</span>
                  </b-button>
                  <b-button
                    @click="deleteUser"
                    v-if="isInEditMode"
                    :disabled="isLoading||isLoadingUserList"
                    type="button"
                    style="margin-right:20px"
                    variant="danger"
                  >
                    <span v-if="isDeleting&&(isLoading||isLoadingUserList)">
                      <i class="fa fa-spin fa-spinner"></i> BRISANJE...
                    </span>
                    <span v-if="!(isDeleting&&(isLoading||isLoadingUserList))">OBRIŠI</span>
                  </b-button>
                  <b-button
                    @click="reset"
                    :disabled="isLoading||isLoadingUserList"
                    type="button"
                    style="margin-right:20px"
                    variant="info"
                  >PONIŠTI</b-button>
                </div>
              </b-form>
            </b-col>
          </b-row>
        </b-card>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import CommonUtils from "../../utils/CommonUtils"
import { Switch as cSwitch } from "@coreui/vue";
import axios from "axios";
export default {
  name: "forms",
  components: {
    cSwitch
  },
  data() {
    return {
      isLoadingUserList: false,
      isLoading: false,
      isInEditMode: false,
      isDeleting: false,
      userDetails: {
        fname: "",
        sname: "",
        email: "",
        isadmin: false,
        ispostava: "",
        kontakt: "",
        username: "",
        password: ""
      },
      listOfUsers: []
    };
  },
  mounted() {
    this.fetchUsers();
  },
  methods: {
    capitalize(str) {
      if (str == null || str == undefined) {
        return str;
      }

      return ("" + str[0]).toUpperCase() + str.substring(1, str.length);
    },
    fetchUsers() {
      this.isLoadingUserList = true;
      axios
        .post("/api/GetUsers", {
          userid: this.$store.getters.userDetails.userid
        })
        .then(res => {
          console.log(res.data);
          this.isLoadingUserList = false;
          if (res.data.error != "") {
            // show error
            this.showMessage(true, res.data.error);
            return;
          }
          //****ISPRAVAK*****

          this.listOfUsers = res.data.data;
        })
        .catch(err => {
          console.log(err);
          this.showMessage(true, err);
          this.isLoadingUserList = false;
        });
    },
    isValidInput(args){
      //CommonUtils
      let form = document.getElementById("mainForm");
      if (!form.checkValidity()) {
        args.srcElement.click();
        return false;
      }
      args.preventDefault();
      if(!CommonUtils.validatePhoneNumber(this.userDetails.kontakt)){
        this.showMessage(true, "Please enter valid kontakt.")
        return false
      }
      return true
    },
    saveUser(args) {
      if(!this.isValidInput(args)){
        return
      }
      this.isLoading = true;
      axios
        .post("/api/Registration", this.userDetails)
        .then(res => {
          console.log(res.data);
          this.isLoading = false;
          if (res.data.error != "") {
            // show error
            this.showMessage(true, res.data.error);
            return;
          }
          this.reset();
          this.fetchUsers();
          this.showMessage(false, "User details saved successfully.");
        })
        .catch(err => {
          console.log(err);
          this.showMessage(true, err);
          this.isLoading = false;
        });
    },
    selectUser(user) {
      if (this.isLoading) {
        return;
      }
      this.userDetails = JSON.parse(JSON.stringify(user));
      this.userDetails.password = "";
      this.isInEditMode = true;
    },
    deleteUser() {
      this.isLoading = true;
      this.isDeleting = true;
      axios
        .post("/api/DeleteUser", { userid: this.userDetails.userid })
        .then(res => {
          console.log(res.data);
          this.isLoading = false;
          this.isDeleting = false;
          if (res.data.error != "") {
            // show error
            this.showMessage(true, res.data.error);
            return;
          }
          this.reset();
          this.fetchUsers();
          this.showMessage(false, "User details deleted successfully.");
        })
        .catch(err => {
          console.log(err);
          this.showMessage(true, err);
          this.isLoading = false;
          this.isDeleting = false;
        });
    },
    updateUser(args) {
      if(!this.isValidInput(args)){
        return
      }
      this.isLoading = true;
      axios
        .post("/api/UpdateUser", this.userDetails)
        .then(res => {
          console.log(res.data);
          this.isLoading = false;
          if (res.data.error != "") {
            // show error
            this.showMessage(true, res.data.error);
            return;
          }
          //this.reset();
          this.fetchUsers();
          this.showMessage(false, "User details updated successfully.");
        })
        .catch(err => {
          this.isLoading = false;
          console.log(err);
          this.showMessage(true, err);
        });
    },
    showMessage(isError, message) {
      if (isError) {
        this.$toasted.error(message, { duration: 2000 });
      } else {
        this.$toasted.success(message, { duration: 2000 });
      }
    },
    reset() {
      this.isInEditMode = false;
      this.userDetails.fname = "";
      this.userDetails.sname = "";
      this.userDetails.email = "";
      this.userDetails.isadmin = false;
      this.userDetails.ispostava = "";
      this.userDetails.kontakt = "";
      this.userDetails.username = "";
      this.userDetails.password = "";
    }
  }
};
</script>

<style scoped>
.card-body {
  padding: 0px;
  margin-right: 15px;
}
.list-group-item:hover {
  background-color: azure;
}
.list-users {
  border-right: 1px solid #e4e7ea;
  padding-right: 0;
}
.registration-form {
  padding: 20px 35px 20px 35px;
}
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter,
.fade-leave-to {
  opacity: 0;
}
</style>
