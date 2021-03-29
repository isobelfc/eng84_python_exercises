# Simple program to use control flow

# check for age
age_check = True
while age_check:
    age = input("How old are you? ")
    if age.isdigit():
        age = int(age)  # casts to integer so that we can compare it
        age_check = False  # ends loop when age is correct
    else:
        print("Please enter your age in digits")

# check for driving licence
licence_check = True
while licence_check:
    driver_licence = input("Do you have a driver's licence? Y/N ")
    if driver_licence in ("Y", "N"):
        licence_check = False  # ends loop if one of expected input
    else:
        print("Please answer 'Y' or 'N'")

if age >= 18 and driver_licence == "Y":  # if user has a licence and is over 18
    print("You can vote and drive")
elif age >= 18:  # if user does not have a licence but is over 18
    print("You can vote")
elif driver_licence == "Y":  # if user has a licence but is not yet 18
    print("You can drive. You can't legally drink but your mates might have your back")
elif age >= 16:  # if user is over 16 (but under 18 and with no licence)
    print("You can't legally drink but your mates might have your back")
else:  # if user is under 16
    print("You're too young, go back to school!")
