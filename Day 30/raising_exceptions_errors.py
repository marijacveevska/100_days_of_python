# BODY FAT CALCULATOR

height = float(input("Height: "))   #(m)
weight = int(input("Weight: "))     #(kg)
age = int(input("Age: "))
sex = (input("Sex: ")).lower()

if height > 3:
    raise ValueError("Human height should not me over 3 meters.")

if sex == "female":
    sex = 0
elif sex == "male":
    sex = 1
else:
    print("Choose male or female only")

bmi= weight / height**2
print(f"bmi: {bmi}")

body_fat=(1.2 * bmi) + (0.23 * age) - (10.8 * sex) - 5.4
print(f"body fat: {body_fat}")