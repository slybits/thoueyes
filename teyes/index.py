from flask import *
import requests
import re

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
@app.route("/index", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        r = re.compile('^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')
        apitoken = (request.form.get('key'))
        if not r.match(apitoken):
            return jsonify({'Alert': 'Invalid Input, Please Obtain a Valid Token From ThousandEyes.com and Try Again!'}) 
        else:
            url = "https://api.thousandeyes.com/v7/tests"
            payload = None
            headers = { "Accept": "application/hal+json", "Authorization": "Bearer " + apitoken }
            response = requests.request('GET', url, headers=headers, data = payload, verify=True)
            response = (response.text.encode('utf8'))
            return response

    return render_template("index.html")

if __name__ == "__main__":
    # Please do not set debug=True in production
    app.run(host="0.0.0.0", port=5000, debug=True)
