class FizzBuzz:
    start = 1
    stop = 100
    factor_1 = 3
    factor_2 = 5
    word_1 = "Fizz"
    word_2 = "Buzz"

    def __init__(self, *args, **kwargs):
        self.start = kwargs.get("start", self.start)
        self.stop = kwargs.get("stop", self.stop) + 1  # non inclusive
        self.factor_1 = kwargs.get("factor_1", self.factor_1)
        self.factor_2 = kwargs.get("factor_2", self.factor_2)
        self.word_1 = kwargs.get("word_1", self.word_1)
        self.word_2 = kwargs.get("word_2", self.word_2)

    def get_line(self, x):
        line = ""
        if x % self.factor_1 == 0:
            line += self.word_1
        if x % self.factor_2 == 0:
            line += self.word_2
        if not line:
            line = str(x)
        return line

    def get_lines(self):
        return [self.get_line(x) for x in range(self.start, self.stop)]

    def get_output(self):
        return "\n".join(self.get_lines())

    def print(self):
        print(self.get_output())
