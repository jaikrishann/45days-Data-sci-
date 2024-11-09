from flask import Flask, render_template,url_for,request
import joblib

model = joblib.load("lr_model.lb")

app = Flask(__name__)



##route 

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/homepage")
def homepage():
    return render_template('homepage.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/project")
def project():
    return render_template('project.html')

@app.route("/predict" , methods = ["GET", "POST"])
def predict():
    if request.method == "POST":
        brand_name = request.form["brand_name"]
        owner_name = int(request.form["owner"])
        age_bike = int(request.form["age"])
        power_bike = int(request.form["power"])
        kms_driven_bike = int(request.form["kms_driven"])
        bike_number = {'TVS': 0,
                        'Royal Enfield': 1,
                        'Triumph': 2,
                        'Yamaha': 3,
                        'Honda': 4,
                        'Hero': 5,
                        'Bajaj': 6,
                        'Suzuki': 7,
                        'Benelli': 8,
                        'KTM': 9,
                        'Mahindra': 10,
                        'Kawasaki': 11,
                        'Ducati': 12,
                        'Hyosung': 13,
                        'Harley-Davidson': 14,
                        'Jawa': 15,
                        'BMW': 16,
                        'Indian': 17,
                        'Rajdoot': 18,
                        'LML': 19,
                        'Yezdi': 20,
                        'MV': 21,
                        'Ideal': 22}
        brand_number = bike_number[brand_name]
        lst = [[owner_name,brand_number,kms_driven_bike,age_bike,power_bike]]  ##single predicitin 
        prediction = model.predict(lst)
        prediction = prediction[0]
        return render_template('project.html', prediction=prediction[0])
        

if __name__ == '__main__':
    app.run(debug=True)