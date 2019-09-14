<template>
  <div class="animated fadeIn">
    <b-row>
      <b-col lg="12">
        <b-card>
          <!-- <div slot="header">
            <strong>ADD</strong> FORM3
          </div>-->
          <b-row>
            <b-col lg="3">
              <a href="#/form1">DOLAZAK</a>
            </b-col>
            <b-col lg="3">
              <a href="#/form2">POLAZAK</a>
            </b-col>
            <b-col lg="3">
              <a href="#/form3">DOMAĆI</a>
            </b-col>
            <b-col lg="3">
              <a href="#/form4">GOST</a>
            </b-col>
          </b-row>
          <br>
          <br>
          <br>
          <br>
          <b-row>
            <b-col>
              <h5>
                <center>DOMAĆI I GOST</center>
              </h5>
            </b-col>
          </b-row>
          <b-row>
            <b-col lg="4"></b-col>
            <div class="chart-wrapper col-sm-4">
              <pie-example chartId="chart-pie-01"/>
            </div>
            <b-col lg="4"></b-col>
          </b-row>
        </b-card>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import PieExample from "../charts/PieExample";
export default {
  name: "forms",
  components: {
    PieExample
  },
  data() {
    return {
      selected: [], // Must be an array reference!
      show: true
    };
  },
  methods: {
    click() {
      // do nothing
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
