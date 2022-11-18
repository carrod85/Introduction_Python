def cat(bmi):
    if bmi <= 18.5:
        print("Underweight")
    elif 18.5 < bmi < 25:
        print("Normal weight")
    elif 25 <= bmi < 30:
        print("overweight")
    else:
        print("Obesity")

cat(1)
