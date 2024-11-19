capitals = {
    "Bulgaria": "Sofia",
    "Germany": "Berlin",
    "France": "Paris",
    "Spain": "Madrid",
    "Italy": "Rome",
}

travel_log = {
    "Bulgaria": ["Sofia", "Plovdiv", "Varna"],
    "Germany": ["Berlin", "Hamburg", "Munich"],
    "France": {
        "cities_visited": ["Paris", "Lyon", "Marseille"],
        "total_visits": 12
    },
    "Spain": ["Madrid", "Barcelona", "Valencia"],
}

print(travel_log["Bulgaria"][1])

nested_list = ["A", "B", ["C", "D"], "E"]
print(nested_list[2][1])

print(travel_log["France"]["cities_visited"][2])