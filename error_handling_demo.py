

while True:
    try:
        number = int(input("Please Enter a number: "))
        break
    except ValueError:
        print("You didn't enter a number")
    except:
        print("An unknown error occurred")

print("Thank You")
