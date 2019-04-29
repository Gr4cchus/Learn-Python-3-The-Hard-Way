team1 = 1
team2 = 2

print(f"You are in team {team1}.")  # format variables into printing

your_options = "{} {}"
print("What do you do?", your_options.format("select", "drop")) # using format function to pass variables.

days = "mon tue wed"
months = "\nApr\nMay\nJun\n"  # using escape characters

print(f"What day is it? {days}")
print(f"Which month {months} do you", your_options.format("select", "or drop?"), end=" ")

selected_month = input()

print(f"You choose {selected_month}.", )