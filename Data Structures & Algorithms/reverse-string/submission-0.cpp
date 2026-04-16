class Solution {
public:
    void reverseString(vector<char>& s) {
        int start = 0; // index from the start
        int end = s.size() - 1; // index from the last

        while (start < end){
            swap(s[start++], s[end--]);
        }
    }
};