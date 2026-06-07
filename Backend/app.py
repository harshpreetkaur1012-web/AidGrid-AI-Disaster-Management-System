from flask import Flask, render_template, request
from risk_agent import analyze_risk
from resource_agent import allocate_resources
from evacuation_agent import find_safe_route

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    result = None

    if request.method == "POST":

        rainfall = float(request.form["rainfall"])
        wind_speed = float(request.form["wind_speed"])
        temperature = float(request.form["temperature"])
        population = int(request.form["population"])

        risk_data = analyze_risk(rainfall, wind_speed, temperature)
        resources = allocate_resources(risk_data["severity"], population)
        route = find_safe_route(risk_data["severity"])

        result = {
            "risk": risk_data,
            "resources": resources,
            "route": route
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)