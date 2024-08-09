from tree import TreeNode
from bfs import bfs

sample_root_node = TreeNode("Home")
docs = TreeNode("Documents")
photos = TreeNode("Photos")
sample_root_node.children = [docs, photos]
my_wish = TreeNode("WishList.txt")
my_todo = TreeNode("TodoList.txt")
my_cat = TreeNode("Fluffy.jpg")
my_dog = TreeNode("Spot.jpg")
docs.children = [my_wish, my_todo]
photos.children = [my_cat, my_dog]

print(sample_root_node)
# Change the 2nd argument below
goal_path = bfs(sample_root_node, "Fluffy.jpg")
if goal_path is None:
  print("No path found")
else:
  print("Path found")
  for node in goal_path:
    print(node.value)


# Before starting the search, define the tree’s root node as well as a value to search for.
# Initialize a frontier queue, which holds a path for each node to search
# Loop through the frontier queue to check if the node value matches the value we are searching for.
# Continue the search by adding child nodes to the frontier until the goal has been found, or the tree has been completely searched.
