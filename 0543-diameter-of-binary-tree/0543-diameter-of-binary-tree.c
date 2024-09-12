/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

int maxDepth(struct TreeNode* node , int* diameter){
    if (node == NULL){
        return 0;
    }
    int leftDepth = maxDepth(node->left , diameter);
    int rightDepth = maxDepth(node->right , diameter);
    
    // 更新最大路徑
    int pathLength = leftDepth + rightDepth;
    if(pathLength > *diameter){
        *diameter = pathLength;
    }

    return (leftDepth > rightDepth ? leftDepth : rightDepth) + 1;
}
int diameterOfBinaryTree(struct TreeNode* root) {
    int diameter = 0;
    maxDepth(root , &diameter);
    return diameter;
}