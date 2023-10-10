Here are some API tests that I made for the final project of Automation Testing on the following endpoint: https://gorest.co.in./

The project is organized as follows:
  - the *requests_folder* which contains a *user_request* file with all the test functions for the project
  - the *tests* folder which contains 10 files with the tests for predefined users and for a created user (get informations from the server for a user, add user, delete user etc.)
  - a *user_api_test_suite* file in which I've made two test suites, one for predefined users and one for the created user
  - the *reports* folder which contains the results for the two test suites

The project can be cloned as it is, in order to test it.
Before runing the test suites, there are some things to do, like:
  - login in on https://gorest.co.in./consumer/login using an account (GitHub or Google) in order to obtain a token and replace the value of *API_TOKEN* variable from *user_request* file with this new one
  - the *get_user_details* and *delete_user* files located in *tests* folder need to be modified with a valid user name and email from https://gorest.co.in./users, because the database is changing periodically and the existing data in those files might be invalid for the tests
  - after running *TestSuiteForAllUsers* from *user_api_test_suite* file, it is mandatory to access https://gorest.co.in./users and take *Fake User1* id and replace the value of *MY_USER_ID* variable from  *user_request* file with this new one, in order to run after the *TestSuiteForMyUser*, because those tests need the user id in order to be performed

After running the two test suites, the reports are automatically generated in the *reports* folder.
