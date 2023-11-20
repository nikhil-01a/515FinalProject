## Nikhil Kumar G - nkumarg@stevens.edu

## GitHub Url:
(https://github.com/nikhil-01a/Python-TestHarness)

## Estimate of how many hours you spent on the project
I usually use the pomodoro technique to estimate the amount of time I spend working on something. My each pomodoro is 20 minutes. I would say collectively and approximately I have completed 30 pomodoros of 20 minutes on this assignment. Which is equivalent of 10 hours approx collectively.

## A description of how you tested your code
1. Created a test harness:
   - In the main function: using glob to find the '.in' files in 'test' directory and passed them through the custom 'run_test()' for **STDIN** first and then for **ARGS**.
   - Collecting the 'run_test()'s return result and storing it in a custom common **results** dictionary for every test, whatever the outcome.
   - The **results** dictonary has a count of 4 tnings:
   - 1. 'OK' : If the test ran successfuly.
     2. 'TestResult.NonZeroExit' : If the test failed and exited with a sys code other than '0'.
     3. 'TestResult.OutputMismatch' : If there were no functional errors but the output got is not same as the output expected.
     4. 'TestResult.MissingOutPutFile' : If the 'expected output' file wasn't found.
   - Lastly we check if the number of 'OK's are equal to the number of tests ran. If that's the case then it means all the tests ran are passed. Otherwise the system will exit with sys.exit(1).

## Any bugs or issues you could not resolve

For my wc program I'm still trying to automate its testing for **multiple files input** in the test harness that I've created.  

## An example of a difficult issue or bug and how you resolved it

While working on gron, although the solution was easy but it was a bit tricky in the begininng to figure out why the output wasn't exactly same as the official gron output. Later I decided to order the output alphabetically. So I just sorted the keys while flattenning the json and that was resolved.

## A list of the three extensions you’ve chosen to implement, with appropriate detail on them for the CAs to evaluate them.
The three extensions I chose are:
1. wc - multiple files
2. wc - flags
3. gron - base --obj
