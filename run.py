from flask import Flask,request,jsonify,render_template
import insurance_db
import test_model
import functions
import insurance

app=Flask(__name__)

@app.route('/') #default
def home_page():
    return render_template(['about.html','contact.html','index.html','resource.html'])

@app.route('/get_region_names',methods=['GET'])
def get_region_names():
    response=jsonify({
        'regions':test_model.get_region_names()
    })
    return response

@app.route('/smoker_predict',methods=['GET','POST'])
def smoker_predict():
    if request.method=='POST':
        data=request.form
        print(data)
        age=int(data['age'])
        sex=int(data['sex'])
        bmi=float(data['bmi'])
        region=data.get('region')
        smoker=int(data['smoker'])
        print('age,sex,bmi,region,smoker',age,sex,bmi,region,smoker)
        prediction = test_model.get_smoker_predict(age,sex,bmi,region,smoker)
        insurance_db.save_smoker_details(age, sex, bmi, region, smoker,prediction)
        return ('the predicted person is {}'.format(prediction))
    return render_template(['about.html','contact.html','index.html','resource.html'])      

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        data = request.form
        response = insurance_db.register_user(data)

    return jsonify({'msg':response})

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        data = request.form
        response = insurance_db.login_user(data)
    return jsonify({'msg':response})


if __name__=="__main__":
    print("starting the python flask for insurance........")
    app.run(host='0.0.0.0',port=5000)
