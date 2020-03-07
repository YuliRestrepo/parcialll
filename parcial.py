import pandas as pd
from flask import Flask, render_template
import datetime

app = Flask(__name__)

data = {'Tiempo':['Lluvioso'],'Temperatura':['30 grados'], 'Humedad':['10%']}
df = pd.DataFrame(data, columns = ['Tiempo','Temperatura','Humedad'])
df.to_csv('03062020.csv')

def myparser(x):
    return datetime.strptime(x, '%d/%m/%Y %H:%M:%S')

@app.route('/')
def archivo():
    df= pd.read_csv('03062020.csv', parse_dates=True, date_parser=myparser, header=None)
    listk = list(df.values)
    return render_template('index.html', listk = listk)

if __name__ == "__main__":
    app.run(debug= True, port=80)




