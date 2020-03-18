heroes = {
    "Superman": "Clark Kent",
    "Batman": "Bruce wayne",

}

print("Length", len(heroes))
print(heroes["Superman"])
heroes["Flash"] = "Barry Allan"
heroes["Flash"] = "Barry Allen"

print(list(heroes.items()))
print(list(heroes.keys()))
print(list(heroes.values()))


del heroes["Flash"]

print(heroes.pop("Batman"))
print("Superman" in heroes)

for k in heroes:
    print(k)

for v in heroes.values():
    print(v)

d1 = {"name": "Bread", "price": 0.88}
print("%(name)s costs $%(price).2f" % d1)
