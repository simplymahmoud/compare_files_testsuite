from base import BaseTest
import uuid
import os


class UnitTests(BaseTest):        

    def test001_check_file_with_non_exists(self):
        '''UT-1: Test (check_file) method with non exists file'''
        self.assertRaises(AssertionError, 
                          self.check_file,
                          str(uuid.uuid4()))

    def test002_check_file_with_non_file(self):
        '''UT-2: Test (check_file) method with non file'''
        filename = str(uuid.uuid4())
        os.makedirs(filename)
        self.folder_to_be_deleted = filename
        self.assertRaises(AssertionError, 
                          self.check_file,
                          filename)

    def test003_check_file_with_valid_file(self):
        '''UT-3: Test (check_file) method with valid file'''
        filename, _ = self._create_file()
        self.check_file(filename)

    def test004_get_file_size_small(self):
        '''UT-4: Test (get_file_size) method with small file size'''
        filename, size = self._create_file(10)
        actual_size = self.get_file_size(filename)
        self.assertEqual(actual_size, size + 2)

    def test005_get_file_size_big(self):
        '''UT-5: Test (get_file_size) method with big file size'''
        filename, size = self._create_file(102400)
        actual_size = self.get_file_size(filename)
        self.assertEqual(actual_size, size)

    def test006_hashlib_comparative_with_different_files_same_size(self):
        '''UT-6: Test (hashlib_comparative) method with different files but same size'''
        first_filename, _ = self._create_file(100)
        second_filename, _ = self._create_file(100)
        self.assertFalse(self.hashlib_comparative(first_filename, second_filename))

    def test007_hashlib_comparative_with_different_files_different_size(self):
        '''UT-7: Test (hashlib_comparative) method with different files and different size'''
        first_filename, _ = self._create_file(100)
        second_filename, _ = self._create_file(200)
        self.assertFalse(self.hashlib_comparative(first_filename, second_filename))

    def test008_hashlib_comparative_with_same_files(self):
        '''UT-8: Test (hashlib_comparative) method with same files and same size'''
        filename, _ = self._create_file()
        self.assertTrue(self.hashlib_comparative(filename, filename))
