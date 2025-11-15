#include <stdio.h>

#define MAX 7

// Queue implementation
int queue[MAX];
int front = -1, rear = -1;

void enqueue(int v) {
    if (rear == MAX - 1) return; // queue full
    if (front == -1) front = 0;
    queue[++rear] = v;
}

int dequeue() {
    if (front == -1 || front > rear) return -1; // queue empty
    return queue[front++];
}

int isEmpty() {
    return (front == -1 || front > rear);
}

// BFS traversal
void BFS(int adj[MAX][MAX], int start) {
    int visited[MAX] = {0};

    printf("Breadth First Traversal starting from vertex %d:\n", start);

    enqueue(start);
    visited[start] = 1;

    while (!isEmpty()) {
        int v = dequeue();
        printf("%d ", v);

        // Explore all adjacent vertices
        for (int i = 0; i < MAX; i++) {
            if (adj[v][i] == 1 && visited[i] == 0) {
                enqueue(i);
                visited[i] = 1;
            }
        }
    }
    printf("\n");
}

int main() {
    int adj[MAX][MAX] = {
        {0,1,0,0,0,0,0},  // 0 -> 1
        {1,0,0,0,0,0,0},  // 1 -> 0
        {0,0,0,0,1,0,0},  // 2 -> 4
        {0,0,0,0,1,0,0},  // 3 -> 4
        {0,0,1,1,0,1,1},  // 4 -> 2,3,5,6
        {0,0,0,0,1,0,0},  // 5 -> 4
        {0,0,0,0,1,0,0}   // 6 -> 4
    };

    BFS(adj, 0);
    return 0;
}
