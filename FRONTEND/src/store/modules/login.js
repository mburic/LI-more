import router from '../../router'
export const state = {
  token: null,
  userDetails: null,
  isAdmin: false,
  editFormName: null,
  editFormData: null
}

export const getters = {
  token: state => state.token,
  userDetails: state => state.userDetails,
  isAdmin: state => state.isAdmin,
  editFormName: state => state.editFormName,
  editFormData: state => state.editFormData
}

export const mutations = {
  token: (state, token) => {
    state.token = token
  },
  userDetails: (state, userDetails) => {
    state.userDetails = userDetails
  },
  isAdmin: (state, isAdmin) => {
    state.isAdmin = isAdmin
  },
  editFormName: (state, editFormName) => {
    state.editFormName = editFormName
  },
  editFormData: (state, editFormData) => {
    state.editFormData = editFormData
  }
}

export const actions = {
  login: ({
    commit
  }, payload) => {
    return new Promise((resolve) => {
      console.log('login-store',payload)
      commit('token', payload.token)
      commit('userDetails', payload.userDetails)
      commit('isAdmin', payload.userDetails.isadmin)
      // sessionStorage.setItem('user-token', 'token')
      // navigate to dashboard
      if (payload.userDetails.isadmin) {
        router.push('/registration')
      } else {
        router.push('/')
      }
      resolve(true)
    })
  },
  logout: ({
    commit
  }) => {
    return new Promise((resolve) => {
      commit('token', null)
      commit('userDetails', null)
      commit('isAdmin', false)
      // sessionStorage.setItem('user-token', 'token')
      // navigate to dashboard
      router.push('/login')
      resolve(true)
    })
  }
}

/* export default {
  state,
  getters,
  mutations,
  actions
} */
