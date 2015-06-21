__author__ = 'tkessler'

"""
When we call odd(), the lambda function that evaluates variable "c" is passed into the array,
and not the value of "c" itself. The value of c has been set to its last value, in the "odd()"
for loop, which is the "g" of the string. This value is then preserved for the generated
lambdas in the "odd()" function.

Therefore, in the second "for func" loop, calling "func()" evaluates each lambda, but the
retained value of "c" is now "g" at this point, resulting in it being evaluated.

Variable "c" is in essence a shared memory object between the lambda and the function that
generates it.

"""

def odd():
    funcs = []
    for c in 'abcdefg':
        funcs.append((lambda: c)) # we append the lambda "call" to the funcs
        # this generates lambda functions for "c", and not of the value it represents
    return funcs

for func in odd(): #odd is called, so for loop evaluates, "lambda c" and not the value of "c"
    print(func(), end=' ') # we call each lambda at this point, which evaluates to the last "c" in the string.

print("\n")

"""
This fixes the issue by preserving the value of "c" in the scope of the lambda function so
when it is called, it will evaluate at the preserved value instead of the final value of "c"

"""

def odd2():
    funcs = []
    for c in 'abcdefg':
        funcs.append((lambda x=c: x)) # we now preserve the value of "c" for each lambda (see guigenerator.py)
        # when lambda is called, its local argument "x" will have been
        # set to the value of "c" in the for loop's scope

        #...may also see (lambda c=c: c)...but this is more confusing.
    return funcs

for func in odd2():
    print(func(), end=' ')
