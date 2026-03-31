/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    void reorderList(ListNode* head) {
        if (head == NULL || head->next == NULL) return;

        //Find middle
        ListNode* slow = head;
        ListNode* fast = head;

        while (fast->next != NULL && fast->next->next != NULL) {
            slow = slow->next;
            fast = fast->next->next;
        }

        //Reverse second half
        ListNode* curr = slow->next;
        slow->next = NULL;

        ListNode* prev = NULL;
        while (curr) {
            ListNode* next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }

        // Merge
        ListNode* first = head;
        slow->next = NULL;
        ListNode* second = prev;

        while (second != NULL) {
            ListNode* next1 = first->next;
            ListNode* next2 = second->next;

            first->next = second;   // attach from second list
            second->next = next1;   // reconnect back to first

            first = next1;
            second = next2;
        }
    }
};
