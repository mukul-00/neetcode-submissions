class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            # store as: length + '#' + actual string
            res += str(len(s)) + "#" + s
        
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0  # pointer to traverse the encoded string

        while i < len(s):

            j = i  # start from i to find '#'

            # move j until we hit '#'
            while s[j] != '#':
                j += 1
        
            # substring s[i:j] gives the length of next word
            length = int(s[i:j])

            # extract the word using the length
            # (start right after '#' and take 'length' chars)
            word = s[j + 1 : j + 1 + length]
            res.append(word)

            # move i to the start of next encoded part
            i = j + 1 + length
        
        return res