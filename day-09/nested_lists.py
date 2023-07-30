capitals = {
    "France": "Paris",
    "`Germany": "Berlin"
}

travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Studgart"], "total_visits": 12}
}

print(travel_log)

# nesting dictionary in a list
travel_log = [
    {"country": "France", "cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    {"country": "Germany", "cities_visited": ["Berlin", "Hamburg", "Studgart"], "total_visits": 12}
]
print(travel_log)
