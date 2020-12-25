<template>
  <div class="category-page">
    <a-row>
      <a-col :span="2"></a-col>
      <a-col :span="16">
        <h1 class="category-title">选影视</h1>
        <ul class="tags">
          <li @click="selectTag(index)" class="tag" :class="{ active: index === activeIndex }" v-for="(category, index) in categories" :key="category">{{ category }}</li>
        </ul>
        <loading v-if="!movies.length"></loading>
        <ul class="movie-list" v-else>
          <router-link tag="li" :to="{ name: 'MovieDetail', params: {id: movie.id} }" class="movie-item" v-for="(movie,index) in movies" :key="movie.id">
            <movie-list-item>
              <img v-lazy="movie.images.small" alt="" class="image" slot="thumbnail">
              <div class="title" slot="title">{{ movie.title }} / {{ movie.original_title }}</div>
              <div class="info" slot="info">{{ movie.pubdates[0] }} {{ stringifyCa(movie.casts) }}</div>
              <div class="rate" slot="rate">
                <a-rate :defaultValue="movie.rating.average/2" allowHalf disabled/>
                <span class="average">{{ movie.rating.average }}</span> ({{ movie.collect_count }}人评价)
              </div>
            </movie-list-item>
          </router-link>
        </ul>
      </a-col>
      <a-col :span="6">
        <go-top></go-top>
      </a-col>
    </a-row>
  </div>
</template>

<script>
  import MovieListItem from '../../components/movie-list-item/MovieListItem.vue'
  import Loading from '../../components/loading/Loading.vue'
  import GoTop from '../../components/go-top/GoTop.vue'
  import { getMoviesByUrl } from '../../apis/request'
  import { API_TAG } from '../../apis/urls'
  import Util from '../../common/js/util'

  export default {
    name: 'CategoryPage',
    components: {
      MovieListItem,
      Loading,
      GoTop
    },
    data() {
      return {
        categories: [
          '剧情', '爱情', '喜剧', '科幻', '动作', '悬疑', '犯罪',
           '战争'
        ],
        tag: '剧情',
        start: 0,
        movies: [],
        activeIndex: 0
      }
    },
    created() {

      this._getMoviesByTag(this.tag, this.start)
      // getMoviesByUrl('http://localhost:5000/getMovieJson').then(res => {
      //   res = res.data
      //   // this.movies = res.subject
      //   // this.movies=[]
      //   // this.movies=res.subjects
      //   this.movies.push(...res.subjects)
      // }).catch(err => {
      //   this.$message.error('获取分类数据失败')
      // })
    },
    methods: {
      selectTag(index) {
        this.tag = this.categories[index]
        this.start = 0
        this.movies = []
        this.activeIndex = index
        this._getMoviesByTag(this.tag, this.start)
      },
      loadMore() {
        this.start = 0
        this._getMoviesByTag(this.tag, this.start)
      },
      _getMoviesByTag(tag, start) {
        let url='http://localhost:5000/getMovieJsonByTag/?tag='+tag+'&start='+start
        console.log(url)
        getMoviesByUrl(url).then(res => {
          res = res.data
          // this.movies = res.subject
          // this.movies=[]
          // this.movies=res.subjects
          this.movies.push(...res.subjects)
          // this.movies.append(res.subjects)
          console.log(this.movies.length)
          if(this.movies.length>20){
            console.log(movies[22]["title"])
          }
        }).catch(err => {
          this.$message.error('获取分类数据失败')
        })
      },
      stringifyCa(casts) {
        return Util.stringifyCasts(casts)
      }
    },
  }
</script>

<style lang="stylus" scoped>
  .category-page >>> .ant-rate
    color #e2952b
    font-size 12px

  .category-page
    .category-title
      font-size 24px
      font-weight 700
      color rgba(0, 0, 0, 0.65)
      margin-top 30px
    .tags
      display flex
      flex-flow wrap
      .tag
        font-size 14px
        color #333
        padding 2px 10px
        margin-bottom 5px
        cursor pointer
        transition all .3s
        &:hover
          color #108ee9
        &.active
          color #fff
          background-color #2a8ccb
          border-radius 3px
    .movie-list
      .movie-item
        padding 15px 10px
        border-top 1px dashed #ddd
        cursor pointer
        .title
          font-size 14px
          color #3576aa
          margin-bottom 5px
        .info
          color #666
          margin-bottom 5px
        .rate
          color #666
          .average
            color #e2952b
    .load-more
      color #3576a8
      text-align center
      background-color #f7f7f7
      cursor pointer
      padding 10px 0
      transition all .3s
      &:hover
        color #108ee9
</style>
