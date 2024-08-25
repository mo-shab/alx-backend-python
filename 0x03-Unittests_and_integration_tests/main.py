memoize = __import__('utils').memoize

class MyClass:
    @memoize
    def a_method(self):
        print("a_method called")
        return 42

a = MyClass()
print(a.a_method())