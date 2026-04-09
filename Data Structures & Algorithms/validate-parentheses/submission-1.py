class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        for ch in s:
            if(ch == '(' or ch == '[' or ch == '{'):
                st.append(ch)
            
            else:
                if len(st) == 0:
                    return False
                
                top = st[-1]
                st.pop()

                if ((ch == ')' and top != '(') or
                   (ch == ']' and top != '[') or
                   (ch == '}' and top != '{')):
                    return False;
                
        
        return len(st) == 0