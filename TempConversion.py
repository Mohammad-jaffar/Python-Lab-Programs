# function to convert fehrenheit to celsius
def Fer_To_Cel(f):
    return ( f - 32 ) * 5 / 9

# function to convert celcius to fehrenheit
def Cel_To_Fer(c):
    return ( c*9/2 ) + 32

choice = int(input("Enter 1 for Fehrenheit to celsius conversion and Enter 2 for Celsius to Fehrenheit conversion"))

if choice == 1:
    f = float(input("Enter temperature in fehrenheit : "))
    c = Fer_To_Cel(f)
    print("Tempertaure in Celsius : ",c)
elif choice == 2:
    c = float(input("Enter temperature in Celcius : "))
    f = Cel_To_Fer(c)
    print("Tempertaure in Fehrenhrit : ",f)
else:
    print("Invalid choice")