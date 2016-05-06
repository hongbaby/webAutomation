import Queue
import cases


class RunTestCasesInQueue(object):

    def run_test_cases(self):
        queue = Queue.LifoQueue()
        for case in cases.test_cases:
            queue.put(case)

        for i in range(queue.qsize()):
            test_case = queue.get()
            print test_case
            test_case().runTest()


if __name__ == "__main__":
    RunTestCasesInQueue().run_test_cases()