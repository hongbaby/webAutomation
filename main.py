import Queue
import cases


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
            execute_test_case.runTest()
            execute_test_case.quit_browser_driver()


if __name__ == "__main__":
    RunTestCasesInQueue().run_test_cases()
