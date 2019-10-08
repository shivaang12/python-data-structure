from graphviz import Digraph # Print the tree in PDF

class Node(object):
    def __init__(self, interval):
        self.interval = interval
        self.left_child = None
        self.right_child = None
        self.Max = None
    
    def hasChild(self):
        if self.left_child or self.right_child:
            return True
        return False
    
    def maxOfChild(self):
        child_interval = list()
        if(self.left_child):
            child_interval.append(self.left_child.interval)
        if(self.right_child):
            child_interval.append(self.right_child.interval)
        return max(child_interval)

class IntervalTree(object):
    def __init__(self, root):
        self.root = root

    def addNode(self, new_node):
        node = self.root
        while(node != None):
            if(new_node.interval[0] <= node.interval[0]):
                if(node.left_child is None):
                    node.left_child = new_node
                    return
                node = node.left_child
            else:
                if(node.right_child is None):
                    node.right_child = new_node
                    return
                node = node.right_child

    def searchIntervalOverlap(self, query_node):
        node = self.root
        while(node):
            if(self.isOverlapping(node.interval, query_node)):
                print("Overlapping with ", node.interval)
                return True
            else:
                if(node.Max >= query_node[0]):
                    node = node.left_child
                else:
                    node = node.right_child
        return False

    def isOverlapping(self, interval_left, interval_right):
        if((interval_left[0] <= interval_right[1]) and (interval_right[0] <= interval_left[1])):
            return True
        
        return False

    def maxOfSubtree(self, root_node):
        if((not root_node.Max) and (root_node.hasChild())):
            max_array = []
            if(root_node.left_child):
                self.maxOfSubtree(root_node.left_child)
                max_array.append(root_node.left_child.Max)
            if(root_node.right_child):
                self.maxOfSubtree(root_node.right_child)
                max_array.append(root_node.right_child.Max)
            max_array.append(root_node.interval[1])
            root_node.Max = max(max_array)
            return

        else:
            root_node.Max = root_node.interval[1]
            return

    def constructMax(self):
        node = self.root
        self.maxOfSubtree(node)

    def printTree(self):
        node_list = [self.root]
        while(len(node_list) != 0):
            current_node = node_list[0]
            node_list.pop(0)
            print(current_node.interval, current_node.Max)
            if(current_node.left_child is not None):
                node_list.append(current_node.left_child)
            if(current_node.right_child is not None):
                node_list.append(current_node.right_child)
        return
    
    def printTreeInPdf(self, filename):
        g = Digraph('G', filename=filename)
        node_list = [self.root]
        while(len(node_list) != 0):
            current_node = node_list[0]
            node_list.pop(0)
            if(current_node.left_child):
                g.edge(str(current_node.Max)+"\n"+str(current_node.interval), str(current_node.left_child.Max)+"\n"+str(current_node.left_child.interval))
                node_list.append(current_node.left_child)
            if(current_node.right_child is not None):
                g.edge(str(current_node.Max)+"\n"+str(current_node.interval), str(current_node.right_child.Max)+"\n"+str(current_node.right_child.interval))
                node_list.append(current_node.right_child)
        g.view()
        return


if __name__ == '__main__':
    It = IntervalTree(Node([15, 20]))
    It.addNode(Node([10, 30]))
    It.addNode(Node([17, 19]))
    It.addNode(Node([5, 20]))
    It.addNode(Node([12, 15]))
    It.addNode(Node([30, 40]))
    It.constructMax()
    It.printTree()
    print(It.searchIntervalOverlap([6, 7]))
    It.printTreeInPdf("interval_tree.gv")