class Node:
    def __init__(self,data,link=None):
        self.data=data
        self.link=link
class Link_List:
    def __init__(self):
        self.head=None
    def print_node(self):
      if not self.head:
        print("Empty list")
        return
      node=self.head

      print((node.data),end='')
      node=node.link
      while(node):
         print("==>{}".format(node.data),end='')
         node=node.link

def create():
    first_list=Link_List()
    first_node=Node(2)
    first_list.head=first_node
    second_node=Node(3)
    first_node.link=second_node
    third_node=Node(4)
    second_node.link=third_node
    fourth_node=Node(5)
    first_list.head.link.link.link=fourth_node
    return first_list

