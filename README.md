# AppliedStatsReader
A short little program that I quickly drew up for my AMAT465 class. I use this program in order to help get through calculations faster in my homework with large datasets.

Well, you must know that this program uses a very specific type of file in a specific format (It's the way the CD came, sue them...not me.)
The format for a text file is as follows:


 Y-var    X-var

Notice how there is one space, then the Y variable, then 3 spaces followed by the X-variable...

Okay!

Now onto commands.

python reader.py help

Opens me!

python reader.py inputfile print-table

This command prints the table in the file that you inputted

python reader.py inputfile print-results

This command prints the results from the file, including sum of squares, a linear regression function, SSE, etc.

python reader.py inputfile X expected_x_value

Here, you can enter an x value, and the output is the expected y value that corresponds to the given regression function.

