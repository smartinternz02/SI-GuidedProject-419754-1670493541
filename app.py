from flask import Flask, request,render_template
import joblib,pickle
import numpy as np
app = Flask(__name__)
model = pickle.load(open("modelor.pkl","rb"))
ct = joblib.load("transform")

@app.route('/')
def predict():
    return render_template('Manual_predict.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():
    #x_test = [x for x in request.form.values()]
    a = request.form["gender"]
    b = request.form["Age"]
    c = request.form["Hypertension"]
    d = request.form["Heart Disease"]
    e = request.form["Ever Married"]
    f = request.form["Work Type"]
    g = request.form["Residence Type"]
    h = request.form["avg glucose level"]
    i = request.form["BMI"]
    j = request.form["Work Type"]
    #print('actual',x_test)
    #x_test np.array(x_test, dtype=float)
    #x_test = [[ float(i) for i in x_test]]
    x_test= [[a,b,c,d,e,f,g,h,i,j]]
    x_test = [[ float(i) for i in x_test[0]]]
    pred = model.predict(x_test)
    #print(pred)
    if(pred[0]==0):
        result="no chances of stroke"
    else:
        result="chances of stroke"
    
    return render_template('Manual_predict.html', \
                           prediction_text=('There are '+ result))
app.run(debug=True)
    
