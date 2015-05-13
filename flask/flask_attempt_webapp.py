import flask
from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd

#---------- MODEL IN MEMORY ----------------#

# Read the scientific data on breast cancer survival,
# Build a LogisticRegression predictor on it
patients = pd.read_csv("flask_df.csv")
patients.columns=['sex','period','totchol','age', 'sysbp', 'diabp',
                  'cigpday', 'bmi', 'heartrte', 'glucose',
                  'angina', 'hospmi', 'mi_fchd', 'anychd', 'stroke',
                  'cvd', 'hyperten']


# patients=patients.replace(2,0)  # The value 2 means death in 5 years

X = patients[['sex','period','totchol','age', 'sysbp', 'diabp',
                 'bmi', 'heartrte', 'glucose']]
Y = patients['angina']
PREDICTOR = LogisticRegression().fit(X,Y)


#---------- URLS AND WEB PAGES -------------#

# Initialize the app
app = flask.Flask(__name__)

# Homepage
@app.route("/")
def viz_page():
    """ Homepage: serve our visualization page, awesome.html
    """
    with open("first_attempt.html", 'r') as viz_file:
        return viz_file.read()

# Get an example and return it's score from the predictor model
@app.route("/score", methods=["POST"])
def score():
    """  When A POST request with json data is made to this uri,
         Read the example from the json, predict probability and
         send it with a response
    """
    # Get decision score for our example that came with the request
    print "hello"
    data = flask.request.json
    print X
    x = np.matrix(data["example"])
    print x
    score = PREDICTOR.predict_proba(x)
    print score
    # Put the result in a nice dict so we can send it as json
    results = {"score": score[0,1]}
    return flask.jsonify(results)

#--------- RUN WEB APP SERVER ------------#
app.debug = True

# Start the app server on port 80
# (The default website port)
app.run(host='0.0.0.0', port=80)

