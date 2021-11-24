class Fibonacci:
    def __init__(self, count):
        self.n = count

    def fib(self):
        arr = ['0', '1']
        i = 2
        while True:
            sum = self.strings(arr[i - 2], arr[i - 1])
            if len(str(sum)) > self.n:
                return arr
            arr.append(sum)
            i += 1

    @staticmethod
    def strings(str1, str2):
        result = ''
        extra = 0
        str1, str2 = str(str1), str(str2)
        i1, i2 = len(str1) - 1, len(str2) - 1
        while i1 >= 0 or i2 >= 0:
            s = extra
            if i1 >= 0:
                s += int(str1[i1])
            if i2 >= 0:
                s += int(str2[i2])
            if s < 10:
                result = str(s) + result
                extra = 0
            else:
                result = str(s - 10) + result
                extra = 1
            i1 -= 1
            i2 -= 1
        if extra == 1:
            return str(extra) + result
        return result


def main():
    n = int(input("enter the count of characters: "))
    if 0 < n <= 100:
        a = Fibonacci(n)
        print(a.fib())
        input()
    else:
        print("the number must be >0 and <100")
        main()


main()
