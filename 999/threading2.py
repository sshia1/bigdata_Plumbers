import threading 
  
def print_x(x, n): 
	for i in range(n):
		print(x)
  
if __name__ == "__main__": 
	# create threads
	t1 = threading.Thread(target=print_x, args=(1, 5,)) 
	t2 = threading.Thread(target=print_x, args=(2, 10,)) 
	
	# start thread 1 
	t1.start() 
	# start thread 2 
	t2.start() 
	
	# wait until thread 1 is completely executed 
	t1.join() 
	# wait until thread 2 is completely executed 
	t2.join() 
	# both threads completely executed 
	
	print("Done!") 
