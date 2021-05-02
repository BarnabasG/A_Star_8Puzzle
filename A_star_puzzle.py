from random import shuffle, randint
import numpy as np
import time

def main():

    matrix = {"data":np.zeros(shape=(3,3)), "id":0, "parent":None, "g":0}
    goal = np.zeros(shape=(3,3))

    h_type = ""
    while not (h_type == "1" or h_type == "2"):
        h_type = input( "Type 1 for A* heuristic based on manhattan " +
                        "distances and 2 for number of misplaced tiles: \n")

    g_type = ""
    while not (g_type == "1" or g_type == "2"):
        g_type = input( "Type 1 to pick your own initial and goal states or " +
                        "2 to use random shuffled start and stop states: \n")

    if g_type == "1":
        input_start = []
        while not len(input_start) == 9:
            user = input("Enter the start game state from top left to bottom right e.g. 254360781: \n")
            for c in user:
                try:
                    c = int(c)
                    if 0 <= c <= 8 and not c in input_start:
                        input_start.append(c)
                except:
                    print("Invalid input: ", c)

        print()

        input_stop = []
        while not len(input_stop) == 9:
            user = input("Enter the goal game state from top left to bottom right e.g. 012345678: \n")
            for c in user:
                try:
                    c = int(c)
                    if 0 <= c <= 8 and not c in input_stop:
                        input_stop.append(c)
                except:
                    print("Invalid input: ", c)

        for i in range(3):
            for j in range(3):
                matrix["data"][i][j] = input_start.pop(0)
                goal[i][j] = input_stop.pop(0)
    
    else:
        input_start = [0,1,2,3,4,5,6,7,8]
        shuffle(input_start)
        input_stop = input_start[:]

        for i in range(3):
            for j in range(3):
                matrix["data"][i][j] = input_start.pop(0)
                goal[i][j] = input_stop.pop(0)

        for i in range(100):
            index = np.where(matrix["data"]==0)
            swap = randint(0,3)
            if swap==0:
                switch = (index[0],index[1]-1)
                pos = 1
                
            elif swap==1:
                switch = (index[0],index[1]+1)
                pos = 1
                        
            elif swap==2:
                switch = (index[0]+1,index[1])
                pos = 0
            
            elif swap==3:
                switch = (index[0]-1,index[1])
                pos = 0

            if 0 <= switch[pos] <= 2:
                new = matrix["data"][switch][0]
                matrix["data"][switch] = 0
                matrix["data"][index] = new

            
    print()

    print("Goal")
    print(goal)
    print("Initial")
    print(matrix["data"])
    start = time.perf_counter()
    calculate(goal, matrix, start, h_type)
    
