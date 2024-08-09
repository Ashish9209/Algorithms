# Tree Traversal Algorithms

Tree traversal algorithms are methods used to explore nodes in a tree data structure. Two common traversal algorithms are Breadth-First Search (BFS) and Depth-First Search (DFS). Each algorithm uses a different approach to explore the nodes and find a specific target node.

## Breadth-First Search (BFS)

Breadth-First Search is a tree traversal algorithm that explores nodes level-by-level. It uses a queue to keep track of nodes to be explored next.

### Key Points

- **Level-by-Level Exploration:** BFS explores all nodes at the present depth level before moving on to nodes at the next depth level.
- **Iterative Approach:** BFS can be implemented using an iterative approach with the help of a queue.
- **Queue Usage:** A queue is used to store frontier nodes that need to be explored.
- **Path Finding:** BFS is useful for finding the shortest path from the root node to the goal node.

### Algorithm

1. **Initialize the Queue:**
   - Start with the root node and enqueue it.
   
2. **Explore Nodes:**
   - Dequeue a node from the front of the queue.
   - Visit the node and check if it is the goal node.
   - Enqueue all children of the current node to the queue.

3. **Return Path:**
   - Return the path of nodes from the root to the goal node if found.

## Depth-First Search (DFS)

Depth-First Search is a tree traversal algorithm that explores as far as possible along each branch before backtracking. It uses a stack to keep track of nodes to be explored.

### Key Points

- **Branch-by-Branch Exploration:** DFS explores nodes down one branch of the tree before backtracking and exploring other branches.
- **Recursive Approach:** DFS is typically implemented using recursion or a stack.
- **Stack Usage:** A stack is used to store frontier nodes to be explored.

### Algorithm

1. **Check Node Value:**
   - If the input node's value matches the target value, return the input node.

2. **Recursive Exploration:**
   - For each child of the input node, recursively call the DFS function.
   - Return the first non-null value returned by a recursive call.

3. **Handle No Children:**
   - If a node has no children, or recursive calls return null, return null.

Both BFS and DFS are fundamental algorithms for traversing trees and graphs, each suitable for different types of problems based on the structure of the data and the desired outcome.
