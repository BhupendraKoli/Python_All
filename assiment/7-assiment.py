# 1. Given a list L = [1, [2, 3], (4, 5), {6, 7}],
# perform slicing on L to extract only the tuple and set,
# then join them into a single set.
L = [1, [2, 3], (4, 5), {6, 7}]
part = L[2:4]
result = set(part[0]).union(part[1])
print( result)

# 2. You have a tuple T = ('a', ['b', 'c'], ('d', 'e')).
# Modify the list inside the tuple to add 'z' at index 1
# and return the updated tuple.
T = ('a', ['b', 'c'], ('d', 'e'))
T[1][1] = 'z'
print( T)

# 3. Given S1 = {1, 2, 3, 4} and S2 = {3, 4, 5, 6},
# perform an operation that results in {1, 2, 5, 6}
# but using only set methods (no operators like |, -, etc.).
S1 = {1, 2, 3, 4}
S2 = {3, 4, 5, 6}
s1_copy = S1.copy()
s1_copy.symmetric_difference_update(S2)
print( s1_copy)

# 4. Given L = ['a', 'b', 'c', 'd', 'e'],
# slice this list to obtain every second element,
# then join them into a single string with "*" as the separator.
L = ['a', 'b', 'c', 'd', 'e']
sliced = L[::2]
print( "*".join(sliced))

# 5. Given T = (10, 20, [30, 40], (50, 60)),
# modify the list inside the tuple by replacing 30 with 300,
# then return the modified tuple.
T = (10, 20, [30, 40], (50, 60))
T[2][0] = 300
print( T)

# 6. You have a nested tuple T = (1, (2, 3), [4, 5], {6, 7}).
# Extract the list, change the second element to 50,
# and reconstruct the tuple with the modified list.
T = (1, (2, 3), [4, 5], {6, 7})
T[2][1] = 50
print( T)

# 7. Given S = {10, 20, 30, 40} and T = (30, 40, 50, 60),
# convert T to a set and perform an operation that results in {10, 20}.
S = {10, 20, 30, 40}
T2 = (30, 40, 50, 60)
S_copy = S.copy()
S_copy.difference_update(set(T2))
print( S_copy)

# 8. Given a list L = [1, [2, 3, 4], 5, (6, 7)],
# extract the inner list and replace 3 with 'X',
# then return the modified original list.
L = [1, [2, 3, 4], 5, (6, 7)]
L[1][1] = 'X'
print( L)

# 9. Given T = ('A', 'B', ['C', 'D'], 'E'),
# modify the list inside the tuple by appending 'Z',
# then return the updated tuple.
T = ('A', 'B', ['C', 'D'], 'E')
T[2].append('Z')
print( T)

# 10. You have L1 = ['x', 'y', 'z'] and L2 = ['a', 'b', 'c'].
# Use a function to join these two lists into a single
# comma-separated string without using loops.
L1 = ['x', 'y', 'z']
L2 = ['a', 'b', 'c']
combined = L1 + L2
print( ",".join(combined))

# 11. Given S = {100, 200, 300} and T = (400, 500),
# merge these two into a single set without converting T into a set explicitly.
S = {100, 200, 300}
T = (400, 500)
for x in T:
    S.add(x)
print( S)

# 12. Given T = (1, 2, [3, 4], 5),
# remove the last element of the list inside the tuple,
# then return the modified tuple.
T = (1, 2, [3, 4], 5)
del T[2][-1]
print( T)

# 13. Given L = ['apple', 'banana', 'cherry', 'date'],
# slice it to extract only ['banana', 'cherry'],
# then join them into a string using '-' as a separator.
L = ['apple', 'banana', 'cherry', 'date']
sliced = L[1:3]
print( "-".join(sliced))

# 14. Given S = {1, 2, 3} and T = (4, 5, 6),
# merge them into a single tuple where the set elements appear first.
S = {1, 2, 3}
T = (4, 5, 6)
merged = tuple(S) + T
print( merged)

# 15. Given L = [10, 20, 30, 40, 50],
# extract every alternate element starting from index 1,
# then join them into a string separated by "@".
L = [10, 20, 30, 40, 50]
sliced = L[1::2]
print( "@".join(str(x) for x in sliced))
