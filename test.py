def test(x):
    def test2(x):
        x += 1
        print x
    test2(x)
if __name__ == '__main__':
    test(1)