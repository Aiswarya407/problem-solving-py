# Longest Subarray With Absolute Difference Less Than or Equal to Limit

# Problem:
# Find the longest contiguous subarray such that the absolute difference between any two elements is ≤ limit.
#Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit

# Uses sliding window with max/min tracking (can use heaps or monotonic deque).
# Check for every window if max_val in that - min_val <= limit

from collections import deque

def longestSubarray(limit, nums):
        max_dq = deque()  # store elements in decreasing order
        min_dq = deque()  # store elements in increasing order
        left = 0
        max_len = 0

        # nums = [1, 3, 6, 7, 9]
        # limit = 3
 
        for right in range(len(nums)):
            while max_dq and nums[right] > max_dq[-1]:
                max_dq.pop()
            max_dq.append(nums[right])

            while min_dq and nums[right] < min_dq[-1]:
                min_dq.pop()
            min_dq.append(nums[right])

            while max_dq[0] - min_dq[0] > limit:
                if max_dq[0] == nums[left]:
                    max_dq.popleft()
                if min_dq[0] == nums[left]:
                    min_dq.popleft()
                left += 1  # shrink the window

            max_len = max(max_len, right - left + 1)

        return max_len



# nums = [10, 1, 2, 4, 7, 2]
# limit = 5

# Step 1
# right = 0, nums[right] = 10

# max_dq is empty ⇒ append 10
# → max_dq = [10]

# min_dq is empty ⇒ append 10
# → min_dq = [10]

# → max-min = 10 - 10 = 0 ≤ 5 ✅
# → Valid window → max_len = right - left + 1 = 1

# Step 2
# right = 1, nums[right] = 1

# For max_dq:
# 1 < 10, so no pop. Append at end:
# → max_dq = [10, 1]

# For min_dq:
# Remove elements > 1 → 10 > 1, so pop:
# → min_dq = [] → then append 1 → min_dq = [1]

# Now check window:
# → max_dq[0] = 10, min_dq[0] = 1
# → 10 - 1 = 9 > 5 ❌ → Invalid

# Shrink window from left:

# nums[left] = 10
# Is it equal to max_dq[0]? Yes → pop from max_dq
# → max_dq = [1]
# Is it equal to min_dq[0]? No → min_dq remains [1]
# → left = 1

# Now window:
# → nums[left:right+1] = [1]
# → max-min = 1 - 1 = 0 ≤ 5 ✅
# → Length = right - left + 1 = 1

# max_len still remains 1