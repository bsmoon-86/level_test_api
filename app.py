from flask import Flask, request, render_template, jsonify
import pandas as pd

app = Flask(__name__)


@app.route('/')
def index():
    df = pd.read_csv("./csv/iris.csv")
    data = df.to_dict(orient='records')
    cols = df.columns
    return render_template('dashboard.html', table_data = data, table_cols = cols)

@app.route('/open_api')
def open():
    serviece_key = request.args['servicekey']
    if serviece_key == 'asdf1234':
        df = pd.read_csv("./csv/df_sample.csv")
        result = df.to_dict(orient='records')
        return jsonify(result)
    else:
        return "Servicekey_error"


app.run()