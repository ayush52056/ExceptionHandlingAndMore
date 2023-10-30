class MyClass:
    @staticmethod
    def static_method():
        print("This is a static method.")

    @classmethod
    def class_method(cls):
        print("This is a class method.")

    @property
    def prop(self):
        return "This is a property."

obj = MyClass()
obj.static_method()
obj.class_method()
print(obj.prop)
