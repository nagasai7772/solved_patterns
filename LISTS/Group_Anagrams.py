# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# Time and Space Complexity O(n)2
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
hashMap={}
for str_val in strs:
    str_cpy=str_val
    sort_str="".join(sorted(str_cpy))
    if sort_str in hashMap:
        hashMap[sort_str].append(str_val)
    else:
        hashMap[sort_str]=[str_val]
print("group the anagrams",list(hashMap.values()))        