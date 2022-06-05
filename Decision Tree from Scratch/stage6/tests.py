from hstest import *


ANSWER = [0.583, 0.903]


class Eval1Test(StageTest):

    @dynamic_test
    def test(self):
        pr = TestedProgram()
        pr.start()
        if not pr.is_waiting_input():
            raise WrongAnswer("You program should input two paths to the files split by space")
        output = pr.execute("test/data_stage6_train.csv test/data_stage6_test.csv").strip()
        res = [round(float(x), 3) for x in output.split()]
        if len(res) != 2:
            raise WrongAnswer("Wrong number of values. Print two numbers: true positives and true negatives normalized over the true rows.")
        if res[0] != ANSWER[0]:
            raise WrongAnswer("Wrong true positives value (the first value).")
        if res[1] != ANSWER[1]:
            raise WrongAnswer("Wrong true negatives value (the second value).")
        return CheckResult.correct()


if __name__ == '__main__':
    Eval1Test().run_tests()

