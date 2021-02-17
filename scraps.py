# friendships.py

from collections import Counter, defaultdict
from rawData import users, friendship_pairs, salaries_and_tenures

# Initialize the dict with an empty list for each user id:
friendships = {user["id"]: [] for user in users}


# And loop over the friendship pairs to populate it:
for i, j in friendship_pairs:
    friendships[i].append(j)  # Add j as a friend of user i
    friendships[j].append(i)  # Add i as a friend of user j

# print(friendships)

def number_of_friends(user):
    """How many friends does _user_ have?"""
    user_id = user["id"]
    friend_ids = friendships[user_id]
    return len(friend_ids)

total_connections = sum(number_of_friends(user)
                        for user in users)        # 24

num_users = len(users)                            # length of the users list
avg_connections = total_connections / num_users   # 24 / 10 == 2.4

# Create a list (user_id, number_of_friends).
num_friends_by_id = [(user["id"], number_of_friends(user))
                     for user in users]
num_friends_by_id.sort(key=lambda id_and_friends: id_and_friends[1], reverse =True)


# print('Number of users: ',num_users)
# print('Average Connnections: ', avg_connections)
# print('Number of friends for each user: ', num_friends_by_id)

def foaf_ids_bad(user):
    """foaf is short for "friend of a friend" """
    return [foaf_id
            for friend_id in friendships[user["id"]]
            for foaf_id in friendships[friend_id]]

# print(f'Friends of User 0: ',friendships[0])  # [1, 2]
# print(f'Friends of User 1: ',friendships[1])  # [0, 2, 3]
# print(f'Friends of User 2: ',friendships[2])  # [0, 1, 3]

def friends_of_friends(user):
    user_id = user["id"]
    return Counter(
        foaf_id
    for friend_id in friendships[user_id]     # For each of my friends,
            for foaf_id in friendships[friend_id]     # find their friends
            if foaf_id != user_id                     # who aren't me
            and foaf_id not in friendships[user_id]   # and aren't my friends.
        )

# print(f'Friend of Friend {users[4]}', friends_of_friends(users[4]))               # Counter({0: 2, 5: 1})



def data_scientists_who_like(target_interest):
    """Find the ids of all users who like the target interest."""
    return [user_id
            # for user_id, user_interest in interests:
            #     if user_interest == target_interest]

# Keys are interests, values are lists of user_ids with that interest
# user_ids_by_interest = defaultdict(list)

# for user_id, interest in interests:
#     user_ids_by_interest[interest].append(user_id)

# Keys are user_ids, values are lists of interests for that user_id.
# interests_by_user_id = defaultdict(list)

for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)

def most_common_interests_with(user):
    return Counter(
        interested_user_id
        for interest in interests_by_user_id[user["id"]]
        for interested_user_id in user_ids_by_interest[interest]
        if interested_user_id != user["id"]
    )

# Keys are years, values are lists of the salaries for each tenure.
salary_by_tenure = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)

# Keys are years, each value is average salary for that tenure.
average_salary_by_tenure = {
    tenure: sum(salaries) / len(salaries)
    for tenure, salaries in salary_by_tenure.items()
}

def tenure_bucket(tenure):
    if tenure < 2:
        return "less than two"
    elif tenure < 5:
        return "between two and five"
    else:
        return "more than five"

# Keys are tenure buckets, values are lists of salaries for that bucket.
salary_by_tenure_bucket = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary) # And finally compute the average salary for each group: 
    # Keys are tenure buckets, values are average salary for that bucket.
average_salary_by_bucket = {
  tenure_bucket: sum(salaries) / len(salaries)
  for tenure_bucket, salaries in salary_by_tenure_bucket.items()
}
 