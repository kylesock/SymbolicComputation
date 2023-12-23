RealType = float
IntegerType = int
NumberType = RealType | IntegerType
FieldValueType = tuple | NumberType


class Field:

    def __init__(self, name: str, value: FieldValueType):
        self.name = name
        self.value = value
        self.validate()

    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.__repr__()

    def validate(self):
        pass


class Integer(Field):

    def __init__(self, value: IntegerType):
        super().__init__('Integer', value)

    def __repr__(self) -> str:
        return f'{self.value}'

    def __str__(self) -> str:
        return super().__str__()

    def validate(self):
        assert isinstance(self.value, IntegerType), f'Value {self.value} must be of type int, got {type(self.value)}.'


class Real(Field):

    def __init__(self, value: RealType):
        super().__init__('Real', value)

    def __repr__(self) -> str:
        return f'{self.value}'

    def __str__(self) -> str:
        return super().__str__()

    def validate(self):
        assert isinstance(self.value, NumberType), f'Value {self.value} must be of type int | float, ' \
                                                    f'got {type(self.value)}. '


class Complex(Field):

    def __init__(self, value: tuple[NumberType, NumberType]):
        super().__init__('Complex', value)

    def __repr__(self) -> str:
        return f'{self.value[0]} + {self.value[1]}i'

    def __str__(self) -> str:
        return super().__str__()

    def validate(self):
        assert isinstance(self.value, tuple), f'Value {self.value} must be of type tuple, ' \
                                                    f'got {type(self.value)}. '
        for item in self.value:
            assert isinstance(item, NumberType), f'Value {self.value} must be of type int | float, ' \
                                                    f'got {type(self.value)}. '


class Quaternion(Field):

    def __init__(self, value: tuple[NumberType, NumberType, NumberType, NumberType]):
        super().__init__('Complex', value)

    def __repr__(self) -> str:
        return f'{self.value[0]} + {self.value[1]}i + {self.value[2]}j + {self.value[3]}k'

    def __str__(self) -> str:
        return super().__str__()

    def validate(self):
        assert isinstance(self.value, tuple), f'Value {self.value} must be of type tuple, ' \
                                                    f'got {type(self.value)}. '
        for item in self.value:
            assert isinstance(item, NumberType), f'Value {self.value} must be of type int | float, ' \
                                                    f'got {type(self.value)}. '


if __name__ == '__main__':
    complex_field = Complex((3, 2))
    print(f'Field Name: {complex_field.name}')
    print(f'Field Expr: {complex_field}')

    real_field = Real(4.0)
    print(f'Field Name: {real_field.name}')
    print(f'Field Expr: {real_field}')

    integer_field = Integer(4)
    print(f'Field Name: {integer_field.name}')
    print(f'Field Expr: {integer_field}')

    quaternion_field = Quaternion((1, 2, 3, 4))
    print(f'Field Name: {quaternion_field.name}')
    print(f'Field Expr: {quaternion_field}')
