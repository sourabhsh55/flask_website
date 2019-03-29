from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap 
#import json 

'''with open('config.json','r') as c:
	params= json.load(c)["params"]'''
app = Flask(__name__)
Bootstrap(app) 

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/saltyml'
db = SQLAlchemy(app)

class Posts(db.Model):
	sno=db.Column(db.Integer,primary_key=True)
	title=db.Column(db.String(80),nullable=False)
	slug=db.Column(db.String(21),nullable=False)
	content=db.Column(db.String(121),nullable=False)
	date=db.Column(db.String(21),nullable=True)


@app.route("/original")
def new():
	return render_template('original.html')


@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html')

@app.route("/about")
def about():
	return render_template('about.html')

@app.route("/blog/<string:post_slug>", methods=['GET'])
def blogs(post_slug):
	post=Posts.query.filter_by(slug=post_slug).first()
	return render_template('posting.html',post=post)

@app.route("/blog")
def blog1():
	return render_template('blog.html')

@app.route("/posting")
def posting():
	return render_template('posting.html')

@app.route("/project1")
def project1():
	return render_template('project1.html')

@app.route("/project2")
def project2():
	return render_template('project2.html')

@app.route("/admin")
def admin():
	return render_template("admin.html")

@app.route("/contact")
def contact():
	return render_template("contact.html")


if __name__== '__main__':
	app.run(debug=True)