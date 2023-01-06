# Create a class CALENDAR.
# Define methods for creating and working with a CALENDAR instances and overload operations
# "+=, -=" - for adding and subtracting days, months, years to a given date
# "==, ! =, >, >=, <, <=" - for comparing dates.

from calendar import monthrange
import datetime


class Calendar:
    def __init__(self, day, month, year):
        self.day = int(day)
        self.month = int(month)
        self.year = int(year)

    def __getattr__(self, atr_name):
        return 'Something wrong...'

    def get_full_date(self):
        return f"{self.day:02d}/{self.month:02d}/{self.year}"

    def add_date(self, days, months, years):
        day = self.day + days
        month = self.month + months
        year = self.year + years

        days_in_month = monthrange(self.year, self.month)[1]

        if day > days_in_month:
            day %= days_in_month
            month += 1

        if month > 12:
            month %= 12
            year += 1

        return f"{day:02d}/{month:02d}/{year}"

    def subtract_date(self, days, months, years):
        day = self.day - days
        month = self.month - months
        year = self.year - years

        if day <= 0:
            days_in_month = monthrange(self.year, self.month - 1)[1]
            day += days_in_month
            month -= 1

        if month <= 0:
            month += 12
            year -= 1

        return f"{day:02d}/{month:02d}/{year}"

    def compare_dates(self, day, month, year):
        if self.year > year:
            return "The starting date is greater"
        elif self.year < year:
            return "The entered date is greater"
        else:
            if self.month > month:
                return "The starting date is greater"
            elif self.month < month:
                return "The entered date is greater"
            else:
                if self.day > day:
                    return "The starting date is greater"
                elif self.day < day:
                    return "The entered date is greater"


def check_values():
    is_valid_date = False
    day = 0
    month = 0
    year = 0

    while not is_valid_date:
        date = input("Enter the date in format 'dd/mm/yy': ")
        day, month, year = date.split('/')

        try:
            datetime.datetime(int(year), int(month), int(day))
            is_valid_date = True
        except ValueError:
            is_valid_date = False
    return day, month, year

def main():
    day, month, year = check_values()
    calendar = Calendar(day, month, year)

    option = input("Choose what you want to do with the date:\n"
                   "\t1 - add\n"
                   "\t2 - subtract\n"
                   "\t3 - compare\n"
                   "\tothers - exit\n")

    if option == '1':
        days = input("Enter how many days you want to add: ")
        months = input("Enter how many months you want to add: ")
        years = input("Enter how many years you want to add: ")

        print("Your result: ")
        print(calendar.add_date(int(days), int(months), int(years)))
        return
    elif option == '2':
        days = input("Enter how many days you want to subtract: ")
        months = input("Enter how many months you want to subtract: ")
        years = input("Enter how many years you want to subtract: ")

        print("Your result: ")
        print(calendar.subtract_date(int(days), int(months), int(years)))
        return
    elif option == '3':
        day, month, year = check_values()
        print(calendar.compare_dates(int(day), int(month), int(year)))
        return
    else:
        print("Bye")
        return


if __name__ == "__main__":
    main()