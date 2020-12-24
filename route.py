# import pymysql
import json
from flask import Flask, render_template, request, flash, jsonify, make_response
from flask import Flask, render_template, session, request, \
    copy_current_request_context
from flask_cors import CORS
from pymongo import MongoClient
from bson import json_util
#建立Mongodb数据库连接
client=MongoClient('mongodb://lwj:123456@49.232.135.197',27017)
db=client.admin

# async_mode = None

app = Flask(__name__)
CORS(app, resources=r'/*')
# app.config['SECRET_KEY'] = 'secret!'
#
# db = pymysql.connect(host='121.196.111.9',
#                          port=3306,
#                          user='test',
#                          passwd='123456',
#                          db='blogs'
#                          )
# 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()
# # # 使用execute方法执行SQL语句
# # cursor.execute("SELECT VERSION()")
# # # 使用 fetchone() 方法获取一条数据
# # data = cursor.fetchone()
# # print("Database version : %s " % data)

@app.route('/getMovieJson', methods=['GET', 'POST'])
def getAllMovies():
    movies=db.moviesJson.find_one()
    print(type(movies))
    print(movies)
    movies['_id']=''
    # movies=json.loads()['subjects']
    dictionay={}
    # dictio
    # print(movies['subjects'])
    # movies=str(movies)
    print(type(movies))
    print(movies)
    # print(movies)
    # while mycursor.hasNext():
    #   print(mycursor.next())
    # movies=db.moviesJson.find().next().pretty()
    # print(movies)
    # with open(r'D:\web-project\static\resource\moviesJson',"r",encoding='utf-8') as json_file:
    # config = json.load(movies)
    # print(movies)
    # config=json.loads(movies)
    # print(type(config))
    res=make_response(movies)
    # print(type(res))
    # res.headers['Access-Control-Allow-Origin'] = '*'
    res.headers['Access-Control-Allow-Credentials'] = 'true'
    res.headers['Access-Control-Allow-Origin'] = request.environ['HTTP_ORIGIN']
    res.headers['Access-Control-Allow-Methods'] = 'POST'
    res.headers['Access-Control-Allow-Headers'] = 'Content-Type, X-Requested-With'
    print(res)
    return res
    #
    # return jsonhh
    # return
    # 获取POST传值

@app.route('/getMovieDetail/', methods=['GET', 'POST'])
def getMovieDetail():
    id = request.args.get('id')
    # movie="moviesJson"+id
    movies = db["movieDetail"+id].find_one()
    print(type(movies))
    print(movies)
    movies['_id'] = ''
    res = make_response(movies)
    # print(type(res))
    # res.headers['Access-Control-Allow-Origin'] = '*'
    res.headers['Access-Control-Allow-Credentials'] = 'true'
    res.headers['Access-Control-Allow-Origin'] = request.environ['HTTP_ORIGIN']
    res.headers['Access-Control-Allow-Methods'] = 'POST'
    res.headers['Access-Control-Allow-Headers'] = 'Content-Type, X-Requested-With'
    print(res)
    return res

@app.route('/getMovieJsonByTag/', methods=['GET', 'POST'])
def getMovieByTag():
    tag = request.args.get('tag')
    start= request.args.get('start')
    # data={}
    choose_movie=[]
    movies = db.moviesJson.find_one()
    print(type(movies))
    print(movies)
    movies['_id'] = ''
    print("Start="+start)
    if(tag=='电影'):
        n=0
        subject=movies["subjects"]
        i=0
        print("subject="+str(len(subject)))
        for each in subject:
            if n >= int(start):
                print("n="+str(n))
                i=i+1
                choose_movie.append(each)
                if(i>20):
                    break
            n=n+1
        data = {}
        data["count"] = 20
        data["start"] = 0
        data["total"] = i
        data["subjects"] = choose_movie
        print(len(choose_movie))
        # return_data=jsonify(config)
        res = make_response(data)
        # res.headers['Access-Control-Allow-Origin'] = '*'
        res.headers['Access-Control-Allow-Credentials'] = 'true'
        res.headers['Access-Control-Allow-Origin'] = request.environ['HTTP_ORIGIN']
        res.headers['Access-Control-Allow-Methods'] = 'POST'
        res.headers['Access-Control-Allow-Headers'] = 'Content-Type, X-Requested-With'
        print(res)
        return res
    else:
        n = 1
        j = 0
        subject=movies["subjects"]
        for each in subject:
            if n>=int(start):
                for i in each["genres"]:
                    if tag==i:
                        j=j+1
                        if(j>=20):
                            break
                        choose_movie.append(each)
            n=n+1
        data={}
        data["count"]=20
        data["start"]=0
        data["total"]=j
        data["subjects"]=choose_movie
        res = make_response(data)
        # res.headers['Access-Control-Allow-Origin'] = '*'
        res.headers['Access-Control-Allow-Credentials'] = 'true'
        res.headers['Access-Control-Allow-Origin'] = request.environ['HTTP_ORIGIN']
        res.headers['Access-Control-Allow-Methods'] = 'POST'
        res.headers['Access-Control-Allow-Headers'] = 'Content-Type, X-Requested-With'
        print(res)
        return res

if __name__ == '__main__':
    app.run(port=5000,debug=True)

