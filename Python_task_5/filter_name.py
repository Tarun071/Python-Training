list=["tarun","raghu","sidhu","saradhi","vasu","vaishnavi"]
result = list(filter(lambda name: name[0].lower() in "aeiou",list))
print(result)