Height=float(input("Enter your height in cm:"))
Weight=float(input("Enter your weight in kg:"))

Height=Height/100
BMI=Weight/(Height*Height)
print("Your body mass index is:",BMI)
if (BMI >0):
  if (BMI<=16):
       print("You are severly underweight")
  elif(BMI<=18.5):
       print("You are underweight")
  elif(BMI<=25):
       print("You are Healthy")
  elif(BMI<=30):
      print("You are Overweight")
  else:print("You are severely overweight")
else:("Enter valid details")
      
