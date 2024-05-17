from flask import Flask, render_template, request
import random_forest

app = Flask(__name__)

# Default route set as 'home'
@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify_type():
    try:
        sepal_len = request.form.get('slen')  # Get parameters for sepal length
        sepal_wid = request.form.get('swid')  # Get parameters for sepal width
        petal_len = request.form.get('plen')  # Get parameters for petal length
        petal_wid = request.form.get('pwid')  # Get parameters for petal width

        # Get the output from the classification model
        variety = random_forest.classify(sepal_len, sepal_wid, petal_len, petal_wid)

        # Render the output in new HTML page
        return render_template('result.html', variety=variety[0], proba0=variety[1][0],
                               proba1=variety[1][1], proba2=variety[1][2], slen=sepal_len,
                               swid=sepal_wid, plen=petal_len, pwid=petal_wid)
    except Exception as e:
        return f"An error occurred: {str(e)}"


@app.route('/plots')
def plots():
    return render_template('plots.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3500)
