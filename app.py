from flask import Flask,redirect,url_for,render_template

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def home():
    return render_template('index.html')

@app.route('/dashboard', methods=["GET","POST"])
def dashboard():
    return render_template('dashboard.html')

@app.route('/report', methods=["GET","POST"])
def report():
    return render_template('report.html')

@app.route('/story', methods=["GET","POST"])
def story():
    return render_template('story.html')

#run server
if __name__ == "__main__":
    app.run(debug=True)
