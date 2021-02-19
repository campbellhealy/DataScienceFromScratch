#counters.py

# AND Sets

from collections import Counter

c = Counter([0,1,2,3,2,4,3,4,])

# print(c)

s = set()
s.add(1)
s.add(1)
s.add(2)

x = len(s)
y = 2 in s
z = 3 in s
# print(s,x,y,z)

stopwords_list = ["a", "an", "at"]  + ["yet", "you"]
"zip" in stopwords_list     # False, but have to check every element

stopwords_set = set(stopwords_list)
"zip" in stopwords_set      # very fast to check
print(stopwords_list)

square_dict = {x: x * x for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
square_set  = {x * x for x in [1, -1]}      # {1}

print(square_dict)
print(square_set)

pairs = [(x, y)
         for x in range(10)
         for y in range(x +1,10)]   

print(pairs)

assert 1 + 1 ==3, "Its True" 