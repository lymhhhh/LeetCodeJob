'''
广度优先搜索 BFS
伪代码：
BFS():


'''


# 广度搜索树
class TreeNode:
    def __init__(self, val, name):
        self.val = val
        self.name = name
        self.childs = []

    def addChild(self, child):
        self.childs.append(child)

    def printTree(self):
        return

    def __str__(self):
        return "{name:" + self.name + ", val:" + str(self.val) + ", clilds:" + str(self.getChildsName()) + "}"

    def getChildsName(self):
        result = []
        for child in self.childs:
            result.append(child.name)
        return result


# 图
class Graph:
    def __init__(self, Glist):
        self.Glist = Glist  # 邻接表
        # self.Gmap = self.initMap(Glist) # 邻接矩阵

    def initMap(self, Glist):
        return None

    def printMap(self):
        return

    def printList(self):
        return


# 使用邻接链表的BFS
def BFS(start, graph):
    # set varibles
    glist = graph.Glist

    # 队列
    queue = []
    root = TreeNode(0, start)

    # initialize varibles
    queue.append(start)

    # 状态，步长
    stepmap = dict.fromkeys(glist.keys(), -1)
    stepmap[start] = 0

    # 树节点数组
    treemap = {}
    for point in glist.keys():
        treemap[point] = TreeNode(0, point)

    # loop
    while len(queue) > 0:
        current = queue.pop(0)
        print(current)
        # get tree node

        for point in glist[current]:
            if stepmap[point] < 0:
                stepmap[point] = stepmap[current] + 1
                queue.append(point)
                # add child
                treemap[point].val = treemap[current].val + 1
                treemap[current].addChild(treemap[point])

    # show tree nodes
    for tree in treemap.keys():
        print(treemap[tree])

    return root, stepmap


l = {'s': ['r', 'w'],
     'r': ['v'],
     'w': ['t', 'x'],
     't': ['w', 'x', 'u'],
     'x': ['w', 't', 'y'],
     'u': ['t', 'x', 'y'],
     'y': ['x', 'u'],
     'v': ['r']
     }

g = Graph(l)

root, stempmap = BFS('s', g)

root.printTree()
