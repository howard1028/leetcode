/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countBits(int n, int* returnSize) {
    int* res = (int*) malloc((n+1) * sizeof(int)); // 指標是通用型別的 void*。為了將其轉換為指向整數類型的指針，使用了類型轉換 (int*)
    *returnSize = n + 1; // 回傳陣列的size
    res[0] = 0;
    for (int i = 1; i <= n; i++){
        res[i] = res[i >> 1] + (i & 1);
    }
    return res;
} 