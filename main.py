import Queue
import cases
import os
from common.logging_file import Logging


class RunTestCasesInQueue(object):

    @staticmethod
    def run_test_cases():
        queue = Queue.LifoQueue()
        for case in cases.test_cases:
            queue.put(case)

        for i in range(queue.qsize()):
            test_case = queue.get()
            execute_test_case = test_case()

            execute_test_case.create_browser_driver()

            logger, log_file_full_name = Logging().create_logger(test_case.__name__, "./", "testdemo.log")
            execute_test_case.logger = logger
            execute_test_case.runTest()
            execute_test_case.quit_browser_driver()


if __name__ == "__main__":
    RunTestCasesInQueue().run_test_cases()
