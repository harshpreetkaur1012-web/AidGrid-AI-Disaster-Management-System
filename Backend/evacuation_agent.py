import networkx as nx

def find_safe_route(severity):

    if severity == "Low":
        return {
            "route_name": "Route A",
            "path": ["Local Road", "Main Street", "Community Shelter"],
            "distance": "2 km",
            "estimated_time": "10 minutes"
        }

    elif severity == "Moderate":
        return {
            "route_name": "Route B",
            "path": ["Highway Link", "City Bypass", "Central Relief Camp"],
            "distance": "5 km",
            "estimated_time": "20 minutes"
        }

    else:  # High
        return {
            "route_name": "Emergency Route"
        }
    