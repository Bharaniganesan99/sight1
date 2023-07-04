import threading
import time

# Sequential execution
def seq():
    print("one")
    time.sleep(2)  # Simulating some time-consuming task
    print("two")

# Multithreading execution
def multi():
    print("three")
    time.sleep(3)  # Simulating some time-consuming task
    print("four")

# Create a thread for multithreading execution
thread = threading.Thread(target=multi)

# Sequential execution
print("=== Sequential Execution ===")
start_time = time.time()

sequential_execution()
multithreading_execution()

end_time = time.time()
execution_time = end_time - start_time
print(f"Sequential execution time: {execution_time} seconds")

# Multithreading execution
print("\n=== Multithreading Execution ===")
start_time = time.time()

thread.start()
sequential_execution()

thread.join()

end_time = time.time()
execution_time = end_time - start_time
print(f"Multithreading execution time: {execution_time} seconds")
