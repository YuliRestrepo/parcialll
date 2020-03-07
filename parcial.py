import redis, os, json, redis
from flask import Flask, render_template, request, url_for
from dotenv import load_dotenv
from pathlib import Path
from datetime import datetime
from flask import redirect
from pymysql as db

APP_ROOT = os.path.join(os.path.dirname(__file__))   
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

r = redis.StrictRedis(host=os.getenv('REDIS_HOST'),
        port=os.getenv('REDIS_PORT'), db=0, password=os.getenv('REDIS_PASS'), ssl=True)

app = Flask(__name__)

class MySQL:

    host = os.getenv('MYSQL_HOST')
    user = os.getenv('MYSQL_USER')
    password = os.getenv('MYSQL_PASS')
    db = os.getenv('MYSQL_DB')
    con = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.
                                DictCursor)
    cur = con.cursor()

    def insert_data(self, time, temperature):
        sql = "INSERT INTO `data` (`time`, `temperature`) VALUES (%s, %s)"
        self.cur.execute(sql, (time, temperature))
        self.con.commit()
        r.get('data')

@app.route('/', methods=['POST'])
def create():
    temperature = request.form['temperature']
    temperature = float(temperature.replace(',','.'))
    now = datetime.now().strftime('%Y %m %d %H:%M:%S')

    print(str(r.ping()))
    
    db.insert_data(now,temperature)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=80)


