# from .sample_generator import generate_random_graph_sample 
# print(generate_random_graph_sample(5))

from sample_generator import generate_random_graph_sample as generator



def findSubgroups(graph):
    print("implement")



def isVertexCover(graph):
    print("implement")



def findSize(graph):
    print("implement")


def findVertices(graph):
    print("implement")




def findMinVertexCover(n,k):
    graph = generator(n) #edges
    vertices = findVertices(graph)
    subgroups = findSubgroups(graph)
    flag = False
    min = None
    for S in subgroups:
        if(findSize(S) <= k):
            flag = True
            for (u,v) in graph:
                if u not in vertices and v not in vertices:
                    flag = False
                    break
            if flag == True:
                if min == None or findSize(S) < findSize(min):
                    min = S
    if min != None:
        return True, min
    else:
        return False