import numpy
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
# filename = 'model_waterPotability_RFC.pkl'
model = pickle.load(open("app/model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")
    # return "Hello World"

@app.route("/predict", methods = ["POST"])
def predict():
    features = [float(x) for x in request.form.values()]
    final_features = [numpy.array(features)]
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)
    if output == 0:
        return render_template("index.html", prediction_text = "Air Tidak Layak Konsumsi" , DataOut=features)
    elif output == 1:
        return render_template("index.html", prediction_text = "Air Layak Konsumsi", DataOut=features)
    else:
        return render_template("index.html", prediction_text = "Something went wrong", DataOut=features)

    
if __name__ == "__main__":
    app.run(debug=True)