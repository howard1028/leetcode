/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
    if (headA == NULL || headB == NULL){
        return NULL;
    }
    struct ListNode* pA = headA;
    struct ListNode* pB = headB;
    // 有交叉：同時指到某個node
    // 沒交叉：同時指到NULL
    while (pA != pB){
        // if (pA == NULL && pB == NULL){
        //     break;
        // }
        pA = (pA == NULL) ? headB : pA->next;
        pB = (pB == NULL) ? headA : pB->next;
    }
    return pA;
}