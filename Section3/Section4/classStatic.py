class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f'<FixedFloat {self.amount:.2f}>'

    # @staticmethod
    # def from_sum(val, val2):
    #     return FixedFloat(val + val2)
    #
    # # # Output
    # # # < FixedFloat 18.35 >
    # # # < FixedFloat 21.90 >
    # # # < FixedFloat 24.56 >

    @classmethod
    def from_sum(cls, val, val2):
        return cls(val + val2)

    # Output
    # < FixedFloat 18.35 >
    # < FixedFloat 21.90 >
    # < Euro E 24.5572 >


number = FixedFloat(18.3455)
print(number)

new_number = FixedFloat.from_sum(19.345, 2.56)
print(new_number)


class Euro(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = 'E'

    def __repr__(self):
        return f'<Euro {self.symbol} {self.amount}>'


money = Euro.from_sum(12.234, 12.3232)
print(money)


