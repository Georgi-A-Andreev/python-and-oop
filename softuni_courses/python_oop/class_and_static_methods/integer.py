from math import floor


class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if type(float_value) != float:
            return "value is not a float"
        return cls(floor(float_value))

    @staticmethod
    def roman_to_int(value):
        roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        for i in range(len(value)):
            if i > 0 and roman_numerals[value[i]] > roman_numerals[value[i - 1]]:
                result -= roman_numerals[value[i - 1]]
                result += roman_numerals[value[i]] - roman_numerals[value[i - 1]]
            else:
                result += roman_numerals[value[i]]
        return result

    @classmethod
    def from_roman(cls, value):
        result = Integer.roman_to_int(value)
        return cls(result)

    @classmethod
    def from_string(cls, value):
        if type(value) == str:
            return cls(int(value))

        return 'wrong type'


first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))



