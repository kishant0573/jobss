from flask import Flask , render_template
from database import load_jobs_from_db
app = Flask(__name__)

@app.route("/")
def first():
    job = load_jobs_from_db() 

    return render_template('home.html',jobs=job)
if __name__ == '__main__':
    app.run(debug=True,port=8000)                  #we can change port also port = 8000 and host also host = :"0.0.0.0"