# postfix-python

It's important to note that this python code is intended to be used with Scribbler 2 robots, hence some of the strange commands.

Assignment: "Postfix Python"

In this lab, we will create a new programming language for controlling our robots. The language will be similar to Reverse Polish Notation (RPN)1. In reverse polish notation, rather than putting the mathematical operators between the operands (i.e. infix) we put them after the operands (i.e. postfix). For example, 3 + 2 is represented by 3 2 + and (3 + 2) / 4 is represented by 3 2 + 4 /. Other than being a little strange, this notation makes writing computer programs to evaluate these expressions simpler and we don’t
need parentheses. The programming languages Forth, Postscript, and Joy all use postfix notation. Other languages, like Lisp, use prefix notation.

Your language should have the following functionality:

1. A display command for printing out values.

2. The ability to perform simple mathematical expressions (+, -, /, *, **).
 
3. Simple forward, backward, turnRight, turnLeft, beep commands.

4. Commands for reading the sensors (e.g. getLeftLight, getRightIR getBattery).

5. Commands for taking and showing pictures.

6. A read command that reads a list of commands from a file (it’s name is specified as a parameter).

7. Lines starting with the # character should be treated as comments and ignored.

8. EXTRA: You might extend your language with pop, dup, swap commands that remove the top item on the stack, duplicate the top item on the stack, and swap the top two items on the stack, respectively.

Submit two files:

1. Your interpreter

2. An example program using all your language’s features.
