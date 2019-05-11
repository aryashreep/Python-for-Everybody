score = input("Enter Score: ")
try:
   score=float(score)
except:
   print("Error, please enter a score number between 0.0 and 1.0")
   quit()

if score >= 0.9 :
   print("A")
elif score >= 0.8 :
   print("B")
elif score >= 0.7 :
   print("C")
elif score >= 0.6 :
   print("D")
elif score  < 0.6 :
   print("F") 
else :
   print("Your score number is not in the 0 - 1 range.")