def calculate(goal, matrix, start, h_type):

    layers, expansions = 0, 0
    turn = 1
    route, turns, matrices, all_nodes = [], [], [], []
    matrices.append(matrix)
    all_nodes.append(matrices[-1])
    turns.append(0)

    costs = []
    if h_type == "1":
        c = calculate_cost_1(goal, matrix["data"], 0)
    else:
        c = calculate_cost_2(goal, matrix["data"], 0)
    costs.append(c)

    while not np.array_equal(matrix["data"], goal): 
        layers += 1

        new_matrices = []
        new_costs = []

        index = np.where(matrix["data"]==0)

        route = get_route(matrix, all_nodes)

        switch = (index[0],index[1]-1)
        if 0 <= switch[1] <= 2:
            left = np.copy(matrix["data"])
            new = matrix["data"][switch][0]
            left[switch] = 0
            left[index] = new
            
            expanded = False
            if any(np.array_equal(m["data"], left) for m in route):
                expanded = True
            if not expanded:
                if any(np.array_equal(m["data"], left) for m in matrices):
                    expanded = True
                    
            if not expanded:
                expansions += 1
                matrices.append({"data":left,"id":expansions,"parent":matrix["id"]})
                turns.append(turn)
                new_matrices.append(matrices[-1])
                all_nodes.append(matrices[-1])
                if h_type == "1":
                    c = calculate_cost_1(goal, left, turn)
                else:
                    c = calculate_cost_2(goal, left, turn)
                costs.append(c)
                new_costs.append(costs[-1])
                

        switch = (index[0],index[1]+1)
        if 0 <= switch[1] <= 2:
            right = np.copy(matrix["data"])
            new = matrix["data"][switch][0]
            right[switch] = 0
            right[index] = new

            expanded = False
            if any(np.array_equal(m["data"], right) for m in route):
                expanded = True
            if not expanded:
                if any(np.array_equal(m["data"], right) for m in matrices):
                    expanded = True
            
            if not expanded:
                expansions += 1
                matrices.append({"data":right, "id":expansions, "parent":matrix["id"]})
                turns.append(turn)
                new_matrices.append(matrices[-1])
                all_nodes.append(matrices[-1])
                if h_type == "1":
                    c = calculate_cost_1(goal, right, turn)
                else:
                    c = calculate_cost_2(goal, right, turn)
                costs.append(c)
                new_costs.append(costs[-1])
                

        switch = (index[0]+1,index[1])
        if 0 <= switch[0] <= 2:
            down = np.copy(matrix["data"])
            new = matrix["data"][switch][0]
            down[switch] = 0
            down[index] = new

            expanded = False
            if any(np.array_equal(m["data"], down) for m in route):
                expanded = True
            if not expanded:
                if any(np.array_equal(m["data"], down) for m in matrices):
                    expanded = True
            
            if not expanded:
                expansions += 1
                matrices.append({"data":down, "id":expansions, "parent":matrix["id"]})
                turns.append(turn)
                new_matrices.append(matrices[-1])
                all_nodes.append(matrices[-1])
                if h_type == "1":
                    c = calculate_cost_1(goal, down, turn)
                else:
                    c = calculate_cost_2(goal, down, turn)
                costs.append(c)
                new_costs.append(costs[-1])
                

        switch = (index[0]-1,index[1])
        if 0 <= switch[0] <= 2:
            up = np.copy(matrix["data"])
            new = matrix["data"][switch][0]
            up[switch] = 0
            up[index] = new

            expanded = False
            if any(np.array_equal(m["data"], up) for m in route):
                expanded = True
            if not expanded:
                if any(np.array_equal(m["data"], up) for m in matrices):
                    expanded = True
            
            if not expanded:
                expansions += 1
                matrices.append({"data":up, "id":expansions, "parent":matrix["id"]})
                turns.append(turn)
                new_matrices.append(matrices[-1])
                all_nodes.append(matrices[-1])
                if h_type == "1":
                    c = calculate_cost_1(goal, up, turn)
                else:
                    c = calculate_cost_2(goal, up, turn)
                costs.append(c)
                new_costs.append(costs[-1])
                

        for i, this_matrix in enumerate(matrices):
            if np.array_equal(matrix["data"], this_matrix["data"]):
                matrices.pop(i)
                turns.pop(i)
                costs.pop(i)

        next_index = costs.index(min(costs))
                
        matrix = matrices[next_index]
        if new_costs:
            this_min = new_matrices[new_costs.index(min(new_costs))]["data"]
        else:
            this_min = np.zeros(shape=(3,3))

        if not np.array_equal(matrix["data"], this_min):

            for i, this_matrix in enumerate(matrices):
                if np.array_equal(this_matrix["data"], matrix["data"]):
                    turn = turns[i]

        turn += 1

        if layers == 5000:
            print("Unsolvable!")
            break

    stop = time.perf_counter()
    turn -= 1

    route = get_route(matrix, all_nodes)

    print("ROUTE - ")
    for i, m in enumerate(route):
        c = calculate_cost_1(goal, m["data"], i)
        print("=======")
        for i in range(3):
            for j in range(3):
                print("|", end='')
                print(int(m["data"][i][j]), end='')
            print("|")
            print("=======")
        print("estimated cost: ", c)
    print("=================")
    print("| steps: ", turn, "   |")
    print("=================")
    print("cost - ", min(costs))
    print("layers: ", layers)
    print("node expansions: ", expansions)
    print(f"Execution time: {stop-start:0.3f} seconds")

def get_route(matrix, matrices):
    route = []
    route.append(matrix)
    node = matrix
    while True:
        parent_id = node["parent"]
        if parent_id == None:
            break
        else:
            for m in matrices:
                if m["id"] == parent_id:
                    node = m
                    route.insert(0, m)
                    break
    return route

def calculate_cost_1(goal, matrix, count):
    cost = count
    for i in range(1,9):
        index1 = np.where(goal==i)
        index2 = np.where(matrix==i)
        cost += abs(index1[0] - index2[0]) + abs(index1[1] - index2[1])
    return(cost)

def calculate_cost_2(goal, matrix, count):
    cost = count
    for i in range(1,9):
        if not np.where(goal==i) == np.where(matrix==i):
            cost += 1
    return(cost)

main()