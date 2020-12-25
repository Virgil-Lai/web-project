import Vue from 'vue'
import Router from 'vue-router'
Vue.use(Router)

export default new Router({
  mode: 'history',
  scrollBehavior(to, from, savedPosition) {
    return { x: 0, y: 0 }
  },
  routes: [
    {
      path: '/',
      name: 'Home',
      component: () => import('../pages/home/Home.vue'),
      meta: {
        title: 'home'
      }
    },
    {
      path: '/theater',
      name: 'MovieInTheater',
      component: () => import('../pages/in-theater/MovieInTheater.vue'),
      meta: {
        title: 'theater'
      }
    },
    {
      path: '/coming',
      name: 'ComingMovies',
      component: () => import('../pages/coming-movies/ComingMovies.vue'),
      meta: {
        title: 'coming'
      }
    },
    {
      path: '/movies-info',
      name: 'MoviesInfo',
      component: () => import('../pages/movies-info/MoviesInfo.vue'),
      meta: {
        title: 'info'
      }
    },
    {
      path: '/rank',
      name: 'RankPage',
      component: () => import('../pages/rank-page/RankPage.vue'),
      meta: {
        title: 'rank'
      }
    },
    {
      path: '/category',
      name: 'CategoryPage',
      component: () => import('../pages/category-page/CategoryPage.vue'),
      meta: {
        title: 'category'
      }
    },
    {
      path: '/subject/:id',
      name: 'MovieDetail',
      component: () => import('../pages/movie-detail/MovieDetail.vue'),
      meta: {
        title: 'detail',
        needLogin:true
      }

    },
    {
      path: '/top250',
      name: 'Top250',
      component: () => import('../pages/top-250/Top250.vue')
    },
    {
      path: '/subject/comments/:id',
      name: 'CommentsPage',
      component: () => import('../pages/comments-page/CommentsPage.vue')
    },
    {
      path: '/search-movie',
      name: 'SearchPage',
      component: () => import('../pages/search-page/SearchPage.vue')
    },
    {
      path: '/user-center',
      name: 'UserCenter',
      component: () => import('../pages/user-center/UserCenter.vue'),
      meta: {
        title: 'login'
      }
    },
    {
      path: '/about',
      name: 'RankPage',
      component: () => import('../pages/about/about.vue')
    }
  ]
})
