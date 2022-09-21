from typing import List, Dict
from flask import Flask
import mysql.connector
import json

app = Flask(__name__)


def test_table() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'rootroot',
        'host': 'db',
        'port': '3306',
        'database': 'testdb'
    }
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM test_table')
    results = [{id: name} for (id, name) in cursor]
    cursor.close()
    conn.close()

    return results

@app.route('/')
def top_page():
    return "<p>This is flask sample page!</p>"


@app.route('/users', methods=['GET'])
def index() -> str:
    return json.dumps({'test_table': test_table()})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
