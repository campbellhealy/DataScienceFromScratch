# dicts.py

empty_dict = {}                     # Pythonic
empty_dict2 = dict()                # less Pythonic
grades = {"Joel": 80, "Tim": 95}    # dictionary literal

joels_grade = grades["Joel"]        # equals 80 But you’ll get a KeyError if you ask for a key that’s not in the dictionary: 

print(joels_grade)

try:
    kates_grade = grades["Kate"]

except KeyError:
    print("no grade for Kate!") 

# You can check for the existence of a key using in: 
joel_has_grade = "Joel" in grades     # True
kate_has_grade = "Kate" in grades     # False This membership check is fast even for large dictionaries. Dictionaries have a get method that returns a default value (instead of raising an exception) when you look up a key that’s not in the dictionary: joels_grade = grades.get("Joel", 0)   # equals 80

print(joel_has_grade)
print(kate_has_grade)

kates_grade = grades.get("Kate", 0)   # equals 0
no_ones_grade = grades.get("No One")  # default is None You can assign key/value pairs using the same square brackets: grades["Tim"] = 99                    # replaces the old value

print(kates_grade)
print(no_ones_grade)

grades["Kate"] = 100                  # adds a third entry
print(grades)

num_students = len(grades)            # equals 3 As you saw in Chapter 1, you can use dictionaries to represent structured data: 
tweet = {
    "user" : "joelgrus",
    "text" : "Data Science is Awesome",
    "retweet_count" : 100,
    "hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}

print(num_students)
print(tweet.keys)
print(tweet.keys())