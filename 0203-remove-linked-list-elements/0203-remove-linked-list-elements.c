/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeElements(struct ListNode* head, int val) {
    // 刪除第一個node
    while (head != NULL && head->val == val){
        struct ListNode* temp = head;
        head = head->next;
        free(temp);
    }
    if (head == NULL){
        return NULL;
    }
    // 刪除中間node(的下一個節點)
    struct ListNode* curr = head;
    while (curr->next != NULL){
        if (curr->next->val == val){
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