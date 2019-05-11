sh = input("Please enter hours: ")
sr = input("Please enter rate: ")
try:
    fh = float(sh)
    fr = float(sr)
except:
    print("Please enter a number as input")
    quit()

def computepay(fh,fr):
    if fh > 40:
        reg = fr * fh
        otp = (fh - 40.0) * (fr * 0.5)
        xp = reg + otp
        return xp
    else:
        xp = fh * fr 
        return xp
    
print(computepay(fh,fr))