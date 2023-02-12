from flask import Flask, request, render_template
from flask_restful import Api
import db
from models import Ad, Seller, SparePart
import routes
from mail import function

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'host':'mongodb://localhost:27017/wow'
}

api=Api(app)
db.initialize_db(app)
routes.initialize_routes(api)

@app.route('/')
def home():
   data = Ad.objects.filter(status = "approved")
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
   context = Ad.objects.filter(status = "approved")
   return render_template('get-ads.html', context = context)

@app.route('/car',  methods = ['GET','POST'])
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

@app.route('/spare-part-ad', methods=['GET', 'POST'])
def post_spare_part_ad():
   return render_template('spare-part-post-ad.html')

@app.route('/about-us')
def about_us():
	return render_template('about.html')

@app.route('/model-toyota')
def model_toyota():
	urls=[["../static/images/models/Toyota/toyota-corolla.jpg", "../static/images/models/Toyota/toyota-landcruiser.jpg", "../static/images/models/Toyota/2018_totoya-yaris.png", "../static/images/models/Toyota/w1SfM7.webp", "../static/images/models/Toyota/2500611.webp"],["34,00,000","77,00,000","450,000","15,000,000","3,500,000"],["Corolla","Land Cruiser","Yaris","Fortuner","Vitz"]]
	return render_template('model-toyota.html', urls=urls)

@app.route('/model-kia')
def model_kia():
   urls=[["../static/images/models/Kia/Kia-Optima-Sportswagon-Plug-in-Hybrid-2017-fotoshowBig-3957e91c-287427.jpg", "../static/images/models/Kia/2016-kia-optima-hybrid-wallpaper-preview.jpg", "../static/images/models/Kia/558827.jpg", "../static/images/models/Kia/690966.jpg", "../static/images/models/Kia/white-background-sedan-kia-kia-wallpaper-preview.jpg", "../static/images/models/Kia/5483417.webp"],[5000000,2000000,4000000,5000000,60000,700000],["Optima","Carnival","Sorento","Optima","K7","Seltos"]]
   print("abc")
   return render_template('model-kia.html', urls=urls)

@app.route('/model-hyundai')
def model_hyundai():
    urls=[["../static/images/models/Hyundai/79812b8dcc2b5e0c4f6e573fc3797107.png", "../static/images/models/Hyundai/hyundai-i-station-wagon-white-isolated-white-63742513.jpg", "../static/images/models/Hyundai/white-background-hyundai-elantra-hyundai-wallpaper-preview.jpg", "../static/images/models/Hyundai/white-background-hyundai-crossover-tucson-wallpaper-preview.jpg", "../static/images/models/Hyundai/abc.jpg"],[5000000,2000000,4000000,5000000,60000],["Santa","Elentra avante","Elentra","Tucson","Tucson"]]
    return render_template('model-hundi.html',urls = urls)
   
@app.route('/model-haval')
def model_haval():
    urls=[["../static/images/models/Havel/Haval_H6_Front.jpg", "../static/images/models/Havel/Haval_H9_2019_SUV_Grey_Metallic_Side_White_589872_1365x1024.jpg", "../static/images/models/Havel/Joilion_-_PNG.png"],[5000000,2000000,40000000],["Haval H6","Haval H9","Jolion"]]
    return render_template('model-havel.html',urls = urls)  

@app.route('/model-honda')
def model_honda():
	urls=[["../static/images/models/Honda/honda_Civic_.jpg", "../static/images/models/Honda/Honda_City.jpg", "../static/images/models/Honda/HR-V.jpg", "../static/images/models/Honda/BRV.jpg"]
          ,["Honda Civic","Honda City","Honda HR-V","Honda BR-V"],["70,00,000 pkr","50,00,000 pkr","75,00,000 pkr","40,00,000 pkr"]]
	return render_template('model-honda.html', urls=urls)    

