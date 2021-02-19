# regex.py

import re

re_examples = [                        # All of these are True, because
    not re.match("a", "cat"),              #  'cat' doesn't start with 'a'
    re.search("a", "cat"),                 #  'cat' has an 'a' in it
    not re.search("c", "dog"),             #  'dog' doesn't have a 'c' in it.
    3 == len(re.split("[ab]", "carbs")),   #  Split on a or b to ['c','r','s'].
    "R-D-" == re.sub("[0-9]", "-", "R2D2") #  Replace digits with dashes.
    ]
assert all(re_examples), "all the regex examples should be True"

"""One important thing to note is that re.match checks whether the beginning of a string matches a regular expression,
 while re.search checks whether any part of a string matches a regular expression. 
 At some point you will mix these two up and it will cause you grief.
"""