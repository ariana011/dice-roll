# ROLLING DICE GAME
import random

print("🎲 Dice game ready...")
roll_count = 0  # this variable is the counter

# Loop
while True:
    # Ask: roll the dice
    choice = input('Roll the dice? (y/n): ').lower()
# If user enters y
    if choice == 'y':
        #   Generate two random numbers
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        roll_count += 1  # this adds the increments when the user press y
        # shows both die rolls and the number of times it was rolled
        print(f'({die1}, {die2}) - Roll #{roll_count}')
# If user enters n
    elif choice == 'n':
        # Terminate
        break
# Else
    else:
        # Print invalid choice
        print('Invalid choice!')

print(f"Thanks for playing! You rolled the dice {roll_count} time(s).")
