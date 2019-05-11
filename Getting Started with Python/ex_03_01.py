sh = input("Please enter hours: ")
sr = input("Please enter rate: ")
fh = float(sh)
fr = float(sr)
if fh > 40:
   reg = fr * fh
   otp = (fh - 40.0) * (fr * 0.5)
   xp = reg + otp
else:
   xp = fh * fr 
   print("wrong parameter")
print("Pay:",xp)