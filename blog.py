import os
from flask import Flask,render_template,url_for,request
from flask_sqlalchemy import SQLAlchemy
import model

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'blog.db')
db = SQLAlchemy(app)

@app.route('/')
@app.route('/index')
def index():
    #db.query.get()
	return render_template('index.html',db = db,post = model.post)
	
@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')

@app.route('/page')
def page():
	return render_template('page.html')

@app.route('/works')
def works():
	return render_template('works.html')

@app.route('/article')
def article():
    id = (int)(request.args.get("ids"))
    return render_template('article.html',post = model.post,ids = id,db = db)

if __name__ == "__main__":
	app.run(debug = True)