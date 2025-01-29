# Create a function to calculate and display the Body Mass Index (BMI) from user-provided height in meters and weight in kilograms. 
# The formula is BMI = <weight in kg> / <height in m>2. The output should be rounded to 2 digits after the decimal point.

# Example input/output:
# Enter height in meters: 1.8
# Enter weight in kilograms: 70
# The BMI is 21.60

def formula(weight : float, height : float) -> float:
    return weight / (height**2)

weight = float(input(f"Please, provide your weight(in Kg): "))
height = float(input(f"Please, porvide yor height(in m): "))

bmi = formula(weight, height)
print(f"The BMI is: {bmi:.2f}")