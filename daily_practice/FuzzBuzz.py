# Daily python practice/ challenge

# Ask the user for the start and stop numbers 
start_num = int(input("Enter the starting number: "))
end_num = int(input("Enter the ending number: "))

# Ask user if they want to limit  what prints to the screen
toggle_choice = input("Do you want to limit what print? (yes/no): ").lower()
if toggle_choice == "yes":
    print_start = int(input("Start printing from number: "))
    print_end = int(input("Stop printing at number: "))

# Counter Room
FuzzBuzz_count = 0
Fuzz_count = 0
Buzz_count = 0
Regular_count = 0

# Operation Engine
for num in range(start_num, end_num + 1):
# Check if a specific number is allowed to print
    should_print = (toggle_choice != "yes") or (print_start <= num <= print_end)
    if num % 3 == 0 and num % 5 == 0:
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
print("--- FINAL SCORES ---")
print("FuzzBuzz showed up:", FuzzBuzz_count, "times")
print("Fuzz showed up:", Fuzz_count, "times")
print("Buzz showed up:", Buzz_count, "times")
print("Regular showed up:", Regular_count, "times")
