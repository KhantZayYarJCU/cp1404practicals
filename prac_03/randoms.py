"""
CP1404/CP5632 - Prac 03 - Randoms
Student Name  - Khant Zay Yar
Student ID    - 14052564
"""

import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# What did you see on line 1?
# What was the smallest number you could have seen, what was the largest?
# The smallest number was 8 and the largest number was 20.

# What did you see on line 2?
# What was the smallest number you could have seen, what was the largest?
# Could line 2 have produced a 4?
# The smallest number was 3 and the largest number was 5.

# What did you see on line 3?
# What was the smallest number you could have seen, what was the largest?
# The smallest number was 3.4 and the largest number was 3.7.

import random

random_number = random.randint(1, 100)
print(random_number)