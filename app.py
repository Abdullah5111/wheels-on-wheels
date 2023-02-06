from flask import Flask, jsonify,request, render_template
from flask_restful import Api
import db
from models import Ad, Seller
import routes

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'host':'mongodb://localhost:27017/wow'
}

api=Api(app)
db.initialize_db(app)
routes.initialize_routes(api)

@app.route('/')
def home():
   data = Ad.objects.all()
   data = data[0:4]
   return render_template('homepage.html', data = data)

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
	return render_template('signup.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
	return render_template('login.html')
	
@app.route('/get-ads', methods = ['GET', 'POST'])
def get_ads():
   context = Ad.objects.all()
   return render_template('get-ads.html', context = context)

@app.route('/car',  methods = ['POST'])
def car():
   id = request.form.get("id")
   creator = request.form.get("creator")
   ad = Ad.objects.get(id=id)
   seller=Seller.objects.filter(username=creator)
   context = [ad, seller[0]]
   return render_template('car.html', context=context)

@app.route('/seller-dashboard')
def seller_dashboard():
   return render_template('seller-dashboard.html')

@app.route('/ad', methods=['GET', 'POST'])
def post_ad():
   return render_template('post-ad.html')

@app.route('/seller-info', methods=['POST'])
def your_info():
   return render_template('seller-info.html')

@app.route('/about-us')
def about_us():
	return render_template('about2.html')

@app.route('/model-toyota')
def model_toyota():
	urls=["../static/images/models/toyota-landcruiser.jpg", "../static/images/models/toyota-corolla.jpg", "../static/images/models/toyota-landcruiser.jpg", "../static/images/models/toyota-landcruiser.jpg", "../static/images/models/toyota-landcruiser.jpg", "../static/images/models/toyota-landcruiser.jpg"]
	return render_template('model-toyota.html', urls=urls)

if __name__ == '__main__':
	app.run(debug=True)
