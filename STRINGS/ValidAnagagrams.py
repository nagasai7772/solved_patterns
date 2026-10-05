# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false


s = "anagram"
t = "nagaram"

#BRUTE FORCE APPROACH
# First, if the lengths are different, they cannot be anagrams
if len(s) != len(t):
    print(False)
else:
    

    # Take each character from s one by one
    for i in range(len(s)):
        found = False

        # Search for the current character inside t
        for j in range(len(t)):

            # Check two things:
            # 1. t[j] is the same character as s[i]
            # 2. This position in t has not already been used
            if s[i] == t[j]:

                

                # We successfully found a match
                found = True
                break

        # If we couldn't find a matching character in t,
        # then s and t are not anagrams
        if not found:
            print(False)
            break

    else:
        # If the outer loop completed successfully,
        # every character in s found a matching character in t
        print(True)


#SECOND APPROACH WITH HASHMAP

hashMap = {}

# Step 1: Count the frequency of every character in string 's'
# Example: "anagram" → {'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1}
for x in s:
    if x in hashMap:
        hashMap[x] = hashMap[x] + 1
    else:
        hashMap[x] = 1


# Step 2: Go through string 't' and decrease the count
# whenever we find a matching character.
for y in t:
    if y in hashMap:
        hashMap[y] = hashMap[y] - 1
    else:
        # If a character exists in 't' but not in 's',
        # then the two strings cannot be anagrams.
        print(False, "Characters Not Found")
        break


# Step 3: Check the final frequency of every character.
# For an anagram, every character's count must become exactly 0.
for z in hashMap:
    if hashMap[z] != 0:
        print(False,"if hashmap is not empty")
        break
else:
    # If all character counts are 0,
    # both strings contain the same characters with the same frequency.
    print(True)



#FINAL APPROACH




# Convert both strings into lists of characters
list1 = list(s)
list2 = list(t)

# Sort both lists so the same characters come into the same order
list1.sort()
list2.sort()

# Anagrams must have the same number of characters
if len(list1) != len(list2):
    print(False, "Not Anagrams")

else:
    # Assume both strings are anagrams initially
    is_anagram = True

    # Compare characters at the same index
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            is_anagram = False
            break

    # Print the final result only after checking all characters
    if is_anagram:
        print(True, "Both Are Anagrams")
    else:
        print(False, "Not Anagrams")