password = "23423c"

if len(password) < 6:
    print("Password is Week")
elif len(password) <= 10:
    print("Password is Medium")
else:
    print("Password is Strong")
