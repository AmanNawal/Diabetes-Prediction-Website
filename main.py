from flask import Flask,render_template,request
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
# from sklearn import svm
from sklearn.metrics import accuracy_score,confusion_matrix


#---------------------------------------------------------------------------------------------------------------

app = Flask(__name__)
#PS J:\0. 8th sem project> set FLASK_APP=main.py
#$env:FLASK_DEBUG = "1"
#PS J:\0. 8th sem project> $env:FLASK_APP = "main.py"
#PS J:\0. 8th sem project> flask run

#----------------------------------------------------CLASS SVM_classifier-----------------------------------------------------------


class SVM_classifier():


  # initiating the hyperparameters
  def __init__(self, learning_rate, no_of_iterations, lambda_parameter):

    self.learning_rate = learning_rate
    self.no_of_iterations = no_of_iterations
    self.lambda_parameter = lambda_parameter


  
  # fitting the dataset to SVM Classifier
  def fit(self, X, Y):

    # m  --> number of Data points --> number of rows
    # n  --> number of input features --> number of columns
    self.m, self.n = X.shape

    # initiating the weight value and bias value

    self.w = np.zeros(self.n)

    self.b = 0

    self.X = X

    self.Y = Y

    # implementing Gradient Descent algorithm for Optimization

    for i in range(self.no_of_iterations):
      self.update_weights()



  # function for updating the weight and bias value
  def update_weights(self):

    # label encoding
    y_label = np.where(self.Y <= 0, -1, 1)



    # gradients ( dw, db)
    for index, x_i in enumerate(self.X):

      condition = y_label[index] * (np.dot(x_i, self.w) - self.b) >= 1

      if (condition == True):

        dw = 2 * self.lambda_parameter * self.w
        db = 0

      else:

        dw = 2 * self.lambda_parameter * self.w - np.dot(x_i, y_label[index])
        db = y_label[index]


      self.w = self.w - self.learning_rate * dw

      self.b = self.b - self.learning_rate * db



  # predict the label for a given input value
  def predict(self, X):

    output = np.dot(X, self.w) - self.b
    
    predicted_labels = np.sign(output)

    y_hat = np.where(predicted_labels <= -1, 0, 1)

    return y_hat


#----------------------------------------------------- ACETONE TRAINING------------------------------------------------------------------------------

  #loading the diabetes dataset to pandas dataframe
diabetes_dataset=pd.read_csv('diabetes.csv')
#Separating data and labels
X=diabetes_dataset.drop(columns='Outcome',axis=1)
Y=diabetes_dataset['Outcome']
#-----------------Data standardization---------------------------------
scaler=StandardScaler()
scaler.fit(X)
standarized_data=scaler.transform(X)
X=standarized_data
Y=diabetes_dataset['Outcome']
#----------------splitting the data-----------------------------------
X_train,X_test,Y_train,Y_test=train_test_split(X,Y , test_size=0.2,stratify=Y,random_state=2)
classifier = SVM_classifier(learning_rate=0.001, no_of_iterations=1000, lambda_parameter = 0.01)
#Training the Support Vector Machine Classifier
classifier.fit(X_train,Y_train)

#--------------------------------------ACETONE END-------------------------------------------------


#------------------------------------------NORMAL PREDICTION------------------------------------------------------

#loading the diabetes dataset to pandas dataframe
normal_dataset=pd.read_csv('kaggle_diabetes.csv')

#Separating data and labels
normal_X=normal_dataset.drop(columns='Outcome',axis=1)
normal_Y=normal_dataset['Outcome']
normal_scaler=StandardScaler()
normal_scaler.fit(normal_X)
normal_standarized_data=normal_scaler.transform(normal_X)
normal_X=normal_standarized_data
normal_Y=normal_dataset['Outcome']
normal_X_train,normal_X_test,normal_Y_train,normal_Y_test=train_test_split(normal_X,normal_Y , test_size=0.2,stratify=normal_Y,random_state=2)
normal_classifier = SVM_classifier(learning_rate=0.001, no_of_iterations=1000, lambda_parameter = 0.01)

normal_classifier.fit(normal_X_train,normal_Y_train)


#--------------------------------------------------------------------------------------------------------------








@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/about") #static routing
def aboutProject():
    return render_template("/about.html")



@app.route("/acetone")
def predict():
    return render_template("acetone.html")

@app.route("/login")
def userLogin():
    return render_template("login.html")

@app.route("/register")
def userRegister():
    return render_template("register.html")

@app.route("/nav")
def navigation():
    return render_template("navigation.html")

@app.route("/acetone")
def predictAcetone():
    return render_template("acetone.html")

@app.route("/normalprediction")
def normalPrediction():
    return render_template("normalprediction.html")

@app.route("/device")
def iotDevice():
    return render_template("device.html")

@app.route("/predict",methods=['POST'])
def acetoneSubmit():
    if request.method=="POST":
        height=float(request.form["height"])
        acetone=float(request.form["acetone"])
        bodytemp=float(request.form["temperature"])
        age=float(request.form["age"])
        weight=float(request.form["weight"])
        BMI=float(request.form["bmi"])

      

        #------------------------------PREDICTION------------------------------------

        input_data=(acetone,bodytemp,height,weight,age,BMI)

        #Changing the input_data to numpy array
        input_data_as_numpy_array=np.asarray(input_data)

        #reshape the array as we are predicting for one instance
        input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)

        #standardize the input data
        std_data=scaler.transform(input_data_reshaped)
       

        prediction=classifier.predict(std_data)

    return render_template('result.html',user_prediction=prediction,user_acetone="Acetone: "+str(acetone),
    user_temp="Body Temperature: "+str(bodytemp),user_height="Height: "+str(height),
    user_age="Age: "+str(age),user_weight="Weight: "+str(weight),user_bmi="BMI: "+str(BMI)) 


@app.route("/predict2",methods=['POST'])
def normalSubmit():
    if request.method=="POST":
        pregnancies=float(request.form["pregnancies"])
        glucose=float(request.form["glucose"])
        bloodpressure=float(request.form["bloodpressure"])
        skinthickness=float(request.form["skinthickness"])
        insulinlevel=float(request.form["insulinlevel"])
        bmi=float(request.form["bmi"])
        pedigreefunction=float(request.form["predigreefunction"])
        age=float(request.form["age"])
        #------------------------------PREDICTION------------------------------------

        input_data=(pregnancies,glucose,bloodpressure,skinthickness,insulinlevel,bmi,pedigreefunction,age)
        print(input_data)
        input_data_as_numpy_array=np.asarray(input_data)

        #reshape the array as we are predicting for one instance
        input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)

        #standardize the input data
        std_data=normal_scaler.transform(input_data_reshaped)
       

        prediction=normal_classifier.predict(std_data)
        return render_template('result.html',user_prediction=prediction,user_acetone="Pregnancies: "+str(pregnancies),
        user_temp="Glucose: "+str(glucose),user_height="Blood Pressure: "+str(bloodpressure),
        user_age="Skin Thickness: "+str(skinthickness),user_weight="Insulin level: "+str(insulinlevel),user_bmi="BMI: "+str(bmi)
        ,seven="Pedigree Function: "+str(pedigreefunction),eight="Age: "+str(age)) 


if __name__ == '__main__':
	app.run(debug=True)



