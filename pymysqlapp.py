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

    res, msg = run_sql_query(sql)
    if res is not None:
        return render_template('query_results.html', tables=[res.to_html(classes='data', header="true")])
    else:
        return render_template('error.html', status_message=msg)


def run_sql_query(sql):
    db = DBConnection()
    results, status_msg = db.get_query_results(sql)
    return results, status_msg


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
