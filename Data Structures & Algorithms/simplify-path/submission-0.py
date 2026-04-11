#  Symbol	         Meaning
#    /	        separator between folders
#   name	    go inside that folder
#    ..	        go one folder back
#    .	        stay in same folder
#    //	        same as / (extra slash, ignore)

class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split('/')   # break path into pieces
        stack = []

        for part in parts:
            if part == '' or part == '.':
                continue
            elif part == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(part)

        return '/' + '/'.join(stack)

        
# class Solution:
#     def simplifyPath(self, path: str) -> str:
#         st = []
#         curr = ""

#         for ch in path + "/":
#             if ch == '/':
#                 if curr == '..':
#                     if st :
#                         st.pop()
#                 elif curr != "" and curr != '.':
#                     st.append(curr)
                
#                 curr = ""

#             else:
#                 curr += ch
        
#         return "/" + "/".join(st)

        