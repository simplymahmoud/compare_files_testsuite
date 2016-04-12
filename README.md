Compare Files Test-suite
=============================
This is a test-suite that tests simple programe to compare files

Introduction
------------
Please develop a solution that compares 2 text files. The input are 2 text files, the output must inform if they are equal or not.

User Story
----------
As a user I need to compare 2 text files so that I know they are equal or not How would you go to test this solution? Could write test cases for it? Please also document your approach to solve this.

Solutions:
----------
1- using python program and tested by python (unittests and integrationtests) in folder (src).
2- using htmls5/javascript program and tested by python/selenium (seleniumtests) in folder (html/js).

Test specs
----------
Please check complete [Specs](https://docs.google.com/spreadsheets/d/1ggEjlWQWNsCzmqT1aCzxL_weYKDMkibZ-yDmpOOtu4M/pubhtml).

Quickstart
----------
To run all tests, you just need to run ./tools/run_test.sh script and like magic it will do everything for you. The script will setup virtual environment then run all tests

```
compare_files_testsuite$> tools/run_test.sh
```

Run a specific test
-------------------
Use tools/setup_env.sh to setup your virtual environment and then use nosetests to run your test

```
compare_files_testsuite$> tools/setup_env.sh
compare_files_testsuite$> venv/bin/nosetests -xv src/unittests.py
compare_files_testsuite$> venv/bin/nosetests -xv src/integrationtests.py
compare_files_testsuite$> venv/bin/nosetests -xv html-js/seleniumtests.py
```
