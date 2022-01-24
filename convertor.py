# This little programm can tkae a user input in Fahrenheit to convert it to Celsius
# and vice versa.

# Fahrenheit to Celsius
print ("This program can convert Fahrenheit to Celsius and vice versa.")
print ("Please enter a temperature in Fahrenheit:")
fahrenheit = float(input())
celsius = (fahrenheit - 32) * 5/9
print (f"The temperature in Celsius is: {celsius:.1f} °C") # :.1f means that the output will be rounded to 1 decimal place
print('')

# Convert Celsius to Fahrenheit
print ("Please enter a temperature in Celsius:")
celsius = float(input())
fahrenheit = (celsius * 9/5) + 32
print (f"The temperature in Fahrenheit is: {fahrenheit:.1f} °F") # :.1f means that the output will be rounded to 1 decimal place
print('')

print ("Thank you for using this program.")
# End of programm