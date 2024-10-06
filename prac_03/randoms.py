import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# On line 1 I saw 18, the smallest number would be 5 and the largest number would be 20

# On line 2 I saw 5, the smallest number would be 3 and the largest number would be 9, line 2 could not
# have produced a 4 as it starts at 3 and goes up by 2

# On line 3 I saw 3.9003604492760755, the smallest number would be 2.5 and the largest would be 5.5

print(random.randint(1, 100))
