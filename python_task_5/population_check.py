cities = [("Hyderabad", 10000000),("Vijayawada", 1700000),("Visakhapatnam", 2200000),("Delhi", 32000000),("Warangal", 900000)]
result = list(filter(lambda city: city[1] > 2000000, cities))
print(result)