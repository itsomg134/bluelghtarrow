
/* Minimal declaration to avoid needing <stdio.h> in the editor's includePath */
int printf(const char *format, ...);

struct node {
    int data;
    struct node* left;
    struct node* right;
};

#define NODE_POOL_SIZE 128
static struct node node_pool[NODE_POOL_SIZE];
static int node_pool_index = 0;

static struct node* alloc_node(int value) {
    if (node_pool_index >= NODE_POOL_SIZE) {
        /* pool exhausted; return NULL to indicate failure */
        return 0;
    }
    struct node* n = &node_pool[node_pool_index++];
    n->data = value;
    n->left = 0;
    n->right = 0;
    return n;
}

struct node* insert(struct node* root, int value) {
    if (root == 0) {
        return alloc_node(value);
    }
    if (value < root->data) {
        root->left = insert(root->left, value);
    } else {
        root->right = insert(root->right, value);
    }
    return root;
}

void preorder(struct node* root) {
    if (root == 0) return;
    printf("%d ", root->data);
    preorder(root->left);
    preorder(root->right);
}

void inorder(struct node* root) {
    if (root == 0) return;
    inorder(root->left);
    printf("%d ", root->data);
    inorder(root->right);
}

void postorder(struct node* root) {
    if (root == 0) return;
    postorder(root->left);
    postorder(root->right);
    printf("%d ", root->data);
}

int main() {
    struct node* root = 0;

    root = insert(root, 5);
    insert(root, 2);
    insert(root, 8);
    insert(root, 1);
    insert(root, 4);
    insert(root, 6);
    insert(root, 9);
    insert(root, 7);
    insert(root, 3);

    printf("Preorder: ");
    preorder(root);
    printf("\n");

    printf("Inorder: ");
    inorder(root);
    printf("\n");

    printf("Postorder: ");
    postorder(root);
    printf("\n");

    return 0;
}
