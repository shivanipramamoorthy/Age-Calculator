# Age-Calculator
First, we have the line "import tkinter as tk" whihc imports the tkinter library but in a shorter term.
"from date import datetime" means we are importing the datetime functions.
Line 3 is a definition of out new function called "calculate age".
Then, in line 4 we create a variable called "birth_year" wihch we take from input1(later shown)
In lines 5-9, we have a sequence of functions/code under something called "try" and hat we are doing within this is we are configuring our birthyear and the current year and subracting that so we can configure the variable "age" as your age.
In lines 10-11, we are making a value error, so if you enter anything but a year it would display the message "please enter a valid year"
In lines 12-14, we are creating the window called "calculator", which is where all our code occurs in to display a window.
In lines 15-16, we create label1, which is our title on the page, and then we place it with y being 70
Again, in lines 17-18 we have our first input, where you input your birthyear so that you can calculate your age. This plays a role in collectiong your birth year so then we can calculate your age(see line 5 of this readme)
in lines 19-20, we configure our button, which you click on to get your output. THis has the command "calculate_age" programmed into it so when clicked, it will configure the variable age and show your output.
And then, in lines 21-22, we have our "age" label, which we configure it's text within the lines of the code 4-9.
Finally, we see a function that says "calculator.mainloop()" this ensures that the window stays running in front or your sight. Without this, the window would appear and dissapear in a blink of time.
