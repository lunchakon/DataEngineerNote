**Python for Data Engineers Review
**
What are the benefits of using Python language as a tool in the present scenario?
- Object-Oriented Languege
- High-Level Language
- Dynamically Typed language
- Extensive support Libraries
- Presence of third-party modules
- Opoen source and community devleopment
- Portable and Interactive
- Portable acrros Operating systems

Python is partially complied langueage and partially interpreted language 
THe compilation part is done first when we execute our code and this will generate byte code internally. This byte code gets converted by the Python Virtual machine(PVM) according to the underlyting platform(machine+OS).

List Comprethension : is a syntax construction to ease the creation of a list based on an existing iterable 
my_list=[i fori in rage(1,10)]


Lamda fucntion is : an anonymous fucntion. It can have any number of parameters but can have just one statement 
a = lamda x,y : x*y
print(a(4,5))
output : 20


floor division whereas 
5//2 =2

precise division 
5/2 =5/2 

Swapcase function 
s = "lunchaKon WongPrasert"
s.swapcase()
output : 'LUNCHAkON wONGpRASERT'

sort() and sorted() fucntions of python 
: Using Tim Sort algorithm for sorting, it's stable sorting whose worst case is O(N logN), it's a hybrid sorting algorithm

In Python we can use the debugger pdb for debugging the code, 
pdb.set_trace()
after address these lines, our code runs in debug mode. Now we cna use command like : breakpoint, step through, step into 
commmand : $ python -m pdb python-script.py

Delete a files using python 
os.remove()
os.unlink()


Slicing in Python 
Lst[Initial:End:IndexJump]


Map()
reduce(0
filter()

display current time : 
cur_time = time.localtime()
print("current :",cur_time)

the schedule Library:
This is a popular Python library that provides a simple interface for scheduling jobs.

===
import schedule
import time

def my_function():
    # Your script's code here

schedule.every(10).minutes.do(my_function)  # Run every 10 minutes
schedule.every().hour.do(my_function)  # Run every hour
schedule.every().day.at("10:30").do(my_function)  # Run at 10:30 AM every day

while True:
    schedule.run_pending()
    time.sleep(1)
===


