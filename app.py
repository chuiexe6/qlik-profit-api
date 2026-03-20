from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Qlik Profit Prediction API running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(silent=True) or {}

    rows = data.get("rows", [])
    predictions = []

    for row in rows:
        sales = float(row.get("Sales", 0) or 0)
        discount = float(row.get("DiscountRate", 0) or 0)
        quantity = float(row.get("Quantity", 0) or 0)
        days_to_ship = float(row.get("DaysToShip", 0) or 0)

        predicted_profit = (
            sales * 0.18
            - sales * discount * 0.55
            + quantity * 1.2
            - days_to_ship * 0.35
        )

        predictions.append({
            "PredictionRowID": row.get("PredictionRowID"),
            "PredictedProfit": round(predicted_profit, 2)
        })

    return jsonify({"predictions": predictions})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
