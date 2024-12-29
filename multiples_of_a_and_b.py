import sys
import bisect
import numpy as np

if len(sys.argv) > 3:
    print("Too many arguments, please follow the example usage: 'python multiples_of_a_and_b.py input.txt output.txt'")
    sys.exit()

if len(sys.argv) < 3:
    print("Too few arguments, please follow the example usage: 'python multiples_of_a_and_b.py input.txt output.txt'")
    sys.exit()


def main():
    all_multiples = []
    with open(sys.argv[1], 'r') as inputfile:
        for line in inputfile:
            # Read line contents to variables
            a, b, goal = np.array(line.split(' '), dtype=int)

            # Use numpy arange to get list of multiples of a and b under goal value
            # Union of a and b lists sorts values and removes duplicates
            # Remove 0 from the multiples list
            multiples = np.delete(np.union1d(np.arange(0, goal, a), np.arange(0, goal, b)), 0)
    
            # Create a string from list items
            # Add goal and colon in front of the string
            output_line = ' '.join(str(multiple) for multiple in multiples)
            output_line = f"{goal}:{output_line}"
            all_multiples.append(output_line)
            
        write_output(all_multiples, sys.argv[2])


def write_output(data, output_file):
    data.sort(key=len)
    with open(output_file, 'a') as file:
        for line in data:
            # Print sorted console output and write to output file
            print(line)
            file.write(f"{line}\n")


if __name__ == '__main__':
    main()