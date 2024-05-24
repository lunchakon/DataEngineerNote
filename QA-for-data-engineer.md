Given the following functions in Python: 
---
def add(a, b):
    return a + b
def mul(a, b):
    return a * b
Will this code works or breaks, and why?

Section A
functions = [add, mul]
for function in functions:
    print(function(3, 5))
Section B
def doing_something_with_four_and_six(fn):
    return fn(4, 6)

print(doing_something_with_four_and_six(mul))
---
a.
A works, B does not works. Functions can be stored in another data structures, but cannot be passed as a parameter to another function.


b.
A does not works, B does not works. Like other programming languages, functions are translated to machine codes and therefore does not really exist as an 'object' compared to other variables.

c.
A works, B works. Functions are so-called 'First Class' in Python and can be indexed or passed as parameters.


d.
A does not works, B works.. Functions cannot be passed as a parameter to another function, but can be stored in another data structures.
