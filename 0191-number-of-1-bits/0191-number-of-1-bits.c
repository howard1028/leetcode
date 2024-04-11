int hammingWeight(int n) {
    int res = 0;
    while(n > 0){
        res += n % 2;
        // printf("res = %d , n = %d\n" ,res, n);
        n /= 2;
    }
    return res;
}