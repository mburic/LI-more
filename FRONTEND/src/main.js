// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import 'core-js/es6/promise'
import 'core-js/es6/string'
import 'core-js/es7/array'
// import cssVars from 'css-vars-ponyfill'
import Vue from 'vue'
import BootstrapVue from 'bootstrap-vue'
import App from './App'
import router from './router'
import store from './store'
import Toasted from 'vue-toasted';
// import axios from "axios";

// set base url here
// axios.defaults.baseURL = ''

// todo
// cssVars()

Vue.use(Toasted)

Vue.use(BootstrapVue)

router.beforeEach((to, from, next) => {
  // console.log(to.name);
  if (to.name == "Login") {
    next(true)
    return;
  }
  if (store.getters.userDetails == null) {
    console.log('no session found')
    next("/login");
    return;
  }
  // if (to.name == "Registration") {
  //   if (!store.getters.isAdmin) {
  //     console.log('user is not admin')
  //     // next("/dashboard");
  //     next("/dashboard");
  //     return
  //   }
  //   next(true)
  //   return;
  // }

  if (store.getters.isAdmin) {
    console.log('user is not admin')

    if (to.name == "Registration") {
      next(true)
      return
    }
    // next("/dashboard");
    next("/registration");
    return
  } else {
    if (to.name == "Registration") {
      next("/dashboard");
      return
    }
  }
  next(true)
})

/* eslint-disable no-new */
var vm = new Vue({
  el: '#app',
  router,
  store,
  template: '<App/>',
  components: {
    App
  }
})

window.app = vm
