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