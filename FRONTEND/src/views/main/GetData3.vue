<template>
  <div class="animated fadeIn">
    <b-row>
      <b-col lg="12">
        <h2>
          <center>GET DATA 3</center>
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
          caption="<!--<i class='fa fa-align-justify'></i>--> DATA 3"
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
      // fields: [
      //   { key: "username", label: "User", sortable: true },
      //   { key: "registered" },
      //   { key: "role" },
      //   { key: "status", sortable: true }
      // ],
      form3Fields: [
        { key: "serijskibrojd", label: "SERIJSKI BROJ PRIJAVE" },
        { key: "datum_do", label: "DATE FROM" },
        { key: "datum_do", label: "DATE TO" },
        { key: "nacindolaskad", label: "NACIN DOLASKA" },
        { key: "manage", label: "" }
      ],
      form3Data: []
    };
  },
  mounted() {
    this.fetchForm3();
  },
  methods: {
    fetchForm3() {
      axios
        .post("/api/PrijavadoForm3", {
          actiontotake: "Get",
          username: this.$store.getters.userDetails.username
        })
        .then(res => {
          console.log(res.data);
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
    }
  }
};
</script>
