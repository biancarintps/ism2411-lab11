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

