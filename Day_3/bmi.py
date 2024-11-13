height = 1.65
weight = 85

bmi = weight / height ** 2

if bmi < 18.5:
    print("underweight")
elif bmi < 25:
    print("normal weight")
else:
    print("overweight")

