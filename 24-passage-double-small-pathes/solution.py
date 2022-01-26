
import csv
import argparse
from copy import deepcopy

from Node import Node, get_size

parser = argparse.ArgumentParser(description='Read input file')
parser.add_argument('infile', metavar='Infile', type=str, help='File to process')

args = parser.parse_args()
infile = vars(args)['infile']
print("Infile: %s" %infile)

# process infile
input_data = []
with open(infile, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter="-")
    for row in reader:
        route = []
        for item in row:
            route.append(item)
        input_data.append(route)
        input_data.append(route[::-1])

print("Initial input: ")
print(input_data)

points = []
for route in input_data:
    new_node = Node(route[0])
    new_node.add_link(route[1])
    if (new_node not in points):
        points.append(new_node)
    else:
        for point in points:
            if point == new_node: point.add_node(new_node)

for i in points:
    print(i)

root = points[points.index(Node('start'))]
print("\nRoot element: ", root, "\n")

def check_route(route, new_point):
    # good route if adding a big cavern
    if get_size(new_point) == 'big':
        return True

    # checking for 1+ small caverns
    small_caves = {}
    for point in route:
        if get_size(point) == 'small':
            if point in small_caves.keys():
                small_caves[point] += 1
            else:
                small_caves[point] = 1

    # if this small cavern never entered - true
    if new_point not in small_caves.keys():
        return True

    # if this small cavern entered 
    # + one small cavern entered twice - false
    if 2 in small_caves.values():
        return False
    else:
        return True


def find_way(root, points, route):
    recursion_indent = "\t" * len(route)

    # adding current node to the current route
    route.append(root.name)
    #print(recursion_indent, "Working with node %s, routes: %s" %(root.name, routes))

    new_routes = []
    if root.name == 'end':
        #print(recursion_indent, "Reached the end! Stopping recursion")
        new_routes.append(route)
        return new_routes

    else:
        for item in root.links:
        
            if Node(item) in points:
                next_node = points[points.index(Node(item))]

                if next_node.size == 'big':
                    #print(recursion_indent, "Going deeper to big (%s->%s)" %(root.name, item))
                    new_routes.extend(find_way(next_node, points, deepcopy(route)))
                elif item == 'start': 
                    #print(recursion_indent, "Faced start again. Aborting. (%s->%s)" %(root.name, item))
                    ...
                elif item == 'end':
                    new_routes.append(route + ['end'])
                elif check_route(route, item) == True:
                    #print(recursion_indent, "Going deeper to small (%s->%s)" %(root.name, item))
                    new_routes.extend(find_way(next_node, points, deepcopy(route)))
                else:
                    ...
                    #print(recursion_indent, "Not going deeper to small again (%s->%s)" %(root.name, item))
                    #new_routes.append(route)

        return new_routes

routes = []
result = find_way(root, points, routes)
print('==== Routes:', len(result))

