#%%
import IterativeDeepeningSearch as ids
import AStar as astar
import GraphicalInterface as gui
import AdditionalFunctions as funcs
import time

if __name__ == "__main__":
    level = input("Which level do you want to use?\n1) level 1\n2) level 2\n3) level 3\n4) level 4\n5) level 5\n6) level 6\n")
    if level == '1':
        file_name = 'test1.txt'
    elif level == '2':
        file_name = 'test2.txt'
    elif level == '3':
        file_name = 'test3.txt'
    elif level == '4':
        file_name = 'test4.txt'
    elif level == '5':
        file_name = 'test5.txt'
    elif level == '6':
        file_name = 'test6.txt'
    algorithm = input("Which Algorithm do you want to use?\n1) IDS\n2) A*\n")
    if algorithm == "1" or algorithm == "IDS":
        start_time = time.time()
        has_result, path, goal_depth, nodes_info = ids.start_ids_algorithm(file_name, 15)
        finish_time = time.time()
        duration = (finish_time - start_time)
        print("number of created nodes are:", nodes_info[0])
        print("number of expanded nodes are:", nodes_info[1])
        print("duration is : ", duration)

        if not has_result:
            print('there is no answer in this environment!')
        else:
            movement_list = funcs.find_movement_list(path)
            print("path costs : ", path[-1].cost_g)
            print("depth of goal : ", goal_depth)
            print('path is: ', movement_list)
            funcs.print_path(path)
            g = gui.GraphicalInterface(path)
            g.Visualize()
            funcs.write_to_file("IDS", file_name, movement_list, duration)
    elif algorithm == "2" or algorithm == "A*":
        start_time = time.time()
        has_result, path, goal_depth, nodes_info = astar.start_a_star_algorithm(file_name, 20)
        finish_time = time.time()
        duration = (finish_time - start_time)

        print("number of created nodes are:", nodes_info[0])
        print("number of expanded nodes are:", nodes_info[1])
        print("duration is : ", duration)

        if not has_result:
            print('there is no answer in this environment!')
        else:
            movement_list = funcs.find_movement_list(path)
            print("path costs : ", path[-1].cost_g)
            print("depth of goal : ", goal_depth)
            print('path is: ', movement_list)
            funcs.print_path(path)
            g = gui.GraphicalInterface(path)
            g.Visualize()
            funcs.write_to_file("ASTAR", file_name, movement_list, duration)
