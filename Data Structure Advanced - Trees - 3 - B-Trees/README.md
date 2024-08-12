This code implements a B-Tree, a self-balancing tree data structure that maintains sorted data and allows searches, sequential access, insertions, and deletions in logarithmic time. B-Trees are widely used in databases and file systems due to their efficiency in handling large amounts of data.

### Key Components of the B-Tree

1. **`BTreeNode` Class:**
   - Represents a node in the B-Tree.
   - Attributes:
     - `keys`: List of keys in the node.
     - `children`: List of child nodes.
     - `leaf`: Boolean indicating if the node is a leaf node.
     - `t`: Minimum degree (or branching factor) of the B-Tree.

   - Methods:
     - `split(parent, value)`: Splits the current node into two nodes and updates the parent node. It returns which of the two nodes to descend into based on the value being inserted.
     - `_is_leaf`: Checks if the node is a leaf (i.e., has no children).
     - `_is_full`: Checks if the node is full (i.e., contains `2*t - 1` keys).
     - `_size`: Returns the number of keys in the node.
     - `add_key(value)`: Inserts a key into the node while maintaining sorted order.
     - `add_child(new_node)`: Adds a new child node in the correct position based on the key values.

2. **`BTree` Class:**
   - Manages the overall B-Tree structure.
   - Attributes:
     - `t`: Minimum degree (or branching factor).
     - `root`: The root node of the B-Tree.

   - Methods:
     - `find_correct_child_node(node, value)`: Finds the appropriate child node where the value should be inserted or searched for.
     - `insert(value)`: Handles the insertion of a new value into the B-Tree. It starts by checking if the root is full and needs splitting, then finds the correct position for the new value, and handles splits as necessary.
     - `search(value, node=None)`: Searches for a value in the B-Tree. If no node is specified, it starts from the root.

### Detailed Explanation of Key Functions

#### `BTreeNode.split(parent, value)`

- **Purpose:** Splits the current node into two nodes when it is full and updates the parent node to accommodate the new structure.
- **Steps:**
  1. Creates a new node (`new_node`) to hold the split keys and children.
  2. Determines the key (`split_key`) that will move up to the parent.
  3. Updates `new_node` with the right half of the current node's keys and children.
  4. Updates the current node with the left half.
  5. Inserts `new_node` into the parent's children list.
  6. Returns either the current node or `new_node` depending on where the value should go.

#### `BTree.insert(value)`

- **Purpose:** Inserts a new value into the B-Tree.
- **Steps:**
  1. Checks if the root is full and splits it if necessary, creating a new root.
  2. Navigates down the tree to find the appropriate leaf node.
  3. Inserts the value into the correct leaf node.
  4. If a child node is full, it is split before the value is inserted.

#### `BTree.search(value, node=None)`

- **Purpose:** Searches for a value in the B-Tree.
- **Steps:**
  1. If no starting node is provided, begins with the root.
  2. Checks if the value is present in the current node.
  3. If the value is not found and the node is a leaf, the search terminates.
  4. If the node is not a leaf, recursively searches the appropriate child node.

### Summary

- **B-Tree Structure:** A self-balancing tree that maintains sorted data with nodes containing multiple keys and children. It allows efficient insertion, deletion, and search operations.
- **Key Operations:**
  - **Insertion:** Handles node splitting and key movement to maintain balance.
  - **Search:** Traverses the tree based on key comparisons to find a value or determine its absence.
- **Efficiency:** Provides logarithmic time complexity for insertions, deletions, and searches, making it suitable for large datasets.
