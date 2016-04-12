from base import BaseTest
from sys import argv


class Main(BaseTest):

    def __init__(self):

        if len(argv) != 3:
            raise AssertionError("Usage: ipython main.py file1 file2")

        first_filename = argv[1]
        second_filename = argv[2]

        self.check_file(filename=first_filename)
        self.check_file(filename=second_filename)

        # Print confirmation
        print "-----------------------------------"
        print "Comparing files  > " + first_filename + " < " + second_filename
        print "-----------------------------------"

        if self.get_file_size(filename=first_filename) == self.get_file_size(filename=second_filename):
            if not self.hashlib_comparative(first_filename=first_filename, second_filename=second_filename):
                raise AssertionError('Compare result : Files are not equal in md5sum, '
                                     'check the diff using ipython pydiff.py file1 file2')

            else:
                print 'Compare result : Both files are equal'

        else:
            raise AssertionError('Compare result : Files are not equal in size, '
                                 'check the diff using ipython pydiff.py file1 file2')

if __name__ == '__main__':
    Main()
