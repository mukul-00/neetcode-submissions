class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # below 3 line can be written as mp = counter(s1)
        mp = {}
        for ch in s1:
            mp[ch] = mp.get(ch, 0) + 1
        
        count = len(mp)

        i = 0

        for j in range(len(s2)):

            if s2[j] in mp:
                mp[s2[j]] -= 1

                if mp[s2[j]] == 0:
                    count -= 1
            
            if j - i + 1 == len(s1): # window size is now equal to size of s1

                if count == 0:
                    return True

                if s2[i] in mp:
                    
                    if mp[s2[i]] == 0:
                        count += 1

                    mp[s2[i]] += 1

                i += 1
            
        return False

#====================================================
# normal fixed size sliding window
# mp = {}
# count = len(mp)
# i = 0

# for j in range(len(arr)):
#     cal for arr[j] # like we can decrease the count and value in dict

#     if j - i + 1 == k:
#         # get answer

#         # remove arr[i] or decrease count

#         i += 1

# return ans
            