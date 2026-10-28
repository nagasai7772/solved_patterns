# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.


height = [1,8,6,2,5,4,8,3,7]

left=0
right=len(height)-1
max_area=0
while left<right:
    width=right-left
    min_height=min(height[left],height[right])
    current_area=min_height*width
    max_area=max(current_area,max_area)
    if height[left]<height[right]:
        left+=1
    else:
        right-=1
print("Max Area",max_area)            
