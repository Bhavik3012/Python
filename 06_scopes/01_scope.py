username = "chaiaurcode"


def test(username):
    print("Inside test function:", username)

    def inner_test(name):
        print("Inside inner_test function:", name)

    inner_test(username)


test(username)


x = 99


# def func(y):
#     z = x + y
#     return z


# result = func(1)
# print("Result of func(1):", result)


def func2():
    global x
    x += 1
    return x


result2 = func2()
print("Result of func2():", result2)
print("Global x after func2():", x)


# def f1():
#     x = 88

#     def f2():
#         print(x)

#     return f2()


# myresult = f1()
# myresult()


def chaicode(num):
    def actual(x):
        return x**num

    return actual


f = chaicode(2)
g = chaicode(3)

print(f(2))
