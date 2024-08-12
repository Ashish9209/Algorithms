
# Graph Search Algorithms

Graph search algorithms are used to traverse a graph data structure to locate a specific value. During traversal, vertices are marked with a “visited” list to keep track of whether each vertex has been checked.

## Common Approaches

There are two common approaches to traversing a graph:

- **Depth-First Search (DFS):** 
  - Follows each possible path to its end before backtracking.
  - Can be implemented using either recursion or a stack data structure.
  - Useful for determining whether a path exists between two points.

- **Breadth-First Search (BFS):**
  - Expands its search from the point of origin to an ever-expanding circle of neighboring vertices.
  - Generally relies on a queue data structure.
  - Helpful in finding the shortest path between two points.

## Traversal Orders

Three main traversal orders are used in graph traversal:

- **Preorder:**
  - Each vertex is added to the “visited” list and output list **before** being added to the stack.

- **Postorder:**
  - Each vertex is added to the “visited” list and output list **after** being popped off the stack.

- **Reverse Post-Order (Topological Sort):**
  - Returns an output list that is the reverse of the post-order list.

## Runtime Complexity

The runtime for graph search algorithms is \( O(\text{vertices} + \text{edges}) \).