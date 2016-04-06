from base import BaseTest
import uuid
import os


class IntegrationTests(BaseTest):

    def _execute_main(self, first_file, second_file):
        command = "ipython main.py %s %s" % (first_file, second_file)
        output, _ = self._execute_command(command)
        if 'AssertionError' in output:
            raise AssertionError("Execute command failed")
        return output

    def test001_with_no_files(self):
        '''IT-1: Test (main.py) without files'''
        self.assertRaises(AssertionError,
                          self._execute_main,
                          '',
                          '')

    def test002_with_one_file(self):
        '''IT-2: Test (main.py) with one file'''
        filename, _ = self._create_file()
        self.assertRaises(AssertionError,
                          self._execute_main,
                          filename,
                          '')

    def test003_with_non_exists_first_file(self):
        '''IT-3: Test (main.py) with non exists first file'''
        first_filename = str(uuid.uuid4())
        second_filename, _ = self._create_file()
        self.assertRaises(AssertionError,
                          self._execute_main,
                          first_filename,
                          second_filename)

    def test004_with_non_exists_second_file(self):
        '''IT-4: Test (main.py) with non exists second file'''
        first_filename, _ = self._create_file()
        second_filename = str(uuid.uuid4())
        self.assertRaises(AssertionError,
                          self._execute_main,
                          first_filename,
                          second_filename)

    def test005_with_non_file_first_file(self):
        '''IT-5: Test (main.py) with non first file (folder)'''
        first_filename = str(uuid.uuid4())
        os.makedirs(first_filename)
        self.folder_to_be_deleted = first_filename
        second_filename, _ = self._create_file()
        self.assertRaises(AssertionError,
                          self._execute_main,
                          first_filename,
                          second_filename)

    def test006_with_non_file_second_file(self):
        '''IT-6: Test (main.py) with non second file (folder)'''
        first_filename, _ = self._create_file()
        second_filename = str(uuid.uuid4())
        os.makedirs(second_filename)
        self.folder_to_be_deleted = second_filename
        self.assertRaises(AssertionError,
                          self._execute_main,
                          first_filename,
                          second_filename)

    def test007_with_non_exists_first_second_file(self):
        '''IT-7: Test (main.py) with non exists first and second file'''
        first_filename = str(uuid.uuid4())
        second_filename = str(uuid.uuid4())
        self.assertRaises(AssertionError,
                          self._execute_main,
                          first_filename,
                          second_filename)

    def test008_with_non_file_first_second_file(self):
        '''IT-8: Test (main.py) with non file first and second (folder)'''
        first_filename = str(uuid.uuid4())
        os.makedirs(first_filename)
        self.folder_to_be_deleted = first_filename
        self.assertRaises(AssertionError,
                          self._execute_main,
                          first_filename,
                          first_filename)

    def test009_with_different_files_same_small_size(self):
        '''IT-9: Test (main.py) with different files same small size'''
        first_filename, _ = self._create_file(100)
        second_filename, _ = self._create_file(100)
        self.assertRaises(AssertionError,
                          self._execute_main,
                          first_filename,
                          second_filename)

    def test010_with_different_files_same_big_size(self):
        '''IT-10: Test (main.py) with different files same big size'''
        first_filename, _ = self._create_file(102400)
        second_filename, _ = self._create_file(102400)
        self.assertRaises(AssertionError,
                          self._execute_main,
                          first_filename,
                          second_filename)

    def test011_different_files_different_small_size(self):
        '''IT-11: Test (main.py) with different files different small size'''
        first_filename, _ = self._create_file(100)
        second_filename, _ = self._create_file(200)
        self.assertRaises(AssertionError,
                          self._execute_main,
                          first_filename,
                          second_filename)

    def test012_different_files_different_big_size(self):
        '''IT-12: Test (main.py) with different files different big size'''
        first_filename, _ = self._create_file(51200)
        second_filename, _ = self._create_file(102400)
        self.assertRaises(AssertionError,
                          self._execute_main,
                          first_filename,
                          second_filename)

    def test013_different_files_different_small_and_big_size(self):
        '''IT-13: Test (main.py) with different files different small and big size'''
        first_filename, _ = self._create_file(51200)
        second_filename, _ = self._create_file(100)
        self.assertRaises(AssertionError,
                          self._execute_main,
                          first_filename,
                          second_filename)

    def test014_with_same_files(self):
        '''IT-14: Test (main.py) with same files'''
        filename, _ = self._create_file()
        self._execute_main(filename, filename)
