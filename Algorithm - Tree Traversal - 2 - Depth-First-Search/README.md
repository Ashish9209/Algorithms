
# Tree Traversal Algorithms

Tree traversal algorithms are methods used to explore nodes in a tree data structure. explore the nodes and find a specific target node.

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

