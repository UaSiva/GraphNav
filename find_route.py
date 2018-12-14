
""" NAME   : SIVA SUBRAMANIAN PARIARIVAZHAGAN  """
""" UTA ID : 1001644268                        """


import sys

class cnode:
	"""used to define a datastrcuture for representing the cities"""
	def __init__(self, name_of_city,node_parent,final_total,current_route_cost,hue_cost):
		
		self.name_of_city = name_of_city;
		self.node_parent = node_parent;
		self.final_total = final_total;
		self.current_route_cost = current_route_cost;
		self.hue_cost = hue_cost;

def file_read_func(name_of_file):
	the_data=[]

	File_Not_Found = None 
	try:
		file=open(name_of_file, 'r')
	except File_Not_Found:
		print 'Encountered an error. Cannot open File'
	else:
		the_data=[line for line in file]
		file.close()

	return the_data

def node_adjacent_to_it(fringeq,routes,curr_node):
	current_city_node=fringeq[0]
	del fringeq[0]

	name_of_city = current_city_node.name_of_city
	current_route_cost = current_city_node.final_total
	curr_node.append(name_of_city)

	for route in routes:
		if name_of_city in route:
			if route[1]==name_of_city and not(route[0] in curr_node):
				city_adj_toit=cnode(route[0],current_city_node, int(current_route_cost)+int(route[2]),int(route[2]),0)
				fringeq.append(city_adj_toit)

			elif route[0]==name_of_city and not(route[1] in curr_node):
				 city_adj_toit=cnode(route[1],current_city_node,int(current_route_cost)+int(route[2]),int(route[2]),0)
				 fringeq.append(city_adj_toit)

def set_hue(hue_arr,name_of_city):
          for i in range(20): 
                if hue_arr[i][0]==name_of_city:
                    return int(hue_arr[i][1])
                  
                

def node_adjacent_to_it_hue(fringeq,routes,hue_arr,curr_node):
	current_city_node=fringeq[0]
	del fringeq[0]

	name_of_city=current_city_node.name_of_city
	current_route_cost=current_city_node.final_total+current_city_node.hue_cost
	curr_node.append(name_of_city)

	for route in routes:
		if name_of_city in route:
			if route[1]==name_of_city and not(route[0] in curr_node):
				city_adj_toit=cnode(route[0],current_city_node, int(current_route_cost)+int(route[2])+current_city_node.hue_cost,0,set_hue(hue_arr,name_of_city))
				fringeq.append(city_adj_toit)
			elif route[0]==name_of_city and not(route[1] in curr_node):
				city_adj_toit=cnode(route[1],current_city_node, int(current_route_cost)+int(route[2])+current_city_node.hue_cost,0,set_hue(hue_arr,name_of_city))


def get_fringe(routes,source_city,city_to_arrive):
	fringeq=[]
	curr_node=[]

	curr_node.append(source_city.name_of_city)
        fringeq.append(source_city)

	while True:
		if not fringeq:
			return None
		if fringeq[0].name_of_city==city_to_arrive:
			return fringeq[0]

		node_adjacent_to_it(fringeq,routes,curr_node)

		fringeq=sorted(fringeq ,key=lambda node: node.final_total)

def get_fringe_astar(routes,source_city_var,city_to_arrive,hue_arr):
	fringeq=[]
	curr_node=[]

	curr_node.append(source_city_var.name_of_city)
	fringeq.append(source_city_var)

	while True:
		if not fringeq:
			return None
		if fringeq[0].name_of_city==city_to_arrive:
			return fringeq[0]

		node_adjacent_to_it_hue(fringeq,routes,hue_arr,curr_node)

		fringeq=sorted(fringeq, key=lambda node: node.final_total)


def retrace_function(city_to_arrive):
	
	print 'distance: %d km' % city_to_arrive.final_total

	cost_for_traversing=[]
	temp_city=[]

	while city_to_arrive:
		cost_for_traversing.append(city_to_arrive.current_route_cost)
		temp_city.append(city_to_arrive.name_of_city)
		city_to_arrive=city_to_arrive.node_parent
	temp_city.reverse()
        cost_for_traversing.reverse()
	

	del cost_for_traversing[0]
	print 'route:'

	for i in range(0,len(temp_city)-1):
		temp_city[i]=temp_city[i][0].upper()+temp_city[i][1:]
		temp_city[i+1]=temp_city[i+1][0].upper()+temp_city[i+1][1:]
		print '%s to %s, %d km' % (temp_city[i],temp_city[i+1],cost_for_traversing[i])
		

def ucs(routes,source_city,destination_city):
	
	final_result=get_fringe(routes,source_city,destination_city)

	if final_result==None:
		print 'distance=infinty'
		print 'route:'
		print 'none'
	else:
		retrace_function(final_result)

def astar(routes,source_city,destination_city,hue_arr):
	final_result=get_fringe_astar(routes,source_city,destination_city,hue_arr)

	if final_result==None:
		print 'distance=infinty'
		print 'route'
		print 'none'
	else:
		retrace_function(final_result)


def main():
	if len(sys.argv)<4:
		print '[Format] python ucs.py <file_name> <source_city> <destination_city>'
		print 'Heads UP ! Kindly place the file in the same folder'
		return

	if len(sys.argv)==5 and sys.argv[1]=='uninf':
	        name_of_file=sys.argv[2]
	        source_city=sys.argv[3].lower()
	        destination_city=sys.argv[4].lower()

	        the_data=file_read_func(name_of_file)


	        if not the_data:
	    	    return


	        routes=[route.lower().split() for route in the_data]

	
	        del routes[len(routes)-1]
	        del routes[len(routes)-1]

      	        obj=cnode(source_city,None,0,0,0)

	        ucs(routes,obj,destination_city)

	if len(sys.argv)==6 and sys.argv[1]=='inf':
		name_of_file=sys.argv[2]
		source_city=sys.argv[3].lower()
		destination_city=sys.argv[4].lower()
		name_of_hue_file=sys.argv[5]

		the_data=file_read_func(name_of_file)

		if not the_data:
		    return

		routes=[route.lower().split() for route in the_data]

		del routes[len(routes)-1]
		del routes[len(routes)-1]

                hue_list=file_read_func(name_of_hue_file)

                if not hue_list:
                    return


                hue_arr=[hue_var.lower().split() for hue_var in hue_list]

	        del hue_arr[len(hue_arr)-1]
	        del hue_arr[len(hue_arr)-1]

	        obj=cnode(source_city,None,0,0,set_hue(hue_arr,source_city)) #last argument adirecta vangiten

	        astar(routes,obj,destination_city,hue_arr)
		



if __name__ == '__main__':
	main()

