
def fibo() -> None:
    def fibonacci(n):
        """
        Fibonacci ketma-ketligini yaratadi

        n (int): Fibonaccida nechta element bo'lishi kerakligini ko'rsatadi

        Yields:
        int: Fibonacci ketma-ketligidagi navbatdagi son
        """


        a, b, i = 0, 1, 0
        while i < n:
            yield a
            a, b = b, a + b
            i += 1


    x = fibonacci(10)
    for i in x:
        print(i)

    yana: str = input("""Davom ettirmoqchimisiz
    1.> Ha
    2.> Yoq
            >>> : """)
    if yana == '1':
        return running()
    elif yana == '2':
        return





def task1() -> object:
    yield 'task1'


def task2() -> object:
    yield 'task2'


def task3() -> object:
    yield 'task3'


def next1() -> object:
    yield 'next'


def run():
    yield task1()
    yield next1()
    yield task2()
    yield next1()
    yield task3()


def generator() -> None:
    for i in run():
        for j in i:
            print(j)
    yana: str = input("""Davom ettirmoqchimisiz
    1.> Ha
    2.> Yoq
            >>> : """)
    if yana == '1':
        return running()
    elif yana == '2':
        return


def running() -> None:
    tanla: str = input("""
    1.> Fibonachi (generator)
    2.> Generator
            >>> : """)
    if tanla == '1':
        return fibo()
    elif tanla == '2':
        return generator()
    else:
        print('Xatolik')
        return running()


running()