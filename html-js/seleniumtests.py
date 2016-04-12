from base import BaseTest
import os
from selenium import webdriver


class FileCaseStudyTest(BaseTest):
    
    def setUp(self):
        self.files_to_be_deleted = []
        self.driver = webdriver.Firefox()
	self.driver.maximize_window()
	self.driver.get("file://%s/index.html" % os.getcwd())
        
    def test001_with_different_files_same_small_size(self):
        '''IT-9: Test (index.html) with different files same small size'''
        first_file, _ = self._create_file(100)
        first_path = os.path.join(os.path.dirname(os.path.abspath(first_file)), first_file)
        second_file, _ = self._create_file(100)
        second_path = os.path.join(os.path.dirname(os.path.abspath(second_file)), second_file)
        self.driver.find_element_by_id("fileselect1").send_keys(first_path)
        self.driver.find_element_by_id("fileselect2").send_keys(second_path)
        self.driver.find_element_by_id("compare").click()        
        self.assertEqual("The two files are not identical",
                         self.driver.find_element_by_id("result").text)

    def test002_with_different_files_same_big_size(self):
        '''IT-10: Test (index.html) with different files same big size'''
        first_file, _ = self._create_file(102400)
        first_path = os.path.join(os.path.dirname(os.path.abspath(first_file)), first_file)
        second_file, _ = self._create_file(102400)
        second_path = os.path.join(os.path.dirname(os.path.abspath(second_file)), second_file)
        self.driver.find_element_by_id("fileselect1").send_keys(first_path)
        self.driver.find_element_by_id("fileselect2").send_keys(second_path)
        self.driver.find_element_by_id("compare").click()        
        self.assertEqual("The two files are not identical",
                         self.driver.find_element_by_id("result").text)

    def test003_different_files_different_small_size(self):
        '''IT-11: Test (index.html) with different files different small size'''
        first_file, _ = self._create_file(100)
        first_path = os.path.join(os.path.dirname(os.path.abspath(first_file)), first_file)
        second_file, _ = self._create_file(200)
        second_path = os.path.join(os.path.dirname(os.path.abspath(second_file)), second_file)
        self.driver.find_element_by_id("fileselect1").send_keys(first_path)
        self.driver.find_element_by_id("fileselect2").send_keys(second_path)
        self.driver.find_element_by_id("compare").click()        
        self.assertEqual("The two files are not identical",
                         self.driver.find_element_by_id("result").text)

    def test004_different_files_different_big_size(self):
        '''IT-12: Test (index.html) with different files different big size'''
        first_file, _ = self._create_file(51200)
        first_path = os.path.join(os.path.dirname(os.path.abspath(first_file)), first_file)
        second_file, _ = self._create_file(102400)
        second_path = os.path.join(os.path.dirname(os.path.abspath(second_file)), second_file)
        self.driver.find_element_by_id("fileselect1").send_keys(first_path)
        self.driver.find_element_by_id("fileselect2").send_keys(second_path)
        self.driver.find_element_by_id("compare").click()        
        self.assertEqual("The two files are not identical",
                         self.driver.find_element_by_id("result").text)

    def test005_different_files_different_small_and_big_size(self):
        '''IT-13: Test (index.html) with different files different small and big size'''
        first_file, _ = self._create_file(51200)
        first_path = os.path.join(os.path.dirname(os.path.abspath(first_file)), first_file)
        second_file, _ = self._create_file(100)
        second_path = os.path.join(os.path.dirname(os.path.abspath(second_file)), second_file)
        self.driver.find_element_by_id("fileselect1").send_keys(first_path)
        self.driver.find_element_by_id("fileselect2").send_keys(second_path)
        self.driver.find_element_by_id("compare").click()        
        self.assertEqual("The two files are not identical",
                         self.driver.find_element_by_id("result").text)

    def test006_with_same_files(self):
        '''IT-14: Test (index.html) with same files'''
        first_file, _ = self._create_file()
        first_path = os.path.join(os.path.dirname(os.path.abspath(first_file)), first_file)
        self.driver.find_element_by_id("fileselect1").send_keys(first_path)
        self.driver.find_element_by_id("fileselect2").send_keys(first_path)
        self.driver.find_element_by_id("compare").click()
        self.assertEqual("The two files are identical",
                         self.driver.find_element_by_id("result").text)     
        
    def tearDown(self):
        self.driver.quit()
        for file in self.files_to_be_deleted:
            os.remove(file)      