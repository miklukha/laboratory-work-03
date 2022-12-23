# Modify the class Rational of Lab No1 to perform the following tasks:
# - adding two Rational numbers. The result should be stored in reduced form;
# - subtracting two Rational numbers. The result should be stored in reduced form;
# - multiplying two Rational numbers. The result should be stored in reduced form;
# - dividing two Rational numbers. The result should be stored in reduced form;
# - comparison two Rational numbers.

import math


class Rational:
    divider = 1

    def __init__(self, a=0, b=0, c=0, d=0):
        self.rationals = [{"id": 1, "numerator": int(a), "denominator": int(b), "floating_f": 0.0, "fractional_f": ''},
                          {"id": 2, "numerator": int(c), "denominator": int(d), "floating_f": 0.0, "fractional_f": ''}]

    def __getattr__(self, atr_name):
        return 'Something wrong...'

    def count_formats(self):
        for number in self.rationals:
            number["numerator"], number["denominator"] = self.fractional_format(number['numerator'],
                                                                                number['denominator'])
            number["fractional_f"] = f"{number['numerator']}/{number['denominator']}"
            number["floating_f"] = self.floating_point_format(number['numerator'], number['denominator'])

            print(f"Number in fractional format: {number['fractional_f']}")
            print(f"Number in floating format: {number['floating_f']:.2}\n")

    def fractional_format(self, numerator, denominator):
        self.divider = math.gcd(numerator, denominator)
        numerator //= self.divider
        denominator //= self.divider
        return numerator, denominator

    def floating_point_format(self, numerator, denominator):
        return numerator / denominator

    def count_lcm(self):
        return math.lcm(self.rationals[0]["denominator"], self.rationals[1]["denominator"])

    def count_numerators(self, lcm):
        numerator_1 = self.rationals[0]["numerator"] * (lcm // self.rationals[0]["denominator"])
        numerator_2 = self.rationals[1]["numerator"] * (lcm // self.rationals[1]["denominator"])
        return numerator_1, numerator_2

    def add_numbers(self):
        lcm = self.count_lcm()
        numerator_1, numerator_2 = self.count_numerators(lcm)
        numerator = numerator_1 + numerator_2
        denominator = lcm

        numerator_fr, denominator_fr = self.fractional_format(numerator, denominator)
        return f"Adding: {numerator_fr}/{denominator_fr}"

    def subtract_numbers(self):
        lcm = self.count_lcm()
        numerator_1, numerator_2 = self.count_numerators(lcm)
        numerator = numerator_1 - numerator_2
        denominator = lcm

        if numerator == 0:
            return "Subtracting: 0"
        else:
            numerator_fr, denominator_fr = self.fractional_format(numerator, denominator)
            return f"Subtracting: {numerator_fr}/{denominator_fr}"

    def multiply_numbers(self):
        numerator = self.rationals[0]["numerator"] * self.rationals[1]["numerator"]
        denominator = self.rationals[0]["denominator"] * self.rationals[1]["denominator"]

        if denominator == 0:
            print("Denominator cannot be 0")
            return
        elif numerator == 0:
            return "Multiplying: 0"
        else:
            numerator_fr, denominator_fr = self.fractional_format(numerator, denominator)
            return f"Multiplying: {numerator_fr}/{denominator_fr}"

    def divide_numbers(self):
        numerator = self.rationals[0]["numerator"] * self.rationals[1]["denominator"]
        denominator = self.rationals[0]["denominator"] * self.rationals[1]["numerator"]

        if denominator == 0:
            print("Denominator cannot be 0")
            return
        elif numerator == 0:
            return "Dividing: 0"
        else:
            numerator_fr, denominator_fr = self.fractional_format(numerator, denominator)
            return f"Dividing: {numerator_fr}/{denominator_fr}"

    def compare_numbers(self):
        lcm = self.count_lcm()
        numerator_1, numerator_2 = self.count_numerators(lcm)

        if numerator_1 > numerator_2:
            return f"{self.rationals[0]['fractional_f']} > {self.rationals[1]['fractional_f']}"
        elif numerator_1 < numerator_2:
            return f"{self.rationals[0]['fractional_f']} < {self.rationals[1]['fractional_f']}"
        elif numerator_1 == numerator_2:
            return f"{self.rationals[0]['fractional_f']} = {self.rationals[1]['fractional_f']}"
        else:
            return "Something wrong..."


rational = Rational(8, 10, 4, 16)
rational.count_formats()
print(rational.add_numbers())
print(rational.subtract_numbers())
print(rational.multiply_numbers())
print(rational.divide_numbers())
print(rational.compare_numbers())