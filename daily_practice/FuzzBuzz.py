# Daily python practice/ challenge

# Counter
FuzzBuzz_count = 0
Fuzz_count = 0
Buzz_count = 0
Regular_count = 0

# Operation
for num in range(1,21):
        if num % 3 == 0 and num % 5 == 0:
                print("FuzzBuzz")
                FuzzBuzz_count += 1 # Add 1 to FuzzBuzz tally
        elif num % 3 == 0:
                print("Fuzz")
                Fuzz_count += 1 # Add 1 to Fuzz tally
        elif num % 5 == 0:
                print("Buzz")
                Buzz_count += 1 # Add 1 to Buzz tally
        else:
                print(num)
                Regular_count += 1 # Add 1 to Regular tally

# Scores
print("--- FINAL SCORES ---")
print("FuzzBuzz showed up:", FuzzBuzz_count, "times")
print("Fuzz showed up:", Fuzz_count, "times")
print("Buzz showed up:", Buzz_count, "times")
print("Regular showed up:", Regular_count, "times")
