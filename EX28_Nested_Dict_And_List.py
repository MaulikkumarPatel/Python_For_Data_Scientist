# dict nested in dict
# travel = {
#     "India": {"visited": ["ahmedabad", "gandhinagar"], "total": 12},
#     "England": {"visited": ["Greemwich", "London Bridge"], "Total": 2}
# }

# dict nested in list
# travel = [
#     {"Contry_visit": "India",
#      "visited": ["ahmedabad", "gandhinagar"],
#      "total": 12},
#     {"Contry_visit": "England",
#      "visited": ["Greemwich", "London Bridge"],
#      "Total": 2}
# ]
# print(travel[1])
###################################


travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


def add_new_country(country, visits, cities):
    new_destination = {"country": country, "visits": visits, "cities": cities}
    travel_log.append(new_destination)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
