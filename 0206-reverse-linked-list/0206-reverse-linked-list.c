/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head) {

    // iteration
    // struct ListNode* curr_node = head;
    // struct ListNode* prev_node = NULL;
    // struct ListNode* next_node = NULL;

    // while (curr_node != NULL){
    //     next_node = curr_node -> next;
    //     curr_node -> next = prev_node;

    //     prev_node = curr_node;
    //     curr_node = next_node;
    // }
    // return prev_node;

    // recursion
    // 終止條件：只有一個node
    if (head == NULL || head->next == NULL){
        return head;
    }
    // 後面進入遞迴
    struct ListNode* newHead = reverseList(head->next);
    
    head->next->next = head;
    head->next = NULL;
    return newHead;
}