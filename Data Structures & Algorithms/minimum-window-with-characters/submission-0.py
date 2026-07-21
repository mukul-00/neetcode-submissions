class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t) > len(s):
            return ""
        
        freq = {}
        for ch in t:
            freq[ch] = freq.get(ch, 0) + 1

        count = len(freq)

        i = 0
        start = 0
        min_len = float("inf")

        for j in range(len(s)):

            if s[j] in freq:
                freq[s[j]] -= 1

                if freq[s[j]] == 0:
                    count -= 1
 
            while count == 0:

                if j - i + 1 < min_len:
                    min_len = j - i + 1
                    start = i
                
                if s[i] in freq:
                    freq[s[i]] += 1

                    if freq[s[i]] == 1:
                        count += 1

                i += 1
        
        if min_len == float("inf"):
            return ""

        return s[start:start + min_len]