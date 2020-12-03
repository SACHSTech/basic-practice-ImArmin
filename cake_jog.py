km = float(input("Enter kilometers jogged: "))
cake = float(input("Enter amoung of cake slices consumed: "))

jog_km = (((225 * cake) - (100 * km)) / 100)

print("You will need to jog " + str(jog_km) + " kilometers.")