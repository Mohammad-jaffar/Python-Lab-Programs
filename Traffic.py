# WAP to display traffic signal using match condition in which the user have to give the input.
def Traffic(Signal):
    match Signal:
        case "red":
            print("STOP")
        case "yellow":
            print("Wait")
        case "green":
            print("Go")
        case _:
            print("Enter a valid aoutput")

signal = str(input("Enter the signal : "))

Traffic(signal)
