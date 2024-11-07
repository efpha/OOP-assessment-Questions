# Static Methods and Attributes
class Calculator:
    count = 0

    @staticmethod
    def add(a, b):
        Calculator.count += 1
        return a + b

result = Calculator.add(5, 3)
print("Sum:", result)
print("Add method called:", Calculator.count, "times")
