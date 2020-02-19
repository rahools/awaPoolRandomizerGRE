from flask import Flask
import pickle
import random
from data.issueScrapper import scrapper

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/issue', methods=['GET'])
def issueFunc():
    with open('data/issue.pkl', 'rb') as f:
        issue = pickle.load(f)

    return issue[random.choice(range(len(issue)))]

@app.route('/issue/scrape', methods=['GET'])
def issueScrape():
    t = scrapper()
    
    return t

@app.route('/', methods=['GET'])
def index():
    return 'Hello, GRE takers. Visit /issue or /argument'

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000)