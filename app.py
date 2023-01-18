from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('homepage.html')

@app.route('/signup')
def signup():
	return render_template('signup.html')

@app.route('/signup-seller')
def signup_seller():
	return render_template('signup-seller.html')

@app.route('/about-us')
def about_us():
	return render_template('about2.html')

if __name__ == '__main__':
	app.run(debug=True)
