# corona ölüm risk seviyesi belirleme

age = input("Are you a cigarette addict older than 75 years old?(yes/no)..")
if age == "yes":
  age = True
else :
  age = False
chronic = input("Do you have a severe chronic disease?(yes/no)..")
if chronic == "yes":
   chronic = True
else :
  chronic = False
immune = input("Is your immune system too weak?(yes/no)..")
if immune == "yes":
  immune = True
else :
  immune = False
  
print(age and chronic or immune)
if age == True and chronic == True or immune == True :
  print("there is a risk of death")
else :
  print("there is not a risk of death")
