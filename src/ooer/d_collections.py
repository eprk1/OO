# in collections we have
# namedtuple() - factory function for creating tuple with named fields
# deque - list-like with fast appends and pops from either end
# ChainMap - dict like class for creating a single view of multiple mapping
# Counter - dict subclass for counting hasable objects
# OrderedDict - dict subclass that remembers the order entries were added
# defaultdict - dict subclass that calls a factory fucntion to supply missing values
# UserDict - wrapper around dictionary objects for easier dct subclassing
# UserList
# UserString


# ChainMap
from collections import *
import builtins


baseline = {"music": "bach", "art": "rembrandt"}
adjustments = {"art": "van gogh", "opera": "carmen"}
cm = list(ChainMap(adjustments, baseline))
print(cm)

pylookup = ChainMap(locals(), globals(), vars(builtins))
print(pylookup)


# Counter
print(Counter("abracadabra").most_common(3))


#deque
# append/pop from either side of the deque are O(1)
d = deque('ghi')
for e in d:
    print(e.upper())

d.append('j')
d.appendleft('f')
print(d.pop())
print(d.popleft())

d.extend('jkl')
d.extendleft('abc')
d.rotate(1)
d.rotate(-1)
d.clear()

