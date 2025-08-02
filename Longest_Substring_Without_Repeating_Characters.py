# Longest Substring Without Repeating Characters

# Problem:
# Given a string, find the length of the longest substring without repeating characters.

# [Sliding window + set idea, but with characters instead of numbers.]

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

class Substrings:
    def __init__(self,s):
        self.s=s

    def Longest_substr(self):
        seen=set()
        max_length=0
        left=0
        start=0

        for right in range(len(self.s)):
            
            while self.s[right] in seen:
                seen.remove(self.s[left])
                left+=1

            seen.add(self.s[right])

           # max_length=max(max_length,right-left+1)
           # If only LEngth is needed
           # if we want to return substr we will have to check max length and then update start index 

            if (right - left+ 1 )> max_length:
                max_length= right - left + 1
                start = left
            
            longest=self.s[start : start + max_length]



        return max_length, longest
    
if __name__=='__main__':

        s=input("Enter s : ").strip()
        substr=Substrings(s)
        result,longest=substr.Longest_substr()
        print("Max Length : ",result)
        print("Longest substring : ",longest)


# @Aiswarya407 ➜ /workspaces/problem-solving-py (main) $ python3 Longest_Substring_Without_Repeating_Characters.py
# Enter s : abcabcbb
# Max Length :  3
# Longest substring :  abc