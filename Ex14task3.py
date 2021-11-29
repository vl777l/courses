DIGITS = "0123456789"
ALP = "qwertyuiopasdfghjklzxcvbnm"
SYMBOLS = "!@#$%^&*-_=+/.,><|"


class Worker:
    __NAME, __SECOND_NAME = "Unknown", "Unknown"
    __YEAR = 1900
    __DEPARTMENT = ""
    __slots__ = ["__name", "__sc_name", "__department", "__year"]

    def __init__(self):
        self.__name = Worker.__NAME
        self.__sc_name = Worker.__SECOND_NAME
        self.__department = Worker.__DEPARTMENT
        self.__year = Worker.__YEAR

    @property
    def name(self):
        return self.__name.strip()

    @name.setter
    def name(self, name_of_worker):
        try:
            user_input_check_loop_digit(name_of_worker, DIGITS and SYMBOLS)
            self.__name = name_of_worker
        except Exception:
            print("You use numbers or symbols.\nRewrite you name.")

    @property
    def scname(self):
        return self.__sc_name.strip()

    @scname.setter
    def scname(self, second_name_of_worker):
        try:
            user_input_check_loop_digit(second_name_of_worker, DIGITS and SYMBOLS)
            self.__sc_name = second_name_of_worker
        except Exception:
            print("You use numbers or symbols.\nRewrite you second name.")

    @property
    def department(self):
        return self.__department.strip()

    @department.setter
    def department(self, worker_department):
        self.__department = worker_department

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year_of_starts_work):
        if isinstance(year_of_starts_work, int):
            self.__year = year_of_starts_work
        else:
            raise UserInputError()

    @staticmethod
    def work_after(li, ye):
        lis = []
        for _ in li:
            if _.year > ye:
                lis.append(_)
        for _ in lis:
            print(_)

    def __str__(self):
        return f"{self.__name} {self.__sc_name}, from the {self.__department} department, starts work in {self.__year}"


class UserInputError(Exception):
    pass


def has_string_symbols(string, symbols):
    for symbol in symbols:
        if symbol in string:
            return False
    return True


def user_input_check_loop_digit(cha, li):
    while True:
        if has_string_symbols(cha, li):
            return cha
        else:
            raise UserInputError('You used not allowed symbols!')


max = Worker()
max.name = 'Max'
max.scname = "Black"
max.department = "Ssc"
max.year = 2000
dim = Worker()
dim.name = "Dima"
dim.scname = "Legend"
dim.department = "OOP'Nice'"
dim.year = 2017
worker = [max, dim]
Worker.work_after(worker, 2000)