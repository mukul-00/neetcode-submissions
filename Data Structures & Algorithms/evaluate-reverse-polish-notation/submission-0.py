
class Solution:
    def isoperator(self, ch):
        if(ch == '+' or ch == '*' or ch == '-' or ch == '/'):
            return True
        return False

    def evalRPN(self, tokens: list[str]) -> int:
        st = []

        for token in tokens:
            if self.isoperator(token):
                # operator
                b = st.pop()
                a = st.pop()

                if token == '+':
                    st.append(a + b)
                elif token == '-':
                    st.append(a - b)
                elif token == '*':
                    st.append(a * b)
                elif token == '/':
                    st.append(int(a / b))   
            else: 
                # operand
                st.append(int(token))

        return st[-1]