/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int checkHeight(struct TreeNode* node){
    if(node == NULL){
        return 0;
    }
    int leftHeight = checkHeight(node->left);
    // left subtree not balanced
    if (leftHeight == -1){
        return -1;
    }

    int rightHeight = checkHeight(node->right);
    // right subtree not balanced
    if (rightHeight == -1){
        return -1;
    }
    
    // check if left、right subtree's height sub > 1
    if (abs(leftHeight - rightHeight) > 1){
        return -1;
    }

    return (leftHeight > rightHeight ? leftHeight : rightHeight) + 1;
    
}

bool isBalanced(struct TreeNode* root) {
    return checkHeight(root) != -1;
}