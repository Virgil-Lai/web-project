<template>
  <div class="user-center">
    <a-row>
      <a-col :span="2"></a-col>
      <a-col :span="20">
        <div class="login-register">
          <a-tabs defaultActiveKey="1" @change="callback">
            <a-tab-pane tab="登陆" key="1">
              <form class="form-horizontal">
                <div class="form-group">
                  <label class="col-sm-3 control-label">用户名</label>
                  <div class="col-sm-8">
                    <input v-model="loginUser.username" type="text" class="form-control">
                  </div>
                </div>
                <div class="form-group">
                  <label class="col-sm-3 control-label">密码</label>
                  <div class="col-sm-8">
                    <input v-model="loginUser.password" type="password" class="form-control">
                  </div>
                </div>
                <div class="button-group">
                  <button @click.prevent="doLogin" class="btn btn-primary">登陆</button>
                  <button @click.prevent="doLoginCancel" class="btn btn-danger">取消</button>
                </div>
              </form>
            </a-tab-pane>

            <a-tab-pane tab="注册" key="2" forceRender>
              <form class="form-horizontal">
                <div class="form-group">
                  <label class="col-sm-3 control-label">用户名</label>
                  <div class="col-sm-8">
                    <input v-model="registerUser.username" type="text" class="form-control">
                  </div>
                </div>
                <div class="form-group">
                  <label class="col-sm-3 control-label">密码</label>
                  <div class="col-sm-8">
                    <input v-model="registerUser.password" type="password" class="form-control">
                  </div>
                </div>
                <div class="form-group">
                  <label class="col-sm-3 control-label">确认密码</label>
                  <div class="col-sm-8">
                    <input v-model="registerUser.confirmPassword" type="password" class="form-control">
                  </div>
                </div>
                <div class="button-group">
                  <button class="btn btn-primary" @click.prevent="doRegister">注册</button>
                  <button class="btn btn-danger" @click.prevent="doRegisterCancel">取消</button>
                </div>
              </form>
            </a-tab-pane>
          </a-tabs>
        </div>
      </a-col>
      <a-col :span="2"></a-col>
    </a-row>
  </div>
</template>

<script>
import {
  mapState
} from 'vuex'
export default {
  name: 'UserCenter',
  data() {
    return {
      registerUser: {
        username: '',
        password: '',
        confirmPassword: ''
      },
      loginUser: {
        username: '',
        password: ''
      }
    }
  },
  computed: {
    ...mapState(['user', 'isLogin'])
  },
  created() {
    console.log(this.user.username, this.user.password)
  },
  methods: {
    doLogin() {
      let {
        username,
        password
      } = this.loginUser
      if (username.length === 0 || password.length === 0) {
        this.$message.error('输入内容不能为空')
        return
      }
      if(this.if_right()){
        localStorage.setItem("login_token",username);
        this.$message.success('登陆成功')
        this.$store.commit('changeLoginStatus', true)
        this.$router.push('/')
      }
    },
    doLoginCancel() {
      this.loginUser.username = ''
      this.loginUser.password = ''
      this.$message.error('取消登陆')
    },
    doRegister() {
      let {
        username,
        password,
        confirmPassword
      } = this.registerUser
      if (username.length === 0 || password.length === 0 || confirmPassword.length === 0) {
        this.$message.error('注册失败-输入内容不能为空')
        return
      }
      var reg=/^[a-zA-Z0-9]{6,12}$/;
      if(reg.test(password)==false){
        this.$message.error('密码格式不正确，应包含字母和数字，并且6-12位')
        return
      }
      if (password !== confirmPassword) {
        this.$message.error('注册失败-两次密码输入不一致')
        return
      }
      this.$store.commit('registerUser', {
        username: username,
        password: password
      })
      let userDetail = {
        username: this.registerUser.username,
        password: this.registerUser.password
      }
      localStorage.setItem('user_detail', userDetail)
      this.setCookie(username,password,7)
      this.$message.success('注册成功')
      this.registerUser.username = ''
      this.registerUser.password = ''
      this.registerUser.confirmPassword = ''
      console.log('after', this.user.username, this.user.password)
    },
    doRegisterCancel() {
      this.registerUser.username = ''
      this.registerUser.password = ''
      this.registerUser.confirmPassword = ''
      this.$message.error('取消注册')
    },
    callback(key) {
    },
    //设置cookie
    setCookie(c_name, c_pwd, exdays) {
      var exdate = new Date(); //获取时间
      exdate.setTime(exdate.getTime() + 24 * 60 * 60 * 1000 * exdays); //保存的天数
      //字符串拼接cookie
      window.document.cookie =c_name + "=" +c_pwd+ ";path=/;expires=" + exdate.toGMTString();
    },
    //读取cookie
    getCookie: function() {
      console.log(document.cookie)
      if (document.cookie.length > 0) {
        var arr = document.cookie.split(";"); //这里显示的格式需要切割一下自己可输出看下
        for (var i = 0; i < arr.length; i++) {
          var arr2 = arr[i].split("="); //再次切割
          //判断查找相对应的值
          this.loginUser.username = arr2[0]; //保存到保存数据的地方
          this.loginUser.password = arr2[1];
        }
      }
    },
    if_right: function (){
      console.log(document.cookie)
      if (document.cookie.length > 0) {
        var arr = document.cookie.split(";"); //这里显示的格式需要切割一下自己可输出看下
        for (var i = 0; i < arr.length; i++) {
          var arr2 = arr[i].split("="); //再次切割
          //判断查找相对应的值
          if (this.loginUser.username == arr2[0]&&this.loginUser.password == arr2[1]) {
            return true;
          }
        }
        this.$message.error('账号或密码错误')
        return false;
      }
    },
    //清除cookie
    clearCookie: function() {
      this.setCookie("", "", -1); //修改2值都为空，天数为负1天就好了
    }
  },
  mounted() {
    this.getCookie();
  },
}
</script>

<style lang="stylus" scoped>
.user-center
  .login-register
    width 40%
    text-align center
    margin 30px auto
</style>
