/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head) {
    if (head == NULL){
        return NULL;
    }
    struct ListNode* curr = head;
    while (curr != NULL && curr->next != NULL){
        if (curr->val == curr->next->val){
            // 要刪後面的node，否則head會沒東西
            // struct ListNode* temp = curr;
            // curr = curr->next;
            struct ListNode* temp = curr->next;
            curr->next = curr->next->next;
            free(temp);
        }
        else{
            curr = curr->next;
        }
    }
    return head;
}