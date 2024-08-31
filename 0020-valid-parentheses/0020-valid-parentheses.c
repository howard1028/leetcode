bool isValid(char* s) {
    char stack[10000];
    int top = -1; // 每次要先加，所以top空從-1開始

    for (int i=0 ; s[i]!='\0' ; i++){
        char c = s[i];
        // printf("%c" , c);
        if (c == '(' || c == '[' || c == '{'){
            stack[++top] = c;
        }
        else{
            if (top == -1) return false; // stack為空
            
            if ((c == ')' && stack[top] == '(') ||
                (c == ']' && stack[top] == '[') ||
                (c == '}' && stack[top] == '{')){
                top --; // 不用pop，直接改變top指標就好
            }
            else{
                return false;
            }
        }
    }
    if (top == -1){
        return true;
    }
    else return false;
}