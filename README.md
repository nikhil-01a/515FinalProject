## Nikhil Kumar G - nkumarg@stevens.edu

## GitHub Url:
(https://github.com/nikhil-01a/Python-TestHarness)

## Estimate of how many hours you spent on the project
I usually use the pomodoro technique to estimate the amount of time I spend working on something. My each pomodoro is 20 minutes. I would say collectively and approximately I have completed 30 pomodoros of 20 minutes on this assignment. Which is equivalent of 10 hours approx collectively.

## Description of how I tested the code using the Test Harness
1. **Test Harness Description**: **test.py**:
   - In the main function: I'm using glob to find the '.in' files in 'test' directory and passed them through the custom 'run_test()' for **STDIN** first and then for **ARGS**.
   - I have created a custom results dictionary to store the overall results. The **results** dictonary keeps a count of 4 things and increments the values inside it accordingly for every test:
   - 1. 'OK' : If the test ran successfuly.
     2. 'TestResult.NonZeroExit' : If the test failed and exited with a sys code other than '0'.
     3. 'TestResult.OutputMismatch' : If there were no functional errors but the output got is not same as the output expected.
     4. 'TestResult.MissingOutPutFile' : If the 'expected output' file wasn't found.
   - I then collect the 'run_test()'s return result for every test and update the results dictionary.
   - Lastly I'm checking if the number of 'OK's are equal to the number of tests ran. If that's the case then it means all the tests ran are passed. Otherwise the system will exit with sys.exit(1).
   - **Runtest()** : In the runtest(), based on the program name and test name, I'm finding the input file and by using 'subprocess' I'm running the input file and storing its result. Then, I'm reading the corresponding 'expected **.out** file' for it and comparing it with the 'result' stored to see if they match. If they match then the test ran successfully.
     
2. **Test Cases Guide**: in **test** directory:
   - Here's a guide to store the test cases with proper naming convention so that our test harness **test.py** picks the files up without any error. 
   - This directory has the ***'.in'*** and ***'.out'*** files that are used by the **RunTest()**.
   - Below we see naming conventions of normal test files, which are the **general** tests and then the naming conventions of the file for the **extensions** test. By storing the files with the below naming conventions you can run the tests for any program using the test harness.
   - 1. Normal Tests: The naming convention format of the test files is as follows:
        - **progName.testName.in** = input file
        - **progName.testName.arg.out** = arg expected ouput file
        - **progName.testName.out** = expect output file for 'STDIN' case.
   - 2. Extension 1: wc 'multiple input' test files
        - **wc.testName.part1.in** = input file 1
        - **wc.testName.part2.in** = input file 2
        - **wc.testName.arg.out** = arg expected ouput file
        - **wc.testName.out** = expect output file for 'STDIN' case.
   - 3. Extension 2: wc 'flag input' test files. Here **'l'**, **'c'** and **'w'** in the file names are important to recognize the flag operations. Also, the flags can be combined as well: **'lw'**. 
        - **wc.testNamel.in** = input file
        - **wc.testNamel.arg.out** = arg expected ouput file
        - **wc.testNamel.out** = expect output file for 'STDIN' case.
        - And so on.. for **'c'** and **'w'**. And a combination is also allowed similarly: like **'lw'**.
   - 4. Extension 3: gron 'custom base object' test files. Here **'objName'** will be our custom base object name.
        - **gron.testNameObj_objName.in** = input file
        - **gron.testNameObj_objName.arg.out** = arg expected ouput file
        - **gron.testNameObj_objName.out** = expect output file for 'STDIN' case.

## Any bugs or issues you could not resolve

For my wc program I'm still trying to automate its testing for **multiple files input** in the test harness that I've created.  

## An example of a difficult issue or bug and how you resolved it

While working on gron, although the solution was easy but it was a bit tricky in the begininng to figure out why the output wasn't exactly same as the official gron output. Later I decided to order the output alphabetically. So I just sorted the keys while flattenning the json and that was resolved.

## A list of the three extensions you’ve chosen to implement, with appropriate detail on them for the CAs to evaluate them.
The three extensions I chose are:
1. **wc** - multiple files:
2. - desc:
   - testing manually:
   - testing using test harness:
3. **wc** - flags to control output:
   - desc:
   - testing manually:
   - testing using test harness:
4. **gron** - control the base-object name:
   - desc:
   - testing manually:
   - testing using test harness:
   
