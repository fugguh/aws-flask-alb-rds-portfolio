from flask import Flask, request
import pymysql

app = Flask(__name__)

# RDS接続情報
db = pymysql.connect(
    host="portfolio-db.crmq0iosol0e.ap-northeast-1.rds.amazonaws.com",
    user="admin",
    password="dbfugguh1",
    database="portfolio_app"
)

# 一覧表示
@app.route("/")
def index():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM posts")
    posts = cursor.fetchall()
    return str(posts)

# 投稿
@app.route("/add")
def add():
    content = request.args.get("content")
    cursor = db.cursor()
    cursor.execute("INSERT INTO posts (content) VALUES (%s)", (content,))
    db.commit()
    return "Added"

app.run(host="0.0.0.0", port=5000)
