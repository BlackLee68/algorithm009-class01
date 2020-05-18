class TestClass():
    def __init__(self):
        self._info = "Hello World"
    def show_info(self):
        print(self._info)

if __name__ == "__main__":
    test = TestClass()
    test.show_info()
