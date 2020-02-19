from flask import Flask
import pickle
import random

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/issue', methods=['GET'])
def issueFunc():
    with open('issue.pkl', 'rb') as f:
        issue =  = pickle.load(f)
    return issue[random.choice(range(len(issue)))]

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000)