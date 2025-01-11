def convert_cel_to_far(c):
    return round(c * 9.0 / 5.0 + 32.0, 2)

def convert_far_to_cel(fa):
    return round((fa - 32.0) * 5.0 / 9.0, 2)

fa = float(input("Enter temperature in degrees F: "))
print(f"{fa} degrees F = {convert_far_to_cel(fa)} degrees C")

c = float(input("Enter temperature in degrees C: "))
print(f"{c} degrees C = {convert_cel_to_far(c)} degrees F")