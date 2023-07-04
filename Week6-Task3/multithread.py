##import threading
##
##def print_message(message):
##    print(message)
##
##def print_message1(message1):
##    print(message1)
##
### Create and start two threads
##thread1 = threading.Thread(target=print_message, args=("Hello from Thread 1",))
##thread2 = threading.Thread(target=print_message1,args=("Hello from Thread 2",))
##thread1.start()
##thread1.join()
##thread2.start()
##thread1.join()
##thread2.join()
##






##import threading
##
##
##def count_up():
##    for i in range(5):
##        print("Count up:", i)
##
##def count_down():
##    for i in range(5, 0,-1):
##        print("Count down:", i)
##
### Create and start two threads
##thread1 = threading.Thread(target=count_up)
##thread2 = threading.Thread(target=count_down)
##thread1.start()
##thread2.start()
##thread1.join()
##thread2.join()







##
##import threading
##
##def count_up():
##    for i in range(5):
##        print("Count up:", i)
##
##def count_down():
##    for i in range(5, 0,-1):
##        print("Count down:", i)
##
### Create and start two threads
##thread1 = threading.Thread(target=count_up)
##thread2 = threading.Thread(target=count_down)
##thread1.start()
##thread1.join()
##thread2.start()
##thread2.join()










##import threading
##
##counter = 0
##counter_lock = threading.Lock()
##
##def increment_counter():
##    global counter
##    with counter_lock:
##        for _ in range(100000):
##            counter += 1
##
### Create and start two threads
##thread1 = threading.Thread(target=increment_counter)
##thread2 = threading.Thread(target=increment_counter)
##thread1.start()
##thread2.start()
##thread1.join()
##thread2.join()

##print("Counter value:", counter)








##import threading
##
##def print_message():
##    print("hello")
##
## Create and start two threads
##thread1 = threading.Thread(target=print_message)
##thread2 = threading.Thread(target=print_message)
##thread1.start()
##thread1.join()
##thread2.start()
##thread2.join()
##








##import threading
##
##def count_up():
##    for i in range(5):
##        print("Count up:", i)
##
##def count_down():
##    for i in range(5, 0,-1):
##        print("Count down:", i)
##count_up()
##count_down()






##import threading
##
##
##def greet(name):
##    print("Hello, " + name)
##
### Create a thread and start its execution
##thread = threading.Thread(target=greet, args=("Alice",))
##thread.start()

# Wait for the thread to complete
##thread.join()
##
##print("Thread execution completed")






##
##import threading
##import time
##
##def print_numbers():
##    for i in range(1, 6):
##        print("Thread 1:", i)
####        time.sleep(1)
##
##def print_letters():
##    for letter in ['A', 'B', 'C', 'D', 'E']:
##        print("Thread 2:", letter)
####        time.sleep(1)
##
### Create two threads
##thread1 = threading.Thread(target=print_numbers)
##thread2 = threading.Thread(target=print_letters)
##
### Start the threads
##thread1.start()
##thread2.start()
##
##
##### Wait for the threads to complete
##thread1.join()
##thread2.join()
##
##print("Program execution completed.")




##import threading
##import time
##def print_numbers():
##    for i in range(1, 6):
##        print("Thread 1:", i)
##        print(time.ctime())
####        time.sleep(1)
##
##def print_letters():
##    for letter in ['A', 'B', 'C', 'D', 'E']:
##        print("Thread 2:", letter)
##        print(time.ctime())
##
##thread1=threading.Thread(target=print_numbers)
##thread2=threading.Thread(target=print_letters)
##
##thread1.start()
##thread2.start()
##
##thread1.join()
##thread2.join()



##import threading
##import time
##
##def print_message(name,delay):
##    time.sleep(delay)
##    print(name)
##    print(time.ctime())
##
##thread1 = threading.Thread(target=print_message,args=("bharani",2))
##thread2 = threading.Thread(target=print_message,args=("ganesan",4))
##thread1.start()
##thread2.start()
##thread1.join()
##thread2.join()





##import threading
##import time
##count = 0
##
##def count_up(delay):
##    global count
##    while count < 10:#execute a statement as long as condition is true.
##        time.sleep(2)
##        count += 1
##        print("Count:", count)
##
##thread1 = threading.Thread(target=count_up)
##thread2 = threading.Thread(target=count_up)
##
##thread1.start()
##thread2.start()
##
##thread1.join()
##thread2.join()
##
##print("Program execution completed.")





##
##
##import threading
##import time
##
##def print_message(name,age,delay):
##    time.sleep(delay)
##    print(name)
##    print(age)
##    print(time.ctime())
##
##thread1 = threading.Thread(target=print_message,args=("bharani",2,4))
##thread2 = threading.Thread(target=print_message,args=("ganesan",4,5))
##thread1.start()
##thread2.start()
##thread1.join()
##thread2.join()







##import threading
##import time
##count = 0
##
##def count_up():
##    global count
##    while count < 10:#execute a statement as long as condition is true.
##        time.sleep(2)
##        count += 1
##        print("Count:", count)
##
##thread1 = threading.Thread(target=count_up)
##thread2 = threading.Thread(target=count_up)
##
##thread1.start()
##thread2.start()
##
##thread1.join()
##thread2.join()
##
##print("Program execution completed.")



