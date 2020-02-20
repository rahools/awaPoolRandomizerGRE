from flask import Flask
import pickle
import random
# from data.issueScrapper import scrapper

with open('data/issue.pkl', 'rb') as f:
        issue = pickle.load(f)

with open('data/argument.pkl', 'rb') as f:
        argument = pickle.load(f)

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/issue', methods=['GET'])
def issueFunc():
    return issue[random.choice(range(len(issue)))]

@app.route('/argument', methods=['GET'])
def argumentFunc():
    return argument[random.choice(range(len(argument)))]

@app.route('/', methods=['GET'])
def index():
    return 'Hello, GRE takers. Visit /issue or /argument'

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000)