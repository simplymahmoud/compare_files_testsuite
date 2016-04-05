import os
import subprocess
from subprocess import PIPE
import hashlib
import unittest
import uuid
import random

class BaseTest(unittest.TestCase):

    def setUp(self):
        self.files_to_be_deleted = []

    def _execute_command(self, command):
        output, error = subprocess.Popen([command], shell=True, stdout=PIPE, stderr=PIPE).communicate()
        return (output, error)

    def _create_file(self, size=0, unit='K'):
        filename = str(uuid.uuid4())
        size = size or random.randrange(10, 500)
        command = "dd if=/dev/urandom of=%s count=%s bs=1%s" % (filename, size, unit)
        self._execute_command(command)
        self.files_to_be_deleted.append(filename)
        return filename, size

    def check_file(self, filename):
        if not os.path.exists(filename):
            raise AssertionError("Entered file is not exists, please try again")
        if not os.path.isfile(filename):
            raise AssertionError("Entered file is not a file, please try again")

    def get_file_size(self, filename):
        command = "du -s %s" % filename
        output, _ = self._execute_command(command)
        return int(output.split('\t')[0])

    def hashlib_comparative(self, first_filename, second_filename):
        first_file = open(first_filename, 'rb')
        first_output = hashlib.md5(first_file.read()).hexdigest()
        first_file.close()

        second_file = open(second_filename, 'rb')
        second_output = hashlib.md5(second_file.read()).hexdigest()
        second_file.close()
        if first_output != second_output:
            return False
        else:
            return True

    def tearDown(self):
        for file in self.files_to_be_deleted:
            os.remove(file)
        if hasattr(self, 'folder_to_be_deleted') and self.folder_to_be_deleted:
            os.rmdir(self.folder_to_be_deleted)