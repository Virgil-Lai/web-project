// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store'
import VueAntd from 'vue-antd-ui'
import VueLazyload from 'vue-lazyload'
import './assets/css/reset.css'
import './assets/css/animated.css'
import 'vue-antd-ui/dist/antd.css'
// import './common/js/rem'

Vue.config.productionTip = false

Vue.use(VueAntd)
Vue.use(VueLazyload, {
  loading: './assets/images/loading/loading-bars.svg',
  attempt: 1
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
// router.beforeEach((to, from, next) => {
//   if (to.meta.title) {
//     document.title = to.meta.title
//   }
//     if (to.meta.title === 'detail') {
//       if(!isLogin){
//         alert("here")
//         next('/user-center')
//       }
//       else{
//         alert("here2")
//         next()
//       }
//     } else {
//       alert("here1")
//       next()
//     }
// })

router.beforeEach(function (to,form,next){
  if(to.meta.needLogin){
    if(localStorage.getItem("login_token")){
      next();
    }
    else {
      next({
        name:'UserCenter'
      });
    }
  }
  else
    next();
})
