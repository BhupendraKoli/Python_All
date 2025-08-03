# 1. Count the occurrences of a specific character in a string
s = "programming"
char = 'm'
count = 0
for c in s:
    if c == char:
        count += 1
print("1. Occurrences of", char, ":", count)

# 2. Check if a string is a palindrome
s = "madam"
rev = s[::-1]
print("2. Is palindrome:", s == rev)

# 3. Check if two strings are anagrams of each other
s1 = "listen"
s2 = "silent"
print("3. Are anagrams:", sorted(s1) == sorted(s2))

# 4. Reverse a string
s = "hello"
rev = ""
for ch in s:
    rev = ch + rev
print("4. Reversed string:", rev)

# 5. Remove duplicate characters from a string
s = "banana"
result = ""
for ch in s:
    if ch not in result:
        result += ch
print("5. Without duplicates:", result)

# 6. Check if a string contains only digits
s = "123456"
print("6. Contains only digits:", s.isdigit())

# 7. Remove whitespace from a string
s = "hello world"
result = ""
for ch in s:
    if ch != " ":
        result += ch
print("7. Without whitespace:", result)

# 8. Convert a string to title case
s = "hello world from python"
words = s.split()
title = ""
for word in words:
    title += word[0].upper() + word[1:] + " "
print("8. Title case:", title.strip())

# 9. Find the longest word in a string
s = "Python is an amazing programming language"
words = s.split()
longest = words[0]
for word in words:
    if len(word) > len(longest):
        longest = word
print("9. Longest word:", longest)

# 10. Count vowels and consonants
s = "hello world"
vowels = "aeiouAEIOU"
v = c = 0
for ch in s:
    if ch.isalpha():
        if ch in vowels:
            v += 1
        else:
            c += 1
print("10. Vowels:", v, "Consonants:", c)

# 11. Check if a string contains only uppercase letters
s = "HELLO"
print("11. Only uppercase:", s.isupper())

# 12. Find the first non-repeated character
s = "aabbcdeff"
for ch in s:
    if s.count(ch) == 1:
        print("12. First non-repeated character:", ch)
        break

# 13. Capitalize the first letter of each word
s = "python programming language"
words = s.split()
capitalized = ""
for word in words:
    capitalized += word[0].upper() + word[1:] + " "
print("13. Capitalized words:", capitalized.strip())

# 14. Find the index of a substring
s = "programming"
sub = "gram"
print("14. Index of substring:", s.find(sub))

# 15. Check if a string is a valid palindrome ignoring non-alphanumeric
s = "A man, a plan, a canal: Panama"
filtered = ""
for ch in s:
    if ch.isalnum():
        filtered += ch.lower()
print("15. Valid palindrome (ignore non-alphanum):", filtered == filtered[::-1])

# 16. Find the longest common prefix among strings
strs = ["flower", "flow", "flight"]
prefix = strs[0]
for word in strs[1:]:
    while not word.startswith(prefix):
        prefix = prefix[:-1]
print("16. Longest common prefix:", prefix)

# 17. Find all substrings of a string
s = "abc"
print("17. All substrings:")
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        print(s[i:j])

# 18. String interpolation
name = "Alice"
age = 25
print(f"18. My name is {name} and I am {age} years old.")

# 19. Reverse words in a string (no built-in reverse)
s = "hello world python"
words = s.split()
rev_words = ""
for i in range(len(words)-1, -1, -1):
    rev_words += words[i] + " "
print("19. Words reversed:", rev_words.strip())

# 20. Check if a string is a rotation of another string
s1 = "abcde"
s2 = "deabc"
print("20. Is rotation:", s2 in s1 + s1)

# 21. String compression (aabbbcccc -> a2b3c4)
s = "aabbbcccc"
result = ""
count = 1
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        count += 1
    else:
        result += s[i-1] + str(count)
        count = 1
result += s[-1] + str(count)
print("21. Compressed string:", result)

# 22. Longest palindromic substring
s = "babad"
longest = ""
for i in range(len(s)):
    for j in range(i, len(s)):
        sub = s[i:j+1]
        if sub == sub[::-1] and len(sub) > len(longest):
            longest = sub
print("22. Longest palindromic substring:", longest)

# 23. Shortest palindrome by adding chars to front
s = "aacecaaa"
for i in range(len(s)):
    if s[i:] == s[i:][::-1]:
        shortest = s[:i][::-1] + s
        break
print("23. Shortest palindrome:", shortest)

# 24. Generate all permutations of a string
from itertools import permutations
s = "abc"
perm = permutations(s)
print("24. Permutations:")
for p in perm:
    print("".join(p))

# 25. KMP string matching
text = "abxabcabcaby"
pattern = "abcaby"
# Preprocess
lps = [0]*len(pattern)
length = 0
i = 1
while i < len(pattern):
    if pattern[i] == pattern[length]:
        length += 1
        lps[i] = length
        i += 1
    else:
        if length != 0:
            length = lps[length-1]
        else:
            lps[i] = 0
            i += 1
# Search
i = j = 0
found = False
while i < len(text):
    if text[i] == pattern[j]:
        i += 1
        j += 1
    if j == len(pattern):
        found = True
        break
    elif i < len(text) and text[i] != pattern[j]:
        if j != 0:
            j = lps[j-1]
        else:
            i += 1
print("25. KMP match found:", found)

# 26. Minimum window with all characters
from collections import Counter
s = "ADOBECODEBANC"
t = "ABC"
countT = Counter(t)
window = {}
have = need = len(countT)
res = ""
l = 0
min_len = float('inf')
for r in range(len(s)):
    window[s[r]] = window.get(s[r], 0) + 1
    if s[r] in countT and window[s[r]] == countT[s[r]]:
        have -= 1
    while have == 0:
        if (r - l + 1) < min_len:
            min_len = r - l + 1
            res = s[l:r+1]
        window[s[l]] -= 1
        if s[l] in countT and window[s[l]] < countT[s[l]]:
            have += 1
        l += 1
print("26. Min window:", res)

# 27. Minimum operations to convert one string to another
s1 = "horse"
s2 = "ros"
m, n = len(s1), len(s2)
dp = [[0]*(n+1) for _ in range(m+1)]
for i in range(m+1):
    for j in range(n+1):
        if i == 0:
            dp[i][j] = j
        elif j == 0:
            dp[i][j] = i
        elif s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
print("27. Edit distance:", dp[m][n])

# 28. Check if two strings are one edit away
s1 = "pale"
s2 = "ple"
if abs(len(s1) - len(s2)) > 1:
    print("28. One edit away: False")
else:
    i = j = 0
    found = False
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if found:
                print("28. One edit away: False")
                break
            found = True
            if len(s1) > len(s2):
                i += 1
            elif len(s1) < len(s2):
                j += 1
            else:
                i += 1
                j += 1
        else:
            i += 1
            j += 1
    else:
        print("28. One edit away: True")

# 29. Longest substring without repeating characters
s = "abcabcbb"
start = 0
max_len = 0
used = {}
for i in range(len(s)):
    if s[i] in used and start <= used[s[i]]:
        start = used[s[i]] + 1
    else:
        max_len = max(max_len, i - start + 1)
    used[s[i]] = i
print("29. Longest substring without repeat:", max_len)

# 30. Check if a string is a rotation of another using suffix array logic
s1 = "rotation"
s2 = "tationro"
print("30. Is rotation (suffix logic):", s2 in s1 + s1)
