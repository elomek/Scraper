from flask import Flask , render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')




@app.route('/', methods=('GET', 'POST'))
def index():
    db = client['briet_quotes']
    collection = db['quotes_scrap']
    quotes = collection.find()
    return render_template('index.html', quotes=quotes)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)