void swap(int* a , int* b){
    int temp = *a;
    *a = *b;
    *b = temp;
}

void insertHeap(int* heap , int* heapSize , int val){
    int i = (*heapSize)++;
    heap[i] = val;

    while(i != 0 && heap[(i-1) / 2] < heap[i]){
        swap(&heap[i] , &heap[(i-1) / 2]);
        i = (i - 1) / 2;
    }
}

// 維持 max heap
void heapify(int* heap , int heapSize , int i){
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < heapSize && heap[left] > heap[largest]){
        largest = left;
    }
    if (right < heapSize && heap[right] > heap[largest]){
        largest = right;
    }
    if(largest != i){
        swap(&heap[i] , &heap[largest]);
        heapify(heap , heapSize , largest);
    }
}

// 拿出 max heap 最大的
int extractMax(int *heap , int* heapSize){
    if(*heapSize == 0){
        return 0;
    }
    int maxElement = heap[0];
    heap[0] = heap[--(*heapSize)];
    heapify(heap , *heapSize , 0);

    return maxElement;
}

int lastStoneWeight(int* stones, int stonesSize) {
    int* heap = (int*)malloc(stonesSize * sizeof(int));
    int heapSize = 0;

    // 插入stone到heap
    for (int i=0; i<stonesSize; i++){
        insertHeap(heap , &heapSize , stones[i]);
    }

    // smash 最大的兩個石頭
    while(heapSize > 1){
        int stone1 = extractMax(heap , &heapSize);
        int stone2 = extractMax(heap , &heapSize);

        if(stone1 != stone2){
            insertHeap(heap , &heapSize , stone1 - stone2);
        }
    }
    // 找最後剩下的石頭
    int lastStone = (heapSize == 1) ? heap[0] : 0;

    free(heap);
    return lastStone;
}