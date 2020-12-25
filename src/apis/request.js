import axios from 'axios'

axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded'
axios.defaults.withCredentials = true

export function getMoviesByUrl(url) {
  return new Promise((resolve, reject) => {
    axios.get(url).then(res => {
      resolve(res)
    }).catch(err => {
      reject(err)
    })
  })
}

// 获取正在热映的电影
export function getMoviesInTheater() {
  return new Promise((resolve, reject) => {
    axios.get('http://localhost:5000/getMovieJson').then(res => {
      console.log(res)
      resolve(res)
    }).catch(err => {
      reject(err)
    })
  })
}

// 获取即将上映的电影
export function getComingMovie() {
  return new Promise((resolve, reject) => {
    axios.get('http://localhost:5000/getMovieJson').then(res => {
      console.log(res)
      resolve(res)
    }).catch(err => {
      reject(err)
    })
  })
}
