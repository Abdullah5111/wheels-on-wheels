from flask import Flask, jsonify,request, render_template
from flask_restful import Api
from database import db
from database.models import Ad
from resources.resources import AdApi
from resources import routes

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

@app.route('/signup')
def signup():
	return render_template('signup.html')

@app.route('/login')
def login():
	return render_template('login.html')
   
@app.route('/ad')
def post_ad():
   return render_template('post-ad.html')
	
@app.route('/get-ad', methods = ['GET', 'POST'])
def uploader_file():
   if request.method == 'POST':
      company=request.form.get("company")
      model=request.form.get("model")
      price=request.form.get("price")
      registered_year=request.form.get("registered_year")
      registered_loc=request.form.get("registered_loc")
      current_loc=request.form.get("current_loc")
      engine_cap=request.form.get("engine_cap")
      km_driven=request.form.get("km_driven")
      transmission=request.form.get("transmission")
      description=request.form.get("description")
      temp =  request.files['file'].filename
      image ="../static/images/ads/" + temp
      creator=request.form.get("creator")
      context=[company,model,price,registered_year,registered_loc,current_loc,engine_cap,km_driven,transmission,description,image,creator]
      return render_template('get-ad.html', context = context)

@app.route('/seller-dashboard')
def seller_dashboard():
   context = Ad.objects.all()
   return render_template('seller-dashboard.html', context=context)

@app.route('/about-us')
def about_us():
	return render_template('about2.html')

@app.route('/model-toyota')
def model_toyota():
	urls=["../static/images/models/toyota-landcruiser.jpg", "../static/images/models/toyota-corolla.jpg", "../static/images/models/toyota-landcruiser.jpg", "../static/images/models/toyota-landcruiser.jpg", "../static/images/models/toyota-landcruiser.jpg", "../static/images/models/toyota-landcruiser.jpg"]
	return render_template('model-toyota.html', urls=urls)

if __name__ == '__main__':
	app.run(debug=True)
