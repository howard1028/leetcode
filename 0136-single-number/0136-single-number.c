int singleNumber(int* nums, int numsSize) {
    int res = 0;
    /*
    xor : a ^ 0 = a 
          a ^ a = 0
    */
    for (int i = 0; i < numsSize; i += 1){
        res ^= nums[i];
    }
    return res;
}