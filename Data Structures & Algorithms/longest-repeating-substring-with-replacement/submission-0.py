class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        i = 0 # start of the window
        freq = {} # stores the ele of s
        max_freq = 0 # keep the track of max no of element in s of curr window
        mx = 0 # for max slididng window (j - i + 1)

        for j in range(len(s)):

            freq[s[j]] = freq.get(s[j], 0) + 1

            # keep check for the new element wheter they are max or not
            max_freq = max(max_freq, freq[s[j]])

            # (invalid condition) window size - most max freq = replacementCharacters that must be replaced
            while (j - i + 1) - max_freq > k:

                freq[s[i]] -= 1

                if freq[s[i]] == 0:
                    del freq[s[i]]
                
                i += 1
            
            mx = max(mx, j - i + 1)
        
        return mx
