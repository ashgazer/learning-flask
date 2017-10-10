from flask import Flask, render_template

app = Flask(__name__)

app.config('SQLALCHEMY_DATABASE_URI') = 'postgresql://localhost/learningflask'



@app.route("/")
def index():
	return render_template("index.html")


@app.route("/my_t")
def mt_t():
	a = 4
	b = 2
	c = a * b
	return (str(c))



@app.route("/about")
def about():
	return render_template('about.html')

if __name__ == "__main__":
	app.run(debug=True)

	