<template>
  <div class="app">
    <AppHeader fixed style="background-color:#f4ffdf;">
      <span v-if="!$store.getters.isAdmin">
        <SidebarToggler class="d-lg-none" display="md" mobile />
      </span>
      <b-link class="navbar-brand" to="/">
        <img
          class="navbar-brand-full"
          src="/img/brand/l2.png"
          width="75"
          height="50"
          alt="LI more"
        />
        <img
          class="navbar-brand-minimized"
          src="/img/brand/l2.png"
          width="30"
          height="30"
          alt="LI more"
        />
      </b-link>
      <span v-if="!$store.getters.isAdmin">
        <SidebarToggler v-show="false" class="d-md-down-none" display="lg" :defaultOpen="true" />
      </span>
      <span v-if="$store.getters.isAdmin">
        <SidebarToggler v-show="false" class="d-md-down-none" display="lg" :defaultOpen="false" />
      </span>

      <!-- <b-navbar-nav class="d-md-down-none">
        <b-nav-item class="px-3" to="/dashboard">Dashboard</b-nav-item>
        <b-nav-item class="px-3" to="/users" exact>Users</b-nav-item>
        <b-nav-item class="px-3">Settings</b-nav-item>
      </b-navbar-nav>-->
      <b-navbar-nav class="ml-auto">
        <!-- <b-nav-item class="d-md-down-none">
          <i class="icon-bell"></i>
          <b-badge pill variant="danger">5</b-badge>
        </b-nav-item>-->
        <!-- <b-nav-item class="d-md-down-none">
          <i class="icon-list"></i>
        </b-nav-item>
        <b-nav-item class="d-md-down-none">
          <i class="icon-location-pin"></i>
        </b-nav-item>-->
        <DefaultHeaderDropdownAccnt />
      </b-navbar-nav>
      <!-- <AsideToggler class="d-none d-lg-block" /> -->
      <!--<AsideToggler class="d-lg-none" mobile />-->
    </AppHeader>
    <div class="app-body">
      <AppSidebar fixed>
        <SidebarHeader />
        <SidebarForm />
        <SidebarNav :navItems="nav"></SidebarNav>
        <SidebarFooter />
        <!-- <SidebarMinimizer/> -->
      </AppSidebar>
      <main class="main">
        <div>
          <div class="row" style="height:50px;background-color:white;margin-bottom:25px">
            <div class="col-sm-4"></div>
            <div class="col-sm-4"></div>
            <div class="col-sm-4">
              <b-input-group style="margin:7px 0px;">
                <b-input-group-prepend>
                  <b-input-group-text>
                    <i class="fa fa-search"></i>
                  </b-input-group-text>
                </b-input-group-prepend>
                <b-form-input id="searchbar" v-on:keyup="search" v-model="searchbar" type="text" placeholder="Pretraži..." style="background-color:#ffdeb2;"></b-form-input>
              </b-input-group>
            </div>
          </div>
          <!-- <Breadcrumb :list="list"/> -->
        </div>
        <div class="container-fluid">
          <router-view></router-view>
        </div>
      </main>
      <AppAside fixed>
        <!--aside-->
        <DefaultAside />
      </AppAside>
    </div>
    <!-- <TheFooter>
      <div>
      </div>
      <div class="ml-auto">
      </div>
    </TheFooter>-->
  </div>
</template>

<script>
import nav from "@/_nav";
import {
  Header as AppHeader,
  SidebarToggler,
  Sidebar as AppSidebar,
  SidebarFooter,
  SidebarForm,
  SidebarHeader,
  SidebarMinimizer,
  SidebarNav,
  Aside as AppAside,
  AsideToggler,
  Footer as TheFooter,
  Breadcrumb
} from "@coreui/vue";
import DefaultAside from "./DefaultAside";
import DefaultHeaderDropdownAccnt from "./DefaultHeaderDropdownAccnt";

export default {
  name: "DefaultContainer",
  components: {
    AsideToggler,
    AppHeader,
    AppSidebar,
    AppAside,
    TheFooter,
    Breadcrumb,
    DefaultAside,
    DefaultHeaderDropdownAccnt,
    SidebarForm,
    SidebarFooter,
    SidebarToggler,
    SidebarHeader,
    SidebarNav,
    SidebarMinimizer
  },
  data() {
    return {
      searchbar: '',
      nav: nav.items
    };
  },
  watch:{
    $route(to, from) {
        this.searchbar = '';
    }
  },
  computed: {
    name() {
      return this.$route.name;
    },
    list() {
      return this.$route.matched.filter(
        route => route.name || route.meta.label
      );
    }
  },
  methods: {
    search() {
        this.$root.$emit('search', this.searchbar);
    }
  }
};
</script>
<style>
</style>