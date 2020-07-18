import threading 
  
def print_one(): 
	for i in range(10):
		print(1)
  
def print_two(): 
	for i in range(10):
		print(2)
  
if __name__ == "__main__": 
	# create threads
	t1 = threading.Thread(target=print_one) 
	t2 = threading.Thread(target=print_two) 
	
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
