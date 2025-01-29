# Write functions that:
# Makes basic math calculations,
# Converts Celsius from faranheit.
# Calculate average speed in meters/sec. Distance is given in Km and time in hours.
# Test all the functions. 
# Prints should be clear and precise.


def num_addition (num_1 : int, num_2 : int) -> int:
    return num_1 + num_2
def num_subtraction(num_1 : int, num_2 : int) -> int:
    return num_1 - num_2
def num_multiplication(num_1 : int, num_2 : int) -> int:
    return num_1 * num_2
def temp(farenheit : float) -> float: 
    return  (farenheit - 32) * 5 / 9
def avr_speed(speed_kmh : int) -> int:
    return speed_kmh * 5 / 18

total_sum = num_addition(7, 2)
difference = num_subtraction(1,5)
product = num_multiplication(2, 3)
celcijus = temp(25)
ave_speed = avr_speed(100)

print("Sum:", total_sum)
print("Diference:", difference)
print("Multiplication:", product)
print("Temperature in Celcius:", celcijus)
print("Average speed:", ave_speed, "m/s")