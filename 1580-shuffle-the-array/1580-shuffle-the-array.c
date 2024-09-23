/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* shuffle(int* nums, int numsSize, int n, int* returnSize){
    int* result = (int*) malloc(sizeof(int) * numsSize);
    *returnSize = numsSize;
    for(int i=0, j=n, k=0; i<n; i++,j++){
        result[k++] = nums[i];
        result[k++] = nums[j];
    }
    return result;
}