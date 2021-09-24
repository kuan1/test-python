# Creating a Set
st = {}
print(st)
st = set()
print(st)
st = {1, 2, 3, 3}
print(st)

# Getting Set's length
st = {1, 2, 3, 4}
print(len(st))

# Checking an Item
st = {1, 2, 3, 4}
print(1 in st)
print(11 in st)

# Adding Items to a Set
st = {1, 2, 3, 4}
st.add(5)
print(st)

# Removing items from a Set
st = {5, 1, 2, 3, 4}
print(st)
st.remove(1)
print(st)
print(st.pop())
print(st)

# Clear Items in a Set
st = {'item1', 'item2', 'item3', 'item4'}
st.clear()
print(st)

# Converting List to Set
lst = [1, 2, 3, 4, 5, 5]
print(set(lst))

# Joining Set
print({1}.union({2}))

# Finding Intersection Items
st1 = {1, 2}
st2 = {2, 3, 4}
print(st1.intersection(st2))

# Checking Subset and Super Set
st1 = {'item1', 'item2', 'item3'}
st2 = {'item2'}
print(st1.issuperset(st2))
print(st2.issubset(st1))

# Checking the Difference Between Two Set
st1 = {'item1', 'item2', 'item3'}
st2 = {'item2'}
print(st1.difference(st2)) # {'item2', 'item3'}
print(st2.difference(st1)) # set()

