<template>
  <b-card>
    <div slot="header" v-html="caption"></div>
    <b-table
      :dark="dark"
      :hover="hover"
      :striped="striped"
      :bordered="bordered"
      :small="small"
      :fixed="fixed"
      responsive="sm"
      :items="items"
      :fields="captions"
      :current-page="currentPage"
      :per-page="perPage"
    >
      <template slot="manage" slot-scope="data">
        <span v-if="isAllowed(data.item)" class="ic-manage" @click="rowClicked(data.item)">
          <i class="fa fa-edit"></i>
        </span>
      </template>
    </b-table>
    <nav>
      <b-pagination
        :total-rows="totalRows"
        :per-page="perPage"
        v-model="currentPage"
        prev-text="Prev"
        next-text="Next"
        hide-goto-end-buttons
      />
    </nav>
  </b-card>
</template>

<script>
export default {
  name: "c-table",
  inheritAttrs: false,
  props: {
    navigateto: {
      type: String,
      default: null
    },
    caption: {
      type: String,
      default: "Table"
    },
    hover: {
      type: Boolean,
      default: false
    },
    striped: {
      type: Boolean,
      default: false
    },
    bordered: {
      type: Boolean,
      default: false
    },
    small: {
      type: Boolean,
      default: false
    },
    fixed: {
      type: Boolean,
      default: false
    },
    tableData: {
      type: [Array, Function],
      default: () => []
    },
    fields: {
      type: [Array, Object],
      default: () => []
    },
    perPage: {
      type: Number,
      default: 5
    },
    dark: {
      type: Boolean,
      default: false
    }
  },
  data: () => {
    return {
      currentPage: 1
    };
  },
  computed: {
    items: function() {
      const items = this.tableData;
      return Array.isArray(items) ? items : items();
    },
    totalRows: function() {
      return this.getRowCount();
    },
    captions: function() {
      return this.fields;
    }
  },
  methods: {
    getBadge(status) {
      return status === "Active"
        ? "success"
        : status === "Inactive"
        ? "secondary"
        : status === "Pending"
        ? "warning"
        : status === "Banned"
        ? "danger"
        : "primary";
    },
    getRowCount: function() {
      return this.items.length;
    },
    isAllowed(item) {
      let keyList = Object.keys(item);
      for (let index = 0; index < keyList.length; index++) {
        const key = keyList[index];
        if (key.startsWith("username")) {
          console.log(item[key], this.$store.getters.userDetails.username);
          return item[key] == this.$store.getters.userDetails.username;
        }
      }
      return true;
    },
    rowClicked(item) {
      if (this.navigateto == null || this.navigateto == undefined) {
        return;
      }
      this.$store.commit("editFormName", this.navigateto);
      this.$store.commit("editFormData", JSON.parse(JSON.stringify(item)));
      this.$router.push(this.navigateto);
    }
  }
};
</script>
<style>
.ic-manage {
  padding: 5px 10px;
  cursor: pointer;
}
.ic-manage:hover {
  background-color: #e4e5e6;
  border-radius: 2px;
}
</style>
