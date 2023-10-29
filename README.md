# Treap_ADT
## What is a Treap?
A treap is a randomized data structure that simultaneously maintains properties of a binary search tree and a heap i.e _treap = tree+heap_

Thus a node in a treap will have value of node itself, a priority , pointer to left and pointer to the right
## Why do we say its a randomized data structure
Simply because the priority chosen for a data in the treap in randomly chosen 

## Advantages of a treap
- The Priority of a value added being random solves the problem of a BST of sometimes having a skewed tree, there are some cases eg: _when we are adding items to a BST and it happens that they are in **ascending order** then it forms a skewed BST of depth n_, the probability of having priorities of treap being in such a way is said to be _1/n!_ thus we can say a treap is a **nearly balanced BST** therefore _insert, delete and search operation_ would always take O(log n)
- Easier to implement, even though there are some data structures that can overacome the downside of a BST eg a Red Black Tree, but a treap ends up being easier to implement in code that a red black tree
- Has split and merge operations that help in cases of eg: _adding a range of values_ i.e a treap can also do what a segment tree does 
## Methods
|Operations| Specifications|
|----------|---------------|
|insert(key)|adds an element of key as its value with a random priority|
|delete(key)| Removes a node with the given key from the Treap return None if key not in treap|
|search(key)| Searches for a node with the specified key and returns the true if found or false if not found|
|is_empty()| Checks if the Treap is empty, return true if so, else return false |
|size()|  Returns the number of nodes in the Treap |
|merge(treap2)| requires two treaps and returns a treap which is a combination of treap2 and treap calling the object|
|split(nleftsize)| splits the treap into two with left subtreap having nleftsize while the right having the remaining|

## Balancing Property
A Treap self-adjusts to maintain the BST and max heap properties as nodes are inserted or deleted. It does this by rotating nodes when necessary to balance the tree.
