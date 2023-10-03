import unittest
import HtmlTestRunner

from tests.test_get_all_users import TestGetAllUsers
from tests.test_add_user import TestAddUser
from tests.test_get_user_details import TestGetUserDetails
from tests.test_delete_user import TestDeleteUser
from tests.test_get_my_user_details import TestGetMyUserDetails
from tests.test_delete_my_user import TestDeleteMyUser
from tests.test_check_if_my_user_was_modified import TestCheckIfMyUserWasModified
from tests.test_check_if_my_user_was_deleted import TestCheckIfMyUserWasDeleted
from tests.test_modify_my_user_email import TestModifyMyUserEmail
from tests.test_modify_my_user_status import TestModifyMyUserStatus


class TestSuiteForAllUsers(unittest.TestCase):

    def test_suite_for_all_users(self):
        teste_de_rulat_1 = unittest.TestSuite()
        teste_de_rulat_1.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestGetAllUsers),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestGetUserDetails),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestDeleteUser),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestAddUser)
        ])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title="API Users tests report",
            report_name="API Users Tests Results"
        )
        runner.run(teste_de_rulat_1)


class TestSuiteForMyUser(unittest.TestCase):

    def test_suite_for_my_user(self):
        teste_de_rulat_2 = unittest.TestSuite()
        teste_de_rulat_2.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestGetMyUserDetails),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestModifyMyUserStatus),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestModifyMyUserEmail),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestCheckIfMyUserWasModified),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestDeleteMyUser),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestCheckIfMyUserWasDeleted),
        ])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title="API My User tests report",
            report_name="API My User Tests Results"
        )
        runner.run(teste_de_rulat_2)