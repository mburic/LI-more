<template>
  <div class="animated fadeIn">
    <b-row>
      <b-col lg="12">
        <b-card>
          <div slot="header">
            <strong>{{isInEditMode?"EDIT":"GOST"}}</strong> 
          </div>
          <b-form id="mainForm">
            <b-form-group
              description
              label="SERIJSKI BROJ PRIJAVE"
              label-for="basicText"
              :label-cols="3"
            >
              <b-form-input
                style="border: 2px solid #0088cc;"                
                required
                v-model="formDetails.serijskibrojg"
                id="basicText"
                type="text"
                placeholder
                disabled
              ></b-form-input>
            </b-form-group>
            <b-form-group label="DATUM OD" label-for="date" :label-cols="3">
              <b-form-input required v-model="formDetails.datumg_od" type="date" id="date" style="background-color:#fff6ae;"></b-form-input>
            </b-form-group>
            <b-form-group label="DATUM DO" label-for="date" :label-cols="3">
              <b-form-input required v-model="formDetails.datumg_do" type="date" id="date" style="background-color:#fff6ae;"></b-form-input>
            </b-form-group>
            <b-form-group description label="NACIN DOLASKA" label-for="basicText" :label-cols="3">
              <b-form-select
                style="background-color:#fff6ae;"
                required
                v-model="formDetails.nacindolaskag"
                id="basicText"
                type="text"
                :plain="true"
                :options="['KOPNOM', 'MOREM']"
                placeholder
              ></b-form-select>
            </b-form-group>
            <hr />
            <b-form-group description label="IME PLOVILA" label-for="basicText" :label-cols="3">
              <b-form-input
                style="background-color:#fff6ae;"
                required
                v-model="formDetails.imeplovilag"
                id="basicText"
                type="text"
                placeholder
              ></b-form-input>
            </b-form-group>
            <b-form-group description label="VRSTA PLOVILA" label-for="basicText" :label-cols="3">
              <b-form-select
                style="background-color:#fff6ae;"
                required
                v-model="formDetails.vrstaplovilag"
                id="basicText"
                type="text"
                :plain="true"
                :options="['BRODICA', 'JEDRILICA', 'MOTORNA']"
                placeholder
              ></b-form-select>
            </b-form-group>
            <b-form-group description label="OZNAKA" label-for="basicText" :label-cols="3">
              <b-form-input
                style="background-color:#fff6ae;"
                required
                v-model="formDetails.oznakag"
                id="basicText"
                type="text"
                placeholder
              ></b-form-input>
            </b-form-group>
            <b-form-group description label="DULJINA" label-for="basicText" :label-cols="3">
              <b-form-input
                style="background-color:#fff6ae;"
                required
                v-model="formDetails.duljinag"
                id="basicText"
                type="text"
                placeholder
              ></b-form-input>
            </b-form-group>
            <b-form-group
              description
              label="BROJ CLANOVA POSADE"
              label-for="basicText"
              :label-cols="3"
            >
              <b-form-input
                style="background-color:#fff6ae;"
                required
                v-model="formDetails.brojclanovag"
                id="basicText"
                type="number"
                placeholder
              ></b-form-input>
            </b-form-group>
            <hr />
            <b-form-group
              description
              label="IME ZAPOVJEDNIKA"
              label-for="basicText"
              :label-cols="3"
            >
              <b-form-input
                style="background-color:#fff6ae;"
                required
                v-model="formDetails.imeg"
                id="basicText"
                type="text"
                placeholder
              ></b-form-input>
            </b-form-group>
            <b-form-group
              description
              label="PREZIME ZAPOVJEDNIKA"
              label-for="basicText"
              :label-cols="3"
            >
              <b-form-input
                style="background-color:#fff6ae;"
                required
                v-model="formDetails.prezimeg"
                id="basicText"
                type="text"
                placeholder
              ></b-form-input>
            </b-form-group>
            <b-form-group description label="KONTAKT" label-for="basicText" :label-cols="3">
              <b-form-input
                style="background-color:#fff6ae;"
                required
                v-model="formDetails.kontaktg"
                id="basicText"
                type="text"
                placeholder
              ></b-form-input>
            </b-form-group>
            <b-form-group description label="OBRACUN" label-for="basicText" :label-cols="3">
              <b-form-input
                style="background-color:#fff6ae;"
                required
                v-model="formDetails.obracung"
                id="basicText"
                type="number"
                placeholder
              ></b-form-input>
            </b-form-group>

            <div class="form-actions">
              <b-button
                v-if="!isInEditMode"
                :disabled="isLoading"
                @click="saveForm"
                type="submit"
                style="margin-right:20px"
                variant="success"
              >
                <span v-if="isLoading">
                  <i class="fa fa-spin fa-spinner"></i> SPREMANJE...
                </span>
                <span v-if="!(isLoading)">SPREMI</span>
              </b-button>
              <b-button
                @click="updateForm"
                v-if="isInEditMode"
                :disabled="isLoading"
                type="submit"
                style="margin-right:20px"
                variant="secondary"
              >
                <span v-if="!isDeleting&&(isLoading)">
                  <i class="fa fa-spin fa-spinner"></i> AŽURIRANJE...
                </span>
                <span v-if="!(!isDeleting&&(isLoading))">AŽURIRAJ</span>
              </b-button>
              <b-button
                @click="deleteForm"
                v-if="isInEditMode"
                :disabled="isLoading"
                type="button"
                style="margin-right:20px"
                variant="danger"
              >
                <span v-if="isDeleting&&(isLoading)">
                  <i class="fa fa-spin fa-spinner"></i> BRISANJE...
                </span>
                <span v-if="!(isDeleting&&(isLoading))">OBRIŠI</span>
              </b-button>
              <b-button
                @click="reset"
                :disabled="isLoading"
                type="button"
                style="margin-right:20px"
                variant="info"
              >PONIŠTI</b-button>
            </div>
          </b-form>
        </b-card>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "forms",
  data() {
    return {
      isLoading: false,
      isInEditMode: false,
      isDeleting: false,
      formDetails: {
        actiontotake: "Insert",
        brojclanovag: "",
        datumg_do: "",
        datumg_od: "",
        duljinag: "",
        imeg: "",
        imeplovilag: "",
        kontaktg: "",
        nacindolaskag: "",
        obracung: "",
        oznakag: "",
        prezimeg: "",
        username: this.$store.getters.userDetails.username,
        vrstaplovilag: ""
      }
    };
  },
  mounted() {
    if (this.$store.getters.editFormName == "/form4") {
      this.isInEditMode = true;
      this.formDetails = JSON.parse(
        JSON.stringify(this.$store.getters.editFormData)
      );
      this.formDetails.actiontotake = "Update";
      this.formDetails.username = this.$store.getters.userDetails.username;
      this.$store.commit("editFormName", null);
      this.$store.commit("editFormData", null);
      return;
    }
    this.getRandomNumber();
  },
  methods: {
    saveForm(args) {
      //Prijavad
      let form = document.getElementById("mainForm");
      if (!form.checkValidity()) {
        args.srcElement.click();
        return;
      }
      args.preventDefault();
      this.isLoading = true;
      axios
        .post("/api/PrijavagoForm4", this.formDetails) //
        .then(res => {
          console.log(res.data);
          this.isLoading = false;
          if (res.data.error != "") {
            // show error
            this.showMessage(true, res.data.error);
            return;
          }
          this.reset();
          this.showMessage(false, "Form data saved successfully.");
          this.getRandomNumber();
        })
        .catch(err => {
          this.isLoading = false;
          console.log(err);
          this.showMessage(true, err);
        });
    },
    reset() {
      if (this.isInEditMode) {
        this.getRandomNumber();
      }
      this.isInEditMode = false;
      this.$store.commit("editFormName", null);
      this.$store.commit("editFormData", null);
      this.formDetails.brojclanovag = "";
      this.formDetails.datumg_do = "";
      this.formDetails.datumg_od = "";
      this.formDetails.duljinag = "";
      this.formDetails.imeg = "";
      this.formDetails.imeplovilag = "";
      this.formDetails.kontaktg = "";
      this.formDetails.nacindolaskag = "";
      this.formDetails.obracung = "";
      this.formDetails.oznakag = "";
      this.formDetails.prezimeg = "";
      this.formDetails.serijskibrojg = "";
      this.formDetails.vrstaplovilag = "";
    },
    showMessage(isError, message) {
      if (isError) {
        this.$toasted.error(message, { duration: 2000 });
      } else {
        this.$toasted.success(message, { duration: 2000 });
      }
    },
    updateForm(args) {
      let form = document.getElementById("mainForm");
      if (!form.checkValidity()) {
        args.srcElement.click();
        return;
      }
      args.preventDefault();
      this.isLoading = true;
      axios
        .post("/api/PrijavagoForm4", this.formDetails)
        .then(res => {
          console.log(res.data);
          this.isLoading = false;
          if (res.data.error != "") {
            // show error
            this.showMessage(true, res.data.error);
            return;
          }
          this.reset();
          this.showMessage(false, "Form details updated successfully.");
          this.getRandomNumber();
        })
        .catch(err => {
          this.isLoading = false;
          console.log(err);
          this.showMessage(true, err);
        });
    },
    deleteForm(args) {
      this.isLoading = true;
      this.isDeleting = true;
      this.formDetails.actiontotake = "Delete";
      axios
        .post("/api/PrijavagoForm4", this.formDetails)
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
          this.showMessage(false, "Form details deleted successfully.");
          this.getRandomNumber();
        })
        .catch(err => {
          console.log(err);
          this.showMessage(true, err);
          this.isLoading = false;
          this.isDeleting = false;
        });
    },
    getRandomNumber() {
      this.isLoading = true;
      axios
        .get("/api/GetUUID")
        .then(res => {
          console.log(res.data);
          this.isLoading = false;
          this.formDetails.serijskibrojg = res.data.uuid;
        })
        .catch(err => {
          console.log(err);
          this.isLoading = false;
          showMessage(true, err);
        });
    }
  }
};
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter,
.fade-leave-to {
  opacity: 0;
}
</style>
