/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* addToArrayForm(int* num, int numSize, int k, int* returnSize) {

    int* result = (int*)malloc(sizeof(int) * (numSize + 10));
    int carry = 0; // 處理進位
    int i = numSize - 1; // num 的 index
    int j = 0; // result 的 index

    // 循環條件是 i >= 0（表示數組 num 還有數字沒有處理完）或 k > 0（表示整數 k 還沒有完全相加完）
    while (i >= 0 || k > 0){
        int sum = (i >= 0 ? num[i] : 0) + k % 10 + carry;
        result[j++] = sum % 10;
        carry = sum / 10;
        k /= 10;
        i -= 1;
    }
    // 最後一次check進位
    if (carry){
        result[j++] = carry;
    }
    // 結果反著放(原本是從左放到右)
    int left = 0 , right = j-1;
    while(left < right){
        int temp = result[left];
        result[left] = result[right];
        result[right] = temp;
        left ++;
        right --;
    }
    *returnSize = j;
    return result;
}