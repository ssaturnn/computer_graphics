
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def getCoords(self):
        return self.x, self.y


class Edge:
    def __init__(self, point1=Point(), point2=Point()):
        self.start = point1
        self.end = point2

    def swapPoints(self):
        self.start, self.end = self.end, self.start


class Polygon:

    def __init__(self):
        self.points = []
        self.edges = []
        self.points_num = 0
        
    def addPoint(self, point):
        self.points.append(point)
        self.points_num += 1

    def addEdge(self, p1_index, p2_index):
        edge = Edge(self.points[p1_index], self.points[p2_index])
        self.edges.append(edge)

    def deletePoint(self):
        self.points.pop()
        self.points_num -= 1

    def deleteEdge(self):
        self.edges.pop()
