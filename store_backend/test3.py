from itertools import count
from nis import cat
from mock_data import catalog


def lower_than(price):
    count = 0
    for x in catalog:
        if x['price']< price:
            count+=1
    return count

print(lower_than(2))
print(lower_than(5))
print(lower_than(12))
print(lower_than(20))