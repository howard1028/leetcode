/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head) {
    // struct ListNode *prev_node = NULL;
    // struct ListNode *curr_node = head;
    // struct ListNode *next_node = NULL;

    // while (curr_node != NULL) {
    //     next_node = curr_node -> next;
    //     curr_node -> next = prev_node;
    //     prev_node = curr_node;
    //     curr_node = next_node;
    // }
    // return prev_node;

    struct ListNode* curr_node = head;
    struct ListNode* prev_node = NULL;
    struct ListNode* next_node = NULL;

    while (curr_node != NULL){
        next_node = curr_node -> next;
        curr_node -> next = prev_node;

        prev_node = curr_node;
        curr_node = next_node;
    }
    return prev_node;
}