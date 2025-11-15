#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* prev;
    struct Node* next;
};

void swapNodes(struct Node** head) {
    if (*head == NULL || (*head)->next == NULL)
        return;

    struct Node* first = *head;
    struct Node* second = first->next;

    // Adjust pointers
    first->next = second->next;
    first->prev = second;
    second->prev = NULL;
    second->next = first;

    if (first->next != NULL)
        first->next->prev = first;

    *head = second;
}

int main() {
    struct Node* head = malloc(sizeof(struct Node));
    struct Node* second = malloc(sizeof(struct Node));

    head->data = 45;
    head->prev = NULL;
    head->next = second;

    second->data = 50;
    second->prev = head;
    second->next = NULL;

    printf("Before swap: %d -> %d\n", head->data, head->next->data);

    swapNodes(&head);

    printf("After swap: %d -> %d\n", head->data, head->next->data);

    return 0;
}
