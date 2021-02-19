from statistics import largest_value, smallest_value, second_largest_value, second_smallest_value
from statistics import mean, median, quantile, mode, data_range, interquartile_range
from statistics import num_friends, num_points, co
import scratch

# # friend_counts
# assert num_points == 204

# assert largest_value == 100
# assert smallest_value == 1

# assert second_smallest_value == 1
# assert second_largest_value == 49

# assert 7.3333 < mean(num_friends) < 7.3334

# assert median([1, 10, 2, 9, 5]) == 5
# assert median([1, 9, 2, 10]) == (2 + 9) / 2

# assert quantile(num_friends, 0.10) == 1
# assert quantile(num_friends, 0.25) == 3
# assert quantile(num_friends, 0.75) == 9
# assert quantile(num_friends, 0.90) == 13

# assert median(num_friends) == 6

# assert set(mode(num_friends)) == {1, 6}

# assert data_range(num_friends) == 99

# assert 81.54 < variance(num_friends) < 81.55

# assert 9.02 < standard_deviation(num_friends) < 9.04

# assert interquartile_range(num_friends) == 6

assert 22.42 < covariance(num_friends, daily_minutes) < 22.43
assert 22.42 / 60 < covariance(num_friends, daily_hours) < 22.43 / 60

assert 0.24 < correlation(num_friends, daily_minutes) < 0.25
assert 0.24 < correlation(num_friends, daily_hours) < 0.25

assert 0.57 < correlation(num_friends_good, daily_minutes_good) < 0.58
assert 0.57 < correlationn(num_friends_good, daily_hours_good) < 0.58