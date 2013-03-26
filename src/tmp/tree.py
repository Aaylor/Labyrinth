#!/dev/bin/python

class Tree(object):

    def __init__(self, value, *args, **kwargs):
        self.value, self.sons = value, list(args)

    def display_tree(self, indent=0):
        print("{}{}".format(" "*indent, self.value))
        for val in self.sons:
            val.display_tree(indent+1)

    def in_tree(self, searched_value):
        boolean = False
        if searched_value == self.value:
            return True

        for val in self.sons:
            boolean = val.in_tree(searched_value)
            if boolean:
                return True
        return False

    def add_son(self, new_son, other_tree=None):
        if other_tree != None:
            if not other_tree.in_tree(new_son.value):
                self.sons.append(new_son)
        else:
            if not self.in_tree(new_son.value):
                self.sons.append(new_son)

if __name__ == "__main__":
    child_1 = Tree([2,3])
    child_2 = Tree([4,5])
    child_3 = Tree([6,3], child_1, child_2)
    child_1.add_son(Tree([12,3]))
    t = Tree([1,2], child_3)

    t.display_tree()
    print(t.in_tree([4,5]), t.in_tree([1,3]))

