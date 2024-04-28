numbers = [0,1,2,3,4,5,6,7]
even = [i for i in numbers if i%2==0]
print(even)
sqrs = [i*i for i in numbers]
print(sqrs)
cities = ["mumbai","new york","paris"]
countries = ["india","usa","france"]
z = zip(cities,countries)
# zip forms a tuple of tuples, has iterator on the next
d = {city:country for city,country in z}
print(d) # dictionary with key as city and value as country.