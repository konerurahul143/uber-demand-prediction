from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# load model
xgb = joblib.load("demand_model.pkl")

@app.route("/")
def home():
    return """
    <h2>Demand Prediction</h2>
    <form action="/predict" method="post">
        Location: <input name="location"><br><br>
        Hour: <input name="hour"><br><br>
        Day of Week: <input name="dow"><br><br>
        Previous Demand: <input name="pre_demand"><br><br>
        <input type="submit" value="Predict">
    </form>
    """

@app.route("/predict", methods=["POST"])
def predict():
    if request.is_json:
        data = request.json
    else:
        data = request.form

    location = float(data["location"])
    hour = float(data["hour"])
    dow = float(data["dow"])
    pre_demand = float(data["pre_demand"])

    pred_log = xgb.predict([[location, hour, dow, pre_demand]])
    pred = np.expm1(pred_log)[0]

    # 👇 Return based on request type
    if request.is_json:
        return jsonify({"predicted_demand": float(pred)})
    else:
        return f"<h3>Predicted Demand: {pred}</h3>"

if __name__ == "__main__":
    app.run(debug=True)


print("Starting app...")