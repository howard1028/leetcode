/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* reverse_list(struct ListNode* head){
    struct ListNode* prev_node = NULL;
    struct ListNode* curr_node = head;
    struct ListNode* next_node = NULL;
    while (curr_node != NULL){
        next_node = curr_node->next;
        curr_node->next = prev_node;
        prev_node = curr_node;
        curr_node = next_node;
    }
    return prev_node;
}

bool isPalindrome(struct ListNode* head) {
    if (head == NULL || head->next == NULL){
        return true;
    }
    struct ListNode* slow = head;
    struct ListNode* fast = head;
    while (fast != NULL && fast->next != NULL){
        slow = slow->next;
        fast = fast->next->next;
    }
    struct ListNode* first_half = head;
    struct ListNode* second_half = reverse_list(slow); // 和first_half一樣長或少一個node
    while (second_half != NULL){
        if (first_half->val != second_half->val){
            return false;
        }
        first_half = first_half->next;
        second_half = second_half->next;
    }
    return true;
}