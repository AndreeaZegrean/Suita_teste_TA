import unittest

import HtmlTestRunner
from Suita_teste.Sesiune11 import TestElefant
from Suita_teste.Sesiune12 import Test_JavaScript_Alerts


class My_Test_Suite(unittest.TestCase):
    def test_suite(self):
        Teste_de_rulat = unittest.TestSuite()
        Teste_de_rulat.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestElefant),
            unittest.defaultTestLoader.loadTestsFromTestCase(Test_JavaScript_Alerts)
        ])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports = True,
            report_title = 'Unit Tests Rezults',
            report_name = 'unittest_report'
        )
        runner.run(Teste_de_rulat)