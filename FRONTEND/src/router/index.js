import Vue from 'vue'
import Router from 'vue-router'

// Containers
const DefaultContainer = () => import('@/containers/DefaultContainer')

// Views - Pages
const Page404 = () => import('@/views/pages/Page404')
const Page500 = () => import('@/views/pages/Page500')
const Login = () => import('@/views/pages/Login')
const Register = () => import('@/views/pages/Register')


// Main-Pages
const Form1 = () => import('@/views/main/Form1')
const Form2 = () => import('@/views/main/Form2')
const Form3 = () => import('@/views/main/Form3')
const Form4 = () => import('@/views/main/Form4')
const GetData12 = () => import('@/views/main/GetData12')
const GetData34 = () => import('@/views/main/GetData34')
const GetData3 = () => import('@/views/main/GetData3')
const MainPage = () => import('@/views/main/MainPage')
const Registration = () => import('@/views/main/Registration')

Vue.use(Router)

export default new Router({
  mode: 'hash', // https://router.vuejs.org/api/#mode
  linkActiveClass: 'open active',
  scrollBehavior: () => ({
    y: 0
  }),
  routes: [{
      path: '/',
      redirect: '/dashboard',
      name: 'Home',
      component: DefaultContainer,
      children: [{
        path: 'dashboard',
        name: 'MainPage',
        component: MainPage
      }, {
        path: '/form1',
        name: 'Form1',
        component: Form1,
      }, {
        path: '/form2',
        name: 'Form2',
        component: Form2,
      }, {
        path: '/form3',
        name: 'Form3',
        component: Form3,
      }, {
        path: '/form4',
        name: 'Form4',
        component: Form4,
      },
      {
        path: '/getdata12',
        name: 'GetData12',
        component: GetData12,
      }, {
        path: '/getdata34',
        name: 'GetData34',
        component: GetData34,
      },  {
        path: '/getdata3',
        name: 'GetData3',
        component: GetData3,
      }, 
      // {
      //   path: '/mainpage',
      //   name: 'MainPage',
      //   component: MainPage,
      // }, 
      {
        path: '/registration',
        name: 'Registration',
        component: Registration,
      }]
    },
    {
      path: '/login',
      name: 'Login',
      component: Login,
    },
    {
      path: '/pages',
      redirect: '/pages/404',
      name: 'Pages',
      component: {
        render(c) {
          return c('router-view')
        }
      },
      children: [{
          path: '404',
          name: 'Page404',
          component: Page404
        },
        {
          path: '500',
          name: 'Page500',
          component: Page500
        },
        {
          path: 'register',
          name: 'Register',
          component: Register
        }
      ]
    }
  ]
})
