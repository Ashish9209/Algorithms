
# Understanding Trees

Trees are a hierarchical data structure used to model relationships where each node has a single parent but can have multiple children. They are particularly useful for representing hierarchical data such as organizational structures, file systems, and taxonomies.

## Key Concepts

### 1. Root
- **Definition**: The root is the topmost node of the tree, which has no parent.
- **Properties**: There is only one root node per tree.
- **Example**: In a file system, the root directory is the top-level directory from which all other directories branch.

### 2. Parent
- **Definition**: A parent node is any node that references other nodes, known as its children.
- **Properties**: Each parent node can have multiple child nodes.
- **Example**: In a family tree, a parent node represents a parent, and its child nodes represent the children.

### 3. Child
- **Definition**: Child nodes are those referenced by another node, known as their parent.
- **Properties**: A node can have zero or more children.
- **Example**: In a corporate hierarchy, employees are children of their managers.

### 4. Sibling
- **Definition**: Sibling nodes are nodes that share the same parent.
- **Properties**: Siblings are at the same level in the tree.
- **Example**: In an organizational chart, employees who report to the same manager are siblings.

### 5. Leaf
- **Definition**: A leaf node is a node that has no children.
- **Properties**: Leaf nodes are at the end of a branch.
- **Example**: In a decision tree, a leaf node represents an outcome or final decision.

### 6. Level
- **Definition**: The level of a node indicates its distance from the root. The root is at level 1, its direct children are at level 2, and so on.
- **Properties**: The level represents the depth of the node in the tree.
- **Example**: In an organizational hierarchy, a CEO at the top level is level 1, their direct reports are level 2, etc.

Implemented a tree in Python.

-   Trees are a Python class called TreeNode.
-   A TreeNode has two properties, value and children.
-   Nodes hold any type of data inside value.
-   children is a list, which can be empty or hold other instances of TreeNode.
-   We add to children by using the list method .append.
-   We remove from children by filtering the list.