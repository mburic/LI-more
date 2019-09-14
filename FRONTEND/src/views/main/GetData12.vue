<template>
  <div class="animated fadeIn">
    <b-row>
      <b-col lg="12">
        <h2>
          <center>PREGLED DOLAZAKA I POLAZAKA</center>
        </h2>
        <hr />
      </b-col>
    </b-row>

    <b-row>
      <b-col lg="12">
        <c-table
          navigateto="/form1"
          :table-data="form1Data"
          :fields="form1Fields"
          caption="<!--<i class='fa fa-align-justify'></i>--> DOLASCI"
        ></c-table>
      </b-col>
    </b-row>

    <b-row>
      <b-col lg="12">
        <c-table
          navigateto="/form2"
          :table-data="form2Data"
          :fields="form2Fields"
          caption="<!--<i class='fa fa-align-justify'></i>--> POLASCI"
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
      tmpData1: '',
      tmpData2: '',
    // fields: [
      //   { key: "username", label: "User", sortable: true },
      //   { key: "registered" },
      //   { key: "role" },
      //   { key: "status", sortable: true }
      // ],
      form1Fields: [
        { key: "date_pd", label: "DATUM DOLASKA", sortable: true },
        { key: "oznaka_pd", label: "OZNAKA PLOVILA" },
        { key: "duzina_pd", label: "DUZINA PLOVILA", sortable: true },
        { key: "vrstaplovila_pd", label: "VRSTA PLOVILA", sortable: true },
        { key: "kontakt_pd", label: "KONTAKT" },
        { key: "lukad", label: "LUKA DOLASKA", sortable: true },
        { key: "ime_pd", label: "IME VLASNIKA" },
        { key: "prezime_pd", label: "PREZIME VLASNIKA",sortable: true },
        { key: "manage", label: "" }
      ],
      form1Data: [],
      form2Fields: [
        { key: "date_po", label: "DATUM POLASKA", sortable: true },
        { key: "oznaka_po", label: "OZNAKA PLOVILA" },
        { key: "duzina_po", label: "DUZINA PLOVILA", sortable: true },
        { key: "vrstaplovila_po", label: "VRSTA PLOVILA", sortable: true },
        { key: "kontakt_po", label: "KONTAKT" },
        { key: "lukao", label: "LUKA ODLASKA", sortable: true },
        { key: "ime_po", label: "IME VLASNIKA" },
        { key: "prezime_po", label: "PREZIME VLASNIKA",sortable: true },
        { key: "manage", label: "" }
      ],
      form2Data: []
    };
  },
  mounted() {
    this.fetchForm1();
    this.fetchForm2();

    this.$root.$on('search', (text) => {
      this.onSearch(text);
    })
  },
  beforeDestroy () {
    this.$root.$off('search');
  },
  methods: {
    onSearch(text) {
      this.form1Data = this.tmpData1.filter(function (el) {
        if (text == null) return true;
        if (text.length < 1) return true;
        
        for (var key in el) {
          if (el[key] == null) continue;
          if (el[key].length < 1) continue;

          if (String(el[key]).toLowerCase().includes(text.toLowerCase())) return 1;
        }

        return 0;
      });

      this.form2Data = this.tmpData2.filter(function (el) {
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
    fetchForm1() {
      axios
        .post("/api/PrijavadForm1", {
          actiontotake: "Get",
          username: this.$store.getters.userDetails.username
        })
        .then(res => {
          this.tmpData1 = res.data.data;

          if (res.data.error == "") {
            this.form1Data = res.data.data;
          } else {
            this.$toasted.error(res.data.error, { duration: 2000 });
          }
        })
        .catch(err => {
          console.log(err);
          this.$toasted.error(err, { duration: 2000 });
        });
    },
    fetchForm2() {
      axios
        .post("/api/PrijavaodForm2", {
          actiontotake: "Get",
          username: this.$store.getters.userDetails.username
        })
        .then(res => {
          this.tmpData2 = res.data.data;

          if (res.data.error == "") {
             this.form2Data = res.data.data; 
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
