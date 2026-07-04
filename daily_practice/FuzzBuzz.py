# Daily python practice/ challenge

# Ask the user for the start and stop numbers
while True:
    try:
        start_num = int(input("Enter the starting number: "))
        break
    except ValueError:
        print("Please enter an integer number and try again.")
while True:
    try:
        end_num = int(input("Enter the ending number: "))
        break
    except ValueError:
        print("Please enter an integer number and try again.")

# Ask user if they want to limit  what prints to the screen
toggle_choice = input("Do you want to limit what print? (yes/no): ").lower()
if toggle_choice in ["yes", "y"]:
    while True:
        try:
            print_start = int(input("Start printing from number: "))

            if start_num <= print_start <= end_num:
                break
            else:
                print("Please enter a start number within the range.")

        except ValueError:
            print("Please enter an integer number and try again.")

    while True:
        try:
            print_end = int(input("Stop printing at number: "))

            if print_start <= print_end <= end_num:
                break
            else:
                print("Please enter a end number within the range.")

        except ValueError:
            print("Please enter an integer number and try again.")

# Counter Room
FuzzBuzz_count = 0
Fuzz_count = 0
Buzz_count = 0
Regular_count = 0
Total_count = end_num - start_num + 1

# Operation Engine
for num in range(start_num, end_num + 1):
# Check if a specific number is allowed to print
    should_print = (toggle_choice not in ["yes", "y"]) or (print_start <= num <= print_end)
    if num % 15 == 0:
        if should_print:
            print("FuzzBuzz")
        FuzzBuzz_count += 1 # Add 1 to FuzzBuzz tally
    elif num % 3 == 0:
        if should_print:
            print("Fuzz")
        Fuzz_count += 1 # Add 1 to Fuzz tally
    elif num % 5 == 0:
        if should_print:
            print("Buzz")
        Buzz_count += 1 # Add 1 to Buzz tally
    else:
        if should_print:
            print(num)
        Regular_count += 1 # Add 1 to Regular tally

# Scores
print("\n --- FINAL SCORES --- \n")
print("FuzzBuzz showed up:", FuzzBuzz_count, "times")
print("Fuzz showed up:", Fuzz_count, "times")
print("Buzz showed up:", Buzz_count, "times")
print("Regular showed up:", Regular_count, "times")
print("Total numbers processed:", Total_count)
if toggle_choice in ["yes", "y"]:
    print("Total numbers printed:", print_end - print_start + 1)
elif toggle_choice in ["no", "n"]:
    print("Total numbers printed:", Total_count)
else:
    print("Total numbers printed: N/A")

# Data Visualization
print("\n --- DATA VISUALIZATION --- \n")

max_count = max(FuzzBuzz_count, Fuzz_count, Buzz_count, Regular_count)
max_width = 25

FuzzBuzz_bar = int((FuzzBuzz_count / max_count) * max_width)
Fuzz_bar = int((Fuzz_count / max_count) * max_width)
Buzz_bar = int((Buzz_count / max_count) * max_width)
Regular_bar = int((Regular_count / max_count) * max_width)

FuzzBuzz_bar_label = f"FuzzBuzz ({FuzzBuzz_count})"
print(f"{FuzzBuzz_bar_label :<12}: {'█' * FuzzBuzz_bar} \n")

Fuzz_bar_label = f"Fuzz ({Fuzz_count})"
print(f"{Fuzz_bar_label :<12}: {'█' * Fuzz_bar} \n")

Buzz_bar_label = f"Buzz ({Buzz_count})"
print(f"{Buzz_bar_label :<12}: {'█' * Buzz_bar} \n")

Regular_bar_label = f"Regular ({Regular_count})"
print(f"{Regular_bar_label :<12}: {'█' * Regular_bar} \n")

# Statistics engine
print("--- STATISTICS --- \n")

FuzzBuzz_pct = (FuzzBuzz_count / ((end_num - start_num) +1)) * 100
Fuzz_pct = (Fuzz_count / ((end_num - start_num) +1)) * 100
Buzz_pct = (Buzz_count / ((end_num - start_num) +1)) * 100
Regular_pct = (Regular_count / Total_count) * 100

print(f"{'FuzzBuzz Percentage' :<21}: {FuzzBuzz_pct:.2f}%")
print(f"{'Fuzz Percentage' :<21}: {Fuzz_pct:.2f}%")
print(f"{'Buzz Percentage' :<21}: {Buzz_pct:.2f}%")
print(f"{'Regular Percentage' :<21}: {Regular_pct:.2f}%")
