class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    # initialize a list with the root node of the tree
    nodes_to_visit = [self.root]

    while nodes_to_visit:
      #removes the first node
      node = nodes_to_visit.pop(0)
      if node['id'] == id:
        return node
      # adds its children to the end of the list if no match is found
      nodes_to_visit = nodes_to_visit + node['children']

    return None # if the loop completes without finding a matching node, the method returns None