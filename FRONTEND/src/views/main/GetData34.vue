<template>
  <div class="animated fadeIn">
    <b-row>
      <b-col lg="12">
        <h2>
          <center>PREGLED DOMAĆINA I GOSTIJU</center>
        </h2>
        <hr />
      </b-col>
    </b-row>

    <b-row>
      <b-col lg="12">
        <c-table
          navigateto="/form3"
          :table-data="form3Data"
          :fields="form3Fields"
          caption="<!--<i class='fa fa-align-justify'></i>--> <b>DOMAĆI</b>  "
        ></c-table>
      </b-col>
    </b-row>

    <b-row>
      <b-col lg="12">
        <c-table
          navigateto="/form4"
          :table-data="form4Data"
          :fields="form4Fields"
          caption="<!--<i class='fa fa-align-justify'></i>--> <b>GOSTI<b>"
        ></c-table>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import axios from "axios";
import { shuffleArray } from "@/shared/utils";
import cTable from "./Table.vue";

export default {
  name: "tables",
  components: { cTable },
  data: () => {
    return {
      tmpData3: '',
      tmpData4: '',
      // fields: [
      //   { key: "username", label: "User", sortable: true },
      //   { key: "registered" },
      //   { key: "role" },
      //   { key: "status", sortable: true }
      // ],
      form3Fields: [
        { key: "datum_od", label: "DATUM OD" },
        { key: "datum_do", label: "DATUM DO" },
        { key: "nacindolaskad", label: "NAČIN DOLASKA" },
        { key: "imeplovilad", label: "IME PLOVILA", sortable: true },
        { key: "vrstaplovilad", label: "VRSTA PLOVILA" },
        { key: "oznakad", label: "OZNAKA", sortable: true },
        { key: "duljinad", label: "DULJINA" },
        { key: "brojclanovad", label: "BROJ ČLANOVA" },
        { key: "imed", label: "IME VLASNIKA" },
        { key: "prezimed", label: "PREZIME VLASNIKA", sortable: true },
        { key: "kontaktd", label: "KONTAKT" },
        { key: "obracund", label: "OBRAČUN" },
        { key: "manage", label: "" }
      ],
      form3Data: [],
      form4Fields: [
        { key: "datumg_od", label: "DATUM OD" },
        { key: "datumg_do", label: "DATUM DO" },
        { key: "nacindolaskag", label: "NAČIN DOLASKA" },
        { key: "imeplovilag", label: "IME PLOVILA", sortable: true },
        { key: "vrstaplovilag", label: "VRSTA PLOVILA" },
        { key: "oznakag", label: "OZNAKA", sortable: true },
        { key: "duljinag", label: "DULJINA" },
        { key: "brojclanovag", label: "BROJ ČLANOVA" },
        { key: "imeg", label: "IME VLASNIKA" },
        { key: "prezimeg", label: "PREZIME VLASNIKA", sortable: true },
        { key: "kontaktg", label: "KONTAKT" },
        { key: "obracung", label: "OBRAČUN" },
        { key: "manage", label: "" }
      ],
      form4Data: []
    };
  },
  mounted() {
    this.fetchForm3();
    this.fetchForm4();

    this.$root.$on('search', (text) => {
      this.onSearch(text);
    })
 },
  created() {
  },
  beforeDestroy () {
    this.$root.$off('search');
  },
  methods: {
    onSearch(text) {
      this.form3Data = this.tmpData3.filter(function (el) {
        if (text == null) return true;
        if (text.length < 1) return true;
        
        for (var key in el) {
          if (el[key] == null) continue;
          if (el[key].length < 1) continue;

          if (String(el[key]).toLowerCase().includes(text.toLowerCase())) return 1;
        }

        return 0;
      });

      this.form4Data = this.tmpData4.filter(function (el) {
        if (text == null) return true;
        if (text.length < 1) return true;
        
        for (var key in el) {
          if (el[key] == null) continue;
          if (el[key].length < 1) continue;

          if (String(el[key]).toLowerCase().includes(text.toLowerCase())) return 1;
        }

        return 0;
      });
    },
    fetchForm3() {
      axios
        .post("/api/PrijavadoForm3", {
          actiontotake: "Get",
          username: this.$store.getters.userDetails.username
        })
        .then(res => {
          this.tmpData3 = res.data.data;

          if (res.data.error == "") {
            this.form3Data = res.data.data;
          } else {
            this.$toasted.error(res.data.error, { duration: 2000 });
          }
        })
        .catch(err => {
          console.log(err);
          this.$toasted.error(err, { duration: 2000 });
        });
    },
    fetchForm4() {
      axios
        .post("/api/PrijavagoForm4", {
          actiontotake: "Get",
          username: this.$store.getters.userDetails.username
        })
        .then(res => {
          this.tmpData4 = res.data.data;

          if (res.data.error == "") {
            this.form4Data = res.data.data;
          } else {
            this.$toasted.error(res.data.error, { duration: 2000 });
          }
        })
        .catch(err => {
          console.log(err);
          this.$toasted.error(err, { duration: 2000 });
        });
    }
  }
};
</script>
