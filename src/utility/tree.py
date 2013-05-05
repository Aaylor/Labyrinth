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

