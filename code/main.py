# TODO: Add more documentation
import getopt
import sys
import os

# -----------------------------------------------------------------------------------------------------
# defining all necessary parameters

# Get all arguments except the program name
argument_list = sys.argv[1:]
training_file_path = ""
number_of_threads = 1
short_sequences = True

# -----------------------------------------------------------------------------------------------------
# This section will handle all input arguments

try:
    # specify what arguments are valid and which ones need a value
    short_options = "w:p:t:"
    arguments, values = getopt.getopt(argument_list, short_options, [])

    # evaluate the correct arguments
    for current_arg, current_val in arguments:
        if current_arg == "-w":
            # This argument specifies if the user gave us short sequence reads or a while genome sequencing
            int_current_val = int(current_val)
            if 0 >= int_current_val <= 1:
                if int_current_val == 1:
                    short_sequences = False
            else:
                print("Wrong value for the -w argument, must be 0 or 1!")
                sys.exit(2)

        elif current_arg == "-p":
            # this argument will specify the amount of threads that can be used to compute the solution
            int_current_val = int(current_val)
            if int_current_val >= 1:
                number_of_threads = int_current_val
            else:
                print("Wrong value for the -p argument, must be greater or equal than 1")
                sys.exit(2)

        elif current_arg == "-t":
            # the value of this argument must be a path to a training file

            if os.path.isfile(current_val):
                training_file_path = current_val
            else:
                print("This argument must be a path to a correct training file!")
                sys.exit(2)

    # TODO: continue the program
    print("Number of threads: "), print(number_of_threads)
    print("Short sequences: "), print(short_sequences)
    print("Path to file: "), print(training_file_path)

except getopt.error as err:
    # output an error, and return an error code
    print(str(err))
    sys.exit(2)

# -----------------------------------------------------------------------------------------------------
