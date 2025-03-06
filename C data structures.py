--list--
# made from nodes which each node has the next node adress and some data
# declare the structure: typedef struc node { (type name); struct node *next;} node;
# node *list = NULL; start of the list
# node *n = malloc (sizeof(node)); add a node
# (*n).data = data == n->data = data; load a node
    # n->next = NULL; need to especify the end of the list
    # list = n; n is an aux
# to add an extra node
       *n = malloc
       n->data = x;
       n->next = list (points to the first element of the list)
       list = n; (prepending aka insertarAdelante) O(1) add - O(n) search

   *n = malloc
    if (n = NULL) {list = n};
    else {
    for (ptr = *node; ptr != NULL; ptr = ptr-next){
    if (ptr == NULL){ ptr->next = n; break}
    }} (prending aka insertarAtras) O(n) add + O() search

*n = malloc
if (n == NULL) {list = n} else
if (n < list->number){ n->next = list; list = n}
else {
for (node *ptr = list; ptr != NULL; ptr = ptr->next){
    if (ptr == NULL) {ptr->next = n; break}
    else if (n->number > ptr->next->number) { n->next = ptr->next; ptr->next = n; break}
}} (insertion aka insetarOrdenado) O(n)

--tree--
# made from nodes which each node points at it's left and right
# declare structure: typedef struct node {type:data; struct node *left; struct node *right;} node

search
bool function(tree *node, number)
if (tree == NULL) #reach the end
{return false}
else if (number > tree->number)
{return function(tree->right, number)}
else if (number < tree->number)
{return funtcion(tree->left, number)}
else if (number == tree->number)
{return true}

--dictionary--
# stores keys and values
# keys must be sorted, in order to improve the serch to O(log n)
# since they keys are in order, it diference it from a list

--hashing--
    # you can say its an array of lists
# organizes different list from a condition, for example a bookphone
# you have 26 starting letters, and you'll have a list for each letter
# trade of memory for speed
# declare structure: typedef struct node{type:data; type:data2; struct node *next;}node;
# declare typeStructure *name[organization type] -- example: node *notebook[26];

# hashing function itself recives an imput and returns an outpot; example it gets a name a returns it first letter alphabetically number;
    # unsigned int hashing(const char *name)
       # {return toupper(name[o] - 'A');}

--tries--

# xd
