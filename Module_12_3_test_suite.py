import unittest
import Module_12_1
import Module_12_2
import Module_12_4_tests_logging


module_12_test_suite = unittest.TestSuite()

module_12_test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Module_12_1.RunnerTest))
module_12_test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Module_12_2.TournamentTest))
module_12_test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Module_12_4_tests_logging.RunnerTest))

tests_runner = unittest.TextTestRunner(verbosity=2)

tests_runner.run(module_12_test_suite)