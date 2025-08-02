#Maximum Length Good Subarray Without Duplicates and Sum ≤ K

# <!-- You are given an array of integers nums and an integer k.
# A subarray is considered good if it satisfies the following two conditions:
# Sum Constraint: The sum of its elements is less than or equal to k.
# Uniqueness Constraint: All elements in the subarray are distinct (i.e., no duplicates).
# Your task is to find the maximum possible length of any subarray that is good. -->

class GoodSubarray:
    def __init__(self,nums,k):
        self.nums=nums
        self.k=k

    def Max_subarray(self):
        seen=set()
        max_length=0
        curr_sum=0
        left=0

        for right in range(len(self.nums)):
            while (self.nums[right] in seen ) or (self.nums[right]+ curr_sum > self.k):
                seen.remove(self.nums[left])
                curr_sum-=self.nums[left]
                left+=1

            seen.add(self.nums[right])
            curr_sum+=self.nums[right]
            max_length=max(max_length,(right-left+1))

        return max_length

if __name__ =='__main__':
    try:
        nums=list(map(int,input("Enter nums : ").strip().split()))
        k=int(input("Enter k : "))

        subfind=GoodSubarray(nums,k)
        result=subfind.Max_subarray()
        print("Maximum Length of Subarray : ",result)
    
    except Exception as e:
        print("Invalid Input :",e)


# @Aiswarya407 ➜ /workspaces/problem-solving-py (main) $ python3 Maximum_Length_Good_Subarray.py

# Enter nums : 1 2 3 3 4 7
# Enter k : 9
# Maximum Length of Subarray :  3

# Enter nums : 1 2 3 4 5
# Enter k : 15
# Maximum Length of Subarray :  5   