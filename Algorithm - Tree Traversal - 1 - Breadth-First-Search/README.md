
# Tree Traversal Algorithms

Tree traversal algorithms are methods used to explore nodes in a tree data structure. explore the nodes and find a specific target node.

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

