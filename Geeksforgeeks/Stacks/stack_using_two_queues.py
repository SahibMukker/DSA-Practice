'''
Implement a Stack using two queues q1 and q2.
Ex. 
Input:
push(2)
push(3)
pop()
push(4)
pop()
Output: 3 4
Explanation:
push(2) stack will be [2]
push(3) stack will be [2 3]
pop()   popped element will be 3 the stack will be [2] 
push(4) the stack will be [2 4]
pop()   popped element will be 4

Time Complexity: O(n) for push() and O(1) for pop() (or vice-versa).
Auxiliary Space: O(1) for both push() and pop().

Worked on for 43 mins, cannot get answer
'''

'''
    :param x: value to be inserted
    :return: None

    queue_1 = Queue() # first queue
    queue_2 = Queue() # second queue
   '''
from queue import Queue

queue_1 = Queue()
queue_2 = Queue()

def push(x):
    global queue_1
    global queue_2
    
    # add element to queue 2 using put function from Queue class
    queue_2.put(x)
    
    # iterate while queue 1 isnt empty and put the elements of queue 1 into queue 2
    while not queue_1.empty():
        queue_2.put(queue_1.get())
    
    # swap the elements from both queues
    queue_1, queue_2 = queue_2, queue_1

def pop():
    global queue_1
    global queue_2
    
    # if queue 1 is empty return 1, if not then then return the element left in queue 1(the one that got popped)
    if queue_1.empty():
        return -1

    return queue_1.get()
