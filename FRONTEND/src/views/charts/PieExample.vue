<script>
import { Pie } from 'vue-chartjs'
import axios from "axios";

export default {
  extends: Pie,
  mounted () {
    axios
        .get("/api/GetCount", {
        })
        .then(res => {
          console.log(res.data[0])
             this.renderChart({
              labels: ['DOMAĆI', 'GOST'],
              datasets: [
              {
          backgroundColor: [
            '#66ccff',
            '#ccff66'
          ],
          data: [res.data.data[0].t1, res.data.data[0].t2]
        }
      ]
    }, {responsive: true, maintainAspectRatio: true})
          console.log(res.data);
        })
        .catch(err => {
          console.log(err);
          this.$toasted.error(err, { duration: 2000 });
        });
  }
}
</script>
