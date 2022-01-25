
class Node:
    def __init__(self, name):
        self.name = name
        self.links = []
        self.size = 'big'
        if name not in ('start', 'end'):
            for char in name:
                if 97 <= ord(char) <= 123:
                    self.size = 'small'
                    break
        else:
            self.size = 'small'

    def add_link(self, link):
        if link not in self.links:
            self.links.append(link)

    def add_node(self, node):
        if self.name == node.name:
            for item in node.links:
                self.add_link(item)

    def __eq__(self, obj):
        return isinstance(obj, Node) and obj.name == self.name

    def __str__(self):
        output = "%s (%s):" %(self.name, self.size)
        for item in self.links:
            output += "\n - %s" %item
        return output


# Object:
#   - link
#   - link
