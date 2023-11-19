import os
import sys
import subprocess
import glob


def run_test(prog, test_name, use_arg=False):
    input_file = f"test/{prog}.{test_name}.in"
    expected_output_file = f"test/{prog}.{test_name}{'.arg.out' if use_arg else '.out'}"

    with open(input_file, 'r') as infile:
        if use_arg:
            result = subprocess.run(
                ['python', f'prog/{prog}.py', input_file], stdout=subprocess.PIPE, text=True)
        else:
            result = subprocess.run(
                ['python', f'prog/{prog}.py'], stdin=infile, stdout=subprocess.PIPE, text=True)

    if result.returncode != 0:
        return "TestResult.NonZeroExit"

    try:
        with open(expected_output_file, 'r') as outfile:
            expected_output = outfile.read()
    except FileNotFoundError:
        return "TestResult.MissingOutputFile"

    if result.stdout != expected_output:
        return f"TestResult.OutputMismatch\nexpected:\n{expected_output}\n\ngot:\n{result.stdout}"

    return "OK"


def main():
    test_files = glob.glob('test/*.in')
    results = {"OK": 0, "TestResult.OutputMismatch": 0,
               "TestResult.NonZeroExit": 0, "TestResult.MissingOutputFile": 0}

    for test_file in test_files:
        basename = os.path.basename(test_file)
        prog, test_name = basename.split('.')[0], basename.split('.')[1]

        # Run test in STDIN mode
        result = run_test(prog, test_name)
        results[result] += 1
        if result != "OK":
            print(f"FAIL: {prog} {test_name} failed ({result})")

        # Run test in argument mode
        result_arg = run_test(prog, test_name, use_arg=True)
        results[result_arg] += 1
        if result_arg != "OK":
            print(
                f"FAIL: {prog} {test_name} failed in argument mode ({result_arg})")

    # Print summary
    print("\nOK:", results["OK"])
    for key, value in results.items():
        if key != "OK":
            print(f"{key}: {value}")
    print("total:", sum(results.values()))

    # Exit with non-zero status if any tests failed
    if sum(results.values()) - results["OK"] > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
