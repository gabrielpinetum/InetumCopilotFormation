
class PowerFiveMeta(type):
    def __new__(meta, name, bases, class_dict):
       
        cls = super(PowerFiveMeta, meta).__new__(meta, name, bases, class_dict)
        original_mul = cls.__mul__

        
        def new_mul(self, other):
            result = original_mul(self, other)
            return result ** 5

      
        cls.__mul__ = new_mul
        return cls


class CustomNumber(metaclass=PowerFiveMeta):
    def __init__(self, value):
        self.value = value

    def __mul__(self, other):
        if isinstance(other, CustomNumber):
            return CustomNumber(self.value * other.value)
        else:
            raise ValueError("Can only multiply with another CustomNumber")

    def __repr__(self):
        return f"CustomNumber({self.value})"


num1 = CustomNumber(2)
num2 = CustomNumber(3)
result = num1 * num2
print(result)