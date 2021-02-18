# randomness.py
""" Seeding ensure consistent random number choices """
import random

random.seed(10)  # this ensures we get the same results every time

# four_uniform_randoms = [random.random() for _ in range(4)]

# random.seed(10)         # set the seed to 10
# print(random.random())  # 0.57140259469
# random.seed(10)         # reset the seed to 10
# print(random.random())  # 0.57140259469 again

# random.randrange(10)    # choose randomly from range(10) = [0, 1, ..., 9]
# print(random.randrange(10))
# random.randrange(3, 6)  # choose randomly from range(3, 6) = [3, 4, 5]
# print(random.randrange(3, 6))  # choose randomly from range(3, 6) = [3, 4, 5]
# print(random.randrange(3, 6))  # choose randomly from range(3, 6) = [3, 4, 5]
# print(random.randrange(3, 6))  # choose randomly from range(3, 6) = [3, 4, 5]
# print(random.randrange(3, 6))  # choose randomly from range(3, 6) = [3, 4, 5]
# print(random.randrange(3, 6))  # choose randomly from range(3, 6) = [3, 4, 5]
# print(random.randrange(3, 6))  # choose randomly from range(3, 6) = [3, 4, 5]

the_numbers = [1,2,3,4,5,6,7,8,9]
random.shuffle(the_numbers)
# print(the_numbers)
# random.shuffle(the_numbers)
# print(the_numbers)
# random.shuffle(the_numbers)
# print(the_numbers)
# random.shuffle(the_numbers)
# print(the_numbers)

more_numbers = range(49)
winners = random.sample(more_numbers,6)
print(winners)