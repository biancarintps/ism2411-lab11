# 1. I would use .get() when a key might be missing and I want a default value
# instead of an error like looking up optional info on a customer. I would use
# bracket notation when the key should always be there because then a KeyError
# tells me something is wrong with my data. My rule of thumb is if it's okay for
# the key to be missing use .get() and if it's not use brackets.

# 2. Building the summary dictionary reminded me of a pivot table  in
# Excel where you add up totals for each category like region. The Python version
# is more useful for large datasets because it can handle huge amounts of data
# quickly and the same code can be reused on new data instead of rebuilding the
# table by hand.



customer = {
    "name":"Bianca Rincon ",
    "email": "Bianca.rincon@gmail.com",
    "tier": "Gold",
    "ytd_spend": 500
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)

#----Exercise 2-----

customer["phone"] = "123-221-3210"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)

#----Exercise 3-----

print(customer.get("email", "no email on file"))

#print(customer["email"])

#----Exercise 4-----

for key, value in customer.items():
    print(f"{key}: {value}")

for key in customer:
    print(key)

# Difference: looping with .items() gives me both the key and the value on each pass. Looping without .items() only gives me the keys so I
# would need customer[key] to get the value.

#----Exercise 5-----

tier_discounts = {"bronze": 0, "silver": .05, "gold": .10, "platinum": .15}

discount = tier_discounts.get(customer["tier"], 0)
price = 200
final_price = price * (1 - discount)

print("Tier:", customer["tier"])
print("Discount:", f"{discount * 100:.0f}%")
print("Final price:", f"${final_price:.2f}")

#----Exercise 6-----

customers = [
    {"name": "Bianca Rincon", "tier": "platinum"},
    {"name": "Maria Lopez", "tier": "gold"},
    {"name": "James Carter", "tier": "bronze"}
]

for c in customers:
    rate = tier_discounts.get(c["tier"], 0)
    amount = 300 * rate
    print(f"{c['name']} | {c['tier']} | discount: ${amount:.2f}")

    #----Exercise 7-----

catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}

for product, info in catalog.items():
    if info["stock"] < 20:
        print(f"LOW STOCK: {product} (only {info['stock']} left)")

        #----Exercise 8-----

transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

summary = {}

for t in transactions:
    region = t["region"]
    summary[region] = summary.get(region, 0) + t["amount"]

for region in sorted(summary):
    print(f"{region}: {summary[region]}")

