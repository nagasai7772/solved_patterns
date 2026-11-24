# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

nums = [1, 1, 1, 2, 2, 3]
k = 2
# Time And Space Complexity O(n)
freq1={}
result=[]
for i in nums:
    if i in freq1:
        freq1[i]+=1
    else:
        freq1[i]=1
freq2={}
max_freq=0        
for key,value in freq1.items():
    if value not in freq2:
        freq2[value]=[]
    freq2[value].append(key)
max_freq=max(freq2.keys())

while(len(result)<k and max_freq>0):
    if max_freq  in freq2:
        for num in freq2[max_freq]:
            result.append(num)
        if len(result)==k:
            break
    max_freq-=1
print("Most frequent Elements",result)    
