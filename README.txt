
NAME                      : SIVA SUBRAMANIAN PARI ARIVAZHAGAN
PROGRAMMING LANGUAGE USED : PYTHON

Note : Please make sure all files are in the same directory.

Code Structure:
The are 2 files in total :
1) find_route.py
2) <input_file>

find_route.py:

1) file_read_function(name_of_file)
   This method takes a file as input and reads it and returns the data in the file. 

2) node_adjacent_to_it(fringeq,routes,curr_node)
   This method is used to return all the adjacent nodes connected to the node passed as argument. 
   Parameters : fringeg(contains current nodes that are used to find a path)
                routes (contains all the routes in the graph which helps us to find all the nodes) 
                curr_node (contains all the visited nodes)
   
   Return Type : returns nothing.

3) node_adjacent_to_it_hue(fringeq,routes,hue_arr,curr_node)
   This method is used to return all the adjacent nodes connected to the node passed as argument. 
   Parameters : fringeg(contains current nodes that are used to find a path)
                routes (contains all the routes in the graph which helps us to find all the nodes) 
                hue_arr(contains all the nodes and their corresponding heuristic costs)
                curr_node (contains all the visited nodes)
   
   Return Type : returns nothing.

4) set_hue(hue_arr,name_of_city)
   This method is used to return the heuristic value of the city passed as the argument
   Parameters : hue_arr(contains the nodes and their corresponding heuristic values)
                name_of_city (name of the city we need to find heuristic value of)
   Return     : return heuristic value as int

5) get_fringe(routes,source_city,city_to_arrive)
   This method sorts the fringes based on least cost.
   Parameters : routes (contains all the routes in the graph which helps us to find all the nodes)
                source_city (contains node object)
                city_to_arrive (contains the name of city of destination)

6) get_fringe_astar(routes,source_city_var,city_to_arrive,hue_arr)
   This method sorts the fringes based on least cost+heuristic cost
   Parameters : routes (contains all the routes in the graph which helps us to find all the nodes)
                source_city_var (contains node object)
                city_to_arrive (contains the name of city of destination)
                hue_arr (contains all the nodes and their corresponding heuristic costs)

7) retrace_function(city_to_arrive)
   This method retraces the path from destination node to source node.
   Parameters : city_to_arrive (this contains the name of the destination city)

8) ucs(routes,source_city,destination_city)
   This method implements Uniform Cost Search on the routes from source to destination.
   Parameters : routes(contains all the routes in the graph which helps us to find all the nodes)
                source_city (contains node object)
                destination_city(contains the destination city name)

9) astar(routes,source_city,destination_city,hue_arr)
   This method implements "A star" Search on the routes from source to destination.
   Parameters : routes(contains all the routes in the graph which helps us to find all the nodes)
                source_city (contains node object)
                destination_city(contains the destination city name)
                hue_arr(contains all the nodes and their corresponding heuristic costs)

How to run the code :

The command to run the code is :
   
  To implement uninformed search
     python find_route.py uninf input_filename origin_city destination_city
  
  Example : python find_route.py uninf input1.txt Munich Berlin
 
  To implement informed search 
     python find_route.py inf input_filename origin_city destination_city heuristic_filename

  Example : python find_route.py inf input1.txt Munich Kassel h_kassel.txt 


References :
1) https://www.youtube.com/watch?v=dRMvK76xQJI
2) https://www.w3schools.com/python/python_file_handling.asp
3) https://www.w3schools.com/python/python_classes.asp
4) https://en.wikipedia.org/wiki/Admissible_heuristic
5) https://superuser.com/questions/1076953/python-typeerror-list-object-is-not-callable
