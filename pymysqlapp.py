from flask import Flask, render_template, request
from db_model import DBConnection
import pandas as pd

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def get_index_page():
    return render_template('index.html')


@app.route('/results', methods=['POST', 'GET'])
def query_results():
    if request.method == "POST":
        sql = request.form['input_sql_query']
    else:
        sql = request.args.get('input_sql_query')

    res = run_sql_query(sql)
    return render_template('query_results.html', tables=[res.to_html(classes='data', header="true")])


def run_sql_query(sql):
    db = DBConnection()
    results = db.get_query_results(sql)
    return results


if __name__ == "__main__":
    app.run(debug=True, port=8888)
