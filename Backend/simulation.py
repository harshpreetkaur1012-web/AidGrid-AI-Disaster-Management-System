from risk_agent import analyze_risk
from resource_agent import allocate_resources
from evacuation_agent import find_safe_route


def run_simulation():

    # Example Inputs
    rainfall = 250
    wind = 70
    temperature = 27
    population = 1000

    # 1️⃣ Risk Prediction
    risk_data = analyze_risk(rainfall, wind, temperature)

    # 2️⃣ Resource Allocation
    resources = allocate_resources(
        risk_data["severity"],
        population
    )

    # 3️⃣ Evacuation Planning
    route = find_safe_route()

    print("\n=== 🌍 AID-GRID SIMULATION ===")
    print("Risk Data:", risk_data)
    print("Resources Allocated:", resources)
    print("Evacuation Route:", route)


if __name__ == "__main__":
    run_simulation()