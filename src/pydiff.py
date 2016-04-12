from sys import argv


class Pydiff():

    def __init__(self):

        if len(argv) != 3:
            raise AssertionError("Usage: ipython pydiff.py file1 file2")

        first_filename = argv[1]
        second_filename = argv[2]

        # Open file for reading in text mode (default mode)
        f1 = open(first_filename)
        f2 = open(second_filename)

        # Read the first line from the files
        f1_line = f1.readline()
        f2_line = f2.readline()

        # Initialize counter for line number
        line_no = 1
        output = open('pydiff.log', 'w')
        output.writelines('Compare result:\n')
        # Loop if either file1 or file2 has not reached EOF
        while f1_line != '' or f2_line != '':

            # Compare the lines from both file
            if f1_line != f2_line:
                # If a line does not exist on file2 then mark the output with + sign
                if f2_line == '' and f1_line != '':
                    output.writelines(">+ Line-%d " % line_no + f1_line)
                # otherwise output the line on file1 and mark it with > sign
                elif f1_line != '':
                    output.writelines("> Line-%d " % line_no + f1_line)

                # If a line does not exist on file1 then mark the output with + sign
                if f1_line == '' and f2_line != '':
                    output.writelines("<+ Line-%d " % line_no + f2_line)
                # otherwise output the line on file2 and mark it with < sign
                elif f2_line != '':
                    output.writelines("< Line-%d " %  line_no + f2_line)

            #Read the next line from the file
            f1_line = f1.readline()
            f2_line = f2.readline()


            #Increment line counter
            line_no += 1

        # Close the files
        f1.close()
        f2.close()
        output.close()
        print 'Compare result : see pydiff.log'

if __name__ == '__main__':
    Pydiff()
