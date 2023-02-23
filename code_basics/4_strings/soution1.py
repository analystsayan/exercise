# 1. Create 3 variables to store street, city and country, now create address variable to
# store entire address. Use two ways of creating this variable, one using + operator and the other using f-string.
# Now Print the address in such a way that the street, city and country prints in a separate line
street = "Malikota"
city = "Kotulpur"
country = "India"
address1 = street + '\n' + city + '\n' + country
print("My address is: ", '\n', address1)
address2 = f'{street}\n{city}\n{country}'
print(f"This is the output using f string: ", '\n', address2)
