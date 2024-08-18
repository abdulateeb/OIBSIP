weight = float(input("Enter you weight in kg: "))
height = float(input("Enter your height in meters: "))

height_in_meters = height / 100
BMI = weight / (height_in_meters**2)
print(BMI)

if  (BMI < 16):
    print ("Your weight is significantly below the healthy range."), BMI

elif (BMI >= 16 and BMI < 18.5):
    print ("Your weight is below the recommended range."), BMI
    
elif (BMI >= 25 and BMI < 30):
    print ("You're carrying a bit more weight than necessary!"), BMI
    
elif (BMI >=30):
    print ("You are obese"), BMI
