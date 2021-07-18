weight = float(input())
height = float(input())
BMI=(weight/(height**2))

print(BMI)
if BMI < 18.5:
    print("Underweight")
elif BMI >= 18.5 and BMI <= 24.9:
	print("Normal")
elif BMI >= 25 and BMI < 30:
	print("Overweight")
else:
	print("Obesity")
