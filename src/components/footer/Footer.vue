<template>
  <div class="footer">
    <a-row>
      <a-col :span="2"></a-col>
      <a-col :span="20">
        <div class="content">
          &copy; CopyRight All Reserved. Made By 烟火光影
        </div>
      </a-col>
      <a-col :span="2"></a-col>
    </a-row>
  </div>
</template>

<script>
  export default {
    name: 'Footer',
    computed: {
      currentYear() {
        return new Date().getFullYear()
      }
    },
  }
</script>

<style lang="stylus" scoped>
  .footer
    text-align center
    width 100%
    height 25px
    font-size 12px
    line-height 25px
    margin-top 10px
    .content
      border-top 1px dashed #ddd
      padding 10px 0
      .link
        padding-left 20px
        font-weight 700
</style>
