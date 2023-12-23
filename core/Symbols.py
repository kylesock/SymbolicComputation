from Fields import Field


class Symbol:
    def __init__(self,
                 name: str,
                 domain: Field | None = None,
                 value: float | None = None) -> None:
        self.name = name
        self.domain = domain
        self.value = value

    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.__repr__()


if __name__ == '__main__':
    X = Symbol('X')
    print(f'Value: {X}')