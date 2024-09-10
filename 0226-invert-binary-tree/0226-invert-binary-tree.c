/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode* invertTree(struct TreeNode* root) {
    if(root == NULL){
        return NULL;
    }

    // D
    struct TreeNode* temp = root->left;
    root->left = root->right;
    root->right = temp;
    // L
    invertTree(root->left);
    // R
    invertTree(root->right);

    return root;
}