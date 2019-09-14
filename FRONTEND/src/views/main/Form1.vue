<template>
  <div class="animated fadeIn">
    <b-row>
      <b-col lg="12">
        <b-card>
          <div slot="header">
            <strong>{{isInEditMode?"EDIT":"DOLAZAK"}}</strong>
          </div>
          <b-form id="mainForm">
            <b-form-group description label="ISPOSTAVA" label-for="basicName" :label-cols="3">
              <label style="background-color:#fff6ae; border-radius: 25px; border: 2px solid #0088cc; padding: 5px;">{{this.$store.getters.userDetails.ispostava}}</label>
            </b-form-group>
            <b-form-group label="DATUM POLASKA" label-for="date" :label-cols="3">
              <b-form-input required v-model="formDetails.date_pd" name="datum" type="date" id="date" style="background-color:#fff6ae;"></b-form-input>
            </b-form-group>
            <b-form-group description label="OZNAKA PLOVILA" label-for="basicText" :label-cols="3">
              <b-form-input
                style="background-color:#fff6ae;"
                required
                v-model="formDetails.oznaka_pd"
                id="basicText"
                type="text"
                placeholder
              ></b-form-input>
            </b-form-group>
            <b-form-group description label="DUZINA PLOVILA" label-for="basicText" :label-cols="3">
              <b-form-input
                style="background-color:#fff6ae;"
                required
                v-model="formDetails.duzina_pd"
                id="basicText"
                type="text"
                placeholder
              ></b-form-input>
            </b-form-group>
            <b-form-group description label="VRSTA PLOVILA" label-for="basicText" :label-cols="3">
              <b-form-select
                style="background-color:#fff6ae;"
                required
                v-model="formDetails.vrstaplovila_pd"
                id="basicText"
                type="text"
                :plain="true"
                :options="['BRODICA', 'JEDRILICA', 'MOTORNA']"
                placeholder
              ></b-form-select>
            </b-form-group>
            <b-form-group description label="KONTAKT" label-for="basicText" :label-cols="3">
              <b-form-input
                style="background-color:#fff6ae;"
                required
                v-model="formDetails.kontakt_pd"
                id="basicText"
                type="text"
                placeholder
              ></b-form-input>
            </b-form-group>
            <hr />
            <b-form-group
              description
              label="LUKA IZ KOJE DOLAZI"
              label-for="basicText"
              :label-cols="3"
            >
              <b-form-select
                style="background-color:#fff6ae;"
                required
                v-model="formDetails.lukad"
                id="basicText"
                type="text"
                :plain="true"
                :options="['Ancona (IT)', 'Bar (ME)', 'Bari (IT)', 'Budva (ME)', 'Durrës (AL)', 'Koper (SL)', 'Pescara (IT)', 'Ploče (HR)', 'Rijeka (HR)', 'Split (HR)', 'Trst (IT)', 'Venecija (IT)']"
                placeholder
              ></b-form-select>
            </b-form-group>
            <b-form-group
              description
              label="IME ZAPOVJEDNIKA"
              label-for="basicText"
              :label-cols="3"
            >
              <b-form-input
                style="background-color:#fff6ae;"
                required
                v-model="formDetails.ime_pd"
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
                v-model="formDetails.prezime_pd"
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
                v-model="formDetails.brojclanova_pd"
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
                style="margin-right:20px;"
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
                style="margin-right:20px;"
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
                style="margin-right:20px;"
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
                style="margin-right:20px;"
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
        brojclanova_pd: "",
        date_pd: "",
        duzina_pd: "",
        ime_pd: "",
        ispostava_pd: this.$store.getters.userDetails.ispostava,
        kontakt_pd: "",
        lukad: "",
        oznaka_pd: "",
        prezime_pd: "",
        username: this.$store.getters.userDetails.username,
        vrstaplovila_pd: ""
      }
    };
  },
  mounted() {
    if (this.$store.getters.editFormName == "/form1") {
      this.isInEditMode = true;
      this.formDetails = JSON.parse(
        JSON.stringify(this.$store.getters.editFormData)
      );
      this.formDetails.actiontotake = "Update";
      this.formDetails.ispostava_pd = this.$store.getters.userDetails.ispostava;
      this.formDetails.username = this.$store.getters.userDetails.username;
      this.$store.commit("editFormName", null);
      this.$store.commit("editFormData", null);
    }
  },
  methods: {
    saveForm(args) {
      let form = document.getElementById("mainForm");
      if (!form.checkValidity()) {
        args.srcElement.click();
        return;
      }
      args.preventDefault();
      this.isLoading = true;
      axios
        .post("/api/PrijavadForm1", this.formDetails) //
        .then(res => {
          console.log(res.data);
          this.isLoading = false;
          if (res.data.error != "") {
            // show error
            this.showMessage(true, res.data.error);
            return;
          }
          this.reset();
          this.showMessage(false, "Uspješno spremljeno");
        })
        .catch(err => {
          this.isLoading = false;
          console.log(err);
          this.showMessage(true, err);
        });
    },
    reset() {
      this.isInEditMode = false;
      this.$store.commit("editFormName", null);
      this.$store.commit("editFormData", null);
      this.formDetails.brojclanova_pd = "";
      this.formDetails.date_pd = "";
      this.formDetails.duzina_pd = "";
      this.formDetails.ime_pd = "";
      this.formDetails.kontakt_pd ="";
      this.formDetails.lukad = "";
      this.formDetails.oznaka_pd = "";
      this.formDetails.prezime_pd = "";
      this.formDetails.vrstaplovila_pd = "";
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
        .post("/api/PrijavadForm1", this.formDetails)
        .then(res => {
          console.log(res.data);
          this.isLoading = false;
          if (res.data.error != "") {
            // show error
            this.showMessage(true, res.data.error);
            return;
          }
          this.reset();
          this.showMessage(false, "Uspješno ažurirano");
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
        .post("/api/PrijavadForm1", this.formDetails)
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
          this.showMessage(false, "Uspješno obrisano");
        })
        .catch(err => {
          console.log(err);
          this.showMessage(true, err);
          this.isLoading = false;
          this.isDeleting = false;
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
