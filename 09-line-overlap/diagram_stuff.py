
from VentPoint import VentPoint

def init_vent_diagram(size):
    diagram = []
    for i in range(size):
        line = []
        for j in range(size):
            line.append(VentPoint(i, j))

        diagram.append(line)
    return diagram

def print_diagram(diagram):
    for line in diagram:
        for item in line:
            print(item, end=" ")
        print()

def mark_line(diagram, line):
    start = line[0]
    end = line[1]

    marked_coord = [ start, end ]
    #print("Start: %s, end: %s" %(start, end))
    if start[0] == end[0]:
        #print("\tHorizontal line")
        if end[1] > start[1]:
            line = [ start[1], end[1]]
        else:
            line = [ end[1], start[1] ]

        for i in range(line[0]+1, line[1]):
            #print("\tMarking point: %d:%d" %(start[0], i))
            marked_coord.append([start[0], i])
    else:
        #print("\tVertical line")
        if end[0] > start[0]:
            line = [ start[0], end[0]]
        else:
            line = [ end[0], start[0] ]

        for i in range(line[0]+1, line[1]):
            #print("\tMarking point: %d:%d" %(i, start[1]))
            marked_coord.append([i , start[1]])

    for coord in marked_coord:
        diagram[coord[0]][coord[1]].mark()

def count_overlaps(diagram):
    count = 0
    for line in diagram:
        for item in line:
            if item.marks > 1 :
                count += 1
    return count
