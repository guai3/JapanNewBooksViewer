# coding: utf-8
from flask import Flask, render_template
import MySQLdb
app = Flask(__name__)  # インスタンス生成


@app.route("/")  
def hello():  
    return "Hello World!"  


@app.route("/index")  
def index():
    conn = MySQLdb.connect(host='localhost', db='jpnbooks',
                           user='root', passwd='')  # MySQLサーバーに接続。
    cur = conn.cursor()  # カーソルを取得。
    cur.execute("SELECT imgurl FROM books")

    results = cur.fetchall()
    cur.close()
    conn.close()
    image_names = [results[i][0] for i, result in enumerate(results)]
    books = []
    for image in image_names:
        my_dic = {}
        my_dic['image_name'] = image
        my_dic['link_url'] = image
        books.append(my_dic)
        
    return render_template('index.html', message=books)

if __name__ == "__main__":
        # webサーバー立ち上げ
    app.run()
