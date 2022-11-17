travel_log = {
    "France":  {"cities_visited": ["Paris", "Lille", "Dijon"],
                "total_visits": 12},
    "Germany": {"cities_visited": ["Bitburg", "Hamburg", "Berlin"],
                "total_visits": 30}
}

print(travel_log["France"]["cities_visited"][1])

travel_log = [
    {"country": "France",
     "cities_visited": ["Paris", "Lille", "Dijon"],
     "total_visits": 12},

    {"country": "Germany",
     "cities_visited": ["Bitburg", "Hamburg", "Berlin"],
     "total_visits": 30}
]

print(travel_log[1]["country"])
