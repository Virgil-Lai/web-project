<template>
  <div class="rank-page">
    <a-row>
      <a-col :span="2"></a-col>
      <a-col :span="13">
        <div class="title">
          <h1>豆瓣电影排行榜</h1>
          <h2>豆瓣新片榜</h2>
        </div>
        <loading v-if="!newMovies.length"></loading>
        <new-rank v-else :movies="newMovies"></new-rank>
<!--        <div class="load-more" @click="_getMoviesByTag">点击加载更多</div>-->
      </a-col>
      <a-col :span="1"></a-col>
<!--      <a-col :span="6">-->
<!--        <loading v-if="!weeklyMovies.length"></loading>-->
<!--        <movie-rank title="本周口碑榜" :movies="weeklyMovies"></movie-rank>-->
<!--        <loading v-if="!usMovies.length"></loading>-->
<!--        <movie-rank v-else title="北美票房榜" :movies="usMovies" :toggle="false"></movie-rank>-->
<!--        <loading v-if="!topMovies.length"></loading>-->
<!--        <top-movie v-else :movies="topMovies"></top-movie>-->
<!--      </a-col>-->
<!--      <a-col :span="2"></a-col>-->
    </a-row>
  </div>
</template>

<script>
  import MovieRank from './components/MovieRank.vue'
  import NewRank from './components/NewRank.vue'
  import TopMovie from './components/TopMovie.vue'
  import Loading from '../../components/loading/Loading.vue'
  import { getMoviesByUrl } from '../../apis/request'
  import { API_WEEKLY, API_US_BOX, API_NEW_MOVIES, API_TOP_250 } from '../../apis/urls'

  export default {
    name: 'RankPage',
    components: {
      MovieRank,
      NewRank,
      TopMovie,
      Loading
    },
    data() {
      return {
        weeklyMovies: [],
        usMovies: [],
        newMovies: [],
        topMovies: []
      }
    },
    mounted () {
      //监听鼠标滚动事件
      // window.addEventListener('mousewheel', this.handleScroll())

    },
    created() {
      let _this = this;
      window.onscroll = function(){
        //变量scrollTop是滚动条滚动时，距离顶部的距离
        var scrollTop = document.documentElement.scrollTop||document.body.scrollTop;
        //变量windowHeight是可视区的高度
        var windowHeight = document.documentElement.clientHeight || document.body.clientHeight;
        //变量scrollHeight是滚动条的总高度
        var scrollHeight = document.documentElement.scrollHeight||document.body.scrollHeight;
        //滚动条到底部的条件
        if(scrollTop+windowHeight == scrollHeight){
          getMoviesByUrl(API_WEEKLY).then(res => {
            res = res.data
            _this.newMovies.push(...res.subjects)
          }).catch(err => {
            _this.$message.error('获取数据失败')
          })
        }
      }
      getMoviesByUrl(API_WEEKLY).then(res => {
        res = res.data
        this.weeklyMovies = res.subjects
      }).catch(err => {
        this.$message.error('获取本周口碑数据发生错误')
      })
      getMoviesByUrl(API_US_BOX).then(res => {
        res = res.data
        this.usMovies = res.subjects
      }).catch(err => {
        this.$message.error('获取北美票房数据发生错误')
      })
      getMoviesByUrl(API_NEW_MOVIES).then(res => {
        res = res.data
        this.newMovies = res.subjects
      }).catch(err => {
        this.$message.error('获取新片榜数据发生错误')
      })
      getMoviesByUrl(API_TOP_250).then(res => {
        res = res.data
        this.topMovies = res.subjects
      }).catch(err => {
        console.log('top250', err)
      })
    },
    methods:{
      // handleScroll(e){
      //   this.loadMore()
      // },
      loadMore() {
        // this.start = 0
        this._getMoviesByTag()
      },
      _getMoviesByTag() {
        // alert("hhhhhhhh")
        // let url='http://localhost:5000/getMovieJsonByTag/?tag='+tag+'&start='+start
        // console.log(url)
        getMoviesByUrl(API_WEEKLY).then(res => {
          res = res.data
          // this.movies = res.subject
          // this.movies=[]
          // this.movies=res.subjects
          this.newMovies.push(...res.subjects)
          // this.movies.append(res.subjects)
          // console.log(this.newMovies.length)
          // if(this.newMovies.length>20){
          //   console.log(movies[22]["title"])
          // }
        }).catch(err => {
          this.$message.error('获取分类数据失败')
        })
      },
    }
  }
</script>

<style lang="stylus" scoped>
  .title
    margin-top 20px
    padding 10px 0 0 10px
    border-bottom 1px dashed #ddd
    h1
      font-size 24px
    h2
      font-size 18px
      color #087626
</style>