@app.route('/model-MG')
def model_MG():
	urls=[["../static/images/models/mg/ep.jpg", "../static/images/models/mg/marvel.png", "../static/images/models/mg/gt.jpg", "../static/images/models/mg/zs.jpg", "../static/images/models/mg/mg4.jpg", "../static/images/models/mg/mg3.jpg"],[5000000,1000000,200000,500000,64000,700000],["MG EP","MG MARVEL R","MG GT","MG ZS","MG-4","MG-3"]]
	return render_template('model-MG.html', urls=urls)

@app.route('/model-pugeot')
def model_pugeot():
	urls=[["../static/images/models/pugeot/5008.png", "../static/images/models/pugeot/3008.png", "../static/images/models/pugeot/2008.jpg", "../static/images/models/pugeot/508.png", "../static/images/models/pugeot/309.jpg", "../static/images/models/pugeot/206.jpeg"],[5400000,2000000,4599900,50550000,600000,459000],["PUGEOT 5008","PUGEOT 3008","PUGEOT 2008","PUGEOT 508","PUGEOT 309","PUGEOT 206"]]
	return render_template('model-pugeot.html', urls=urls)

@app.route('/model-suzuki')
def model_suzuki():
	urls=[["../static/images/models/suzuki/swift.jpg", "../static/images/models/suzuki/alto.png", "../static/images/models/suzuki/cultus.png", "../static/images/models/suzuki/wagonr.png"]
   ,["Suzuki Swift","Suzuki Alto","Suzuki Cultus","Suzuki WagonR"],["45,00,000 pkr","25,00,000 pkr","35,00,000 pkr","32,00,000 pkr"]]
	return render_template('model-suzuki.html', urls=urls)

@app.route('/get-spare-parts-engine')
def get_spare_parts_engine():
   context = SparePart.objects.filter(category = "Engine")
   return render_template('get-spare-parts-engine.html', context=context)

@app.route('/get-spare-parts-interior')
def get_spare_parts_interior():
   context = SparePart.objects.filter(category = "Interior")
   return render_template('get-spare-parts-interior.html', context=context)

@app.route('/get-spare-parts-exterior')
def get_spare_parts_exterior():
   context = SparePart.objects.filter(category = "Exterior")
   return render_template('get-spare-parts-exterior.html', context=context)

@app.route('/get-spare-parts-brakes')
def get_spare_parts_brakes():
   context = SparePart.objects.filter(category = "Brakes")
   return render_template('get-spare-parts-brakes.html', context=context)

@app.route('/get-spare-parts-oil')
def get_spare_parts_oil():
   context = SparePart.objects.filter(category = "Oil")
   return render_template('get-spare-parts-oil.html', context=context)

@app.route('/get-spare-parts-wheels')
def get_spare_parts_wheels():
   context = SparePart.objects.filter(category = "Wheels")
   return render_template('get-spare-parts-wheels.html', context=context)

@app.route('/get-spare-parts-lights')
def get_spare_parts_lights():
   context = SparePart.objects.filter(category = "lights")
   return render_template('get-spare-parts-lights.html', context=context)

@app.route('/get-spare-parts-sound')
def get_spare_parts_sound():
   context = SparePart.objects.filter(category = "Sound")
   return render_template('get-spare-parts-sound.html', context=context)

@app.route('/admin')
def admin():
	return render_template('admin.html', msg="ADMIN PANNEL")
   
@app.route('/admin-success', methods=['GET', 'POST'])
def admin_success():
   password = request.form.get("password")
   if password == "admin":
      return render_template('admin-success.html')
   else:
	   return render_template('admin.html', msg = "Incorrect Password")
   
@app.route('/admin-dashboard', methods=['GET', 'POST'])
def admin_dashboard():
   return render_template('admin-dashboard.html')

@app.route('/inspection', methods =['GET','POST'])
def inspection():
   return render_template("inpection.html")

@app.route('/sent-mail',methods = ['GET','POST'])
def sent_mail():
   email = request.form.get("email")
   function(email)
   return render_template("mail-sent.html")

if __name__ == '__main__':
	app.run(debug=True)
