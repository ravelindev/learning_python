# How to calculate the velocity of an object
import math

print("welcome to the velocity calculator. Please enter the following:")
print("")

# get the Mass of the object
mass = float(input("Mass (in kilograms): "))
print(f"Mass (in kg):  {mass}")
print("")

# Get the Gravity of the object
gravity = float(input("gravity (in meters/second squared): "))
print(f"Gravity (in m/s^2 {gravity} for Earth, 24 for Jupiter): {gravity}")

# Get the time of the object
print("Enter time in seconds: ")
time = float(input("time (in seconds): "))
print(f"Time (in seconds): {time}")
print("")

# Get the Denisty of the object
print("Enter the density of the object: ")
density = float(input("density (in kg/m^3): "))
print(f"Density (in kg/m^3, {density} for air, 1000 for water): {density}")
print("")

# Get the cross sectional area of the object
print("Enter the cross sectional area of the object: ")
area = float(input("Cross sectional area (in meters^2): "))
print(f"Cross sectional area (in m^2): {area}")
print("")

# Get the Drag constant of the object
print("Enter the drag constant of the object: ")
drag_constant = float(input("Drag constant (in meters/second): "))
print(f"Drag constant ({drag_constant} for sphere, in m/s): {drag_constant}")
print("")

# Get the inner value of C
c_inner = (1/2) * density * area * drag_constant
print(f"The inner value of C is: {c_inner:.3f}")


# Get the result of the Velocity
velocity = math.sqrt(gravity * mass / c_inner) * (1-math.exp((-math.sqrt(mass * gravity * c_inner)/mass) * time))
# velocity = (c_inner * mass * gravity) / (c_inner + mass * gravity)
print(f"The velocity after {time} seconds is: {velocity:.3f} m/s")
print("")

# End of program
print("Thank you for using our program")
print("Goodbey")
print("")
