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

