import filters_handler


class Job(object):
    """Class with job parameters"""

    def __init__(self):
        self.__cnt_of_parameters = 9
        self.__list_number = [self.get_property_name([0, "payment"])[0]]

        self.__vacancy = filters_handler.FilterConstants.Vacancy
        self.__age = filters_handler.FilterConstants.Age
        self.__gender = filters_handler.FilterConstants.Gender
        self.__place_of_work = filters_handler.FilterConstants.PlaceOfWork
        self.__town = filters_handler.FilterConstants.Town
        self.__type_of_work = filters_handler.FilterConstants.TypeOfWork
        self.__payment = filters_handler.FilterConstants.Payment
        self.__experience = filters_handler.FilterConstants.Experience
        self.__education = filters_handler.FilterConstants.Education

        self.__cnt = filters_handler.FilterConstants.Count

    @property
    def list_number(self):
        return self.__list_number

    @property
    def cnt_of_parameters(self):
        return self.__cnt_of_parameters

    @staticmethod
    def get_property_name(num_or_name):
        for names in filters_handler.FilterConstants.names:
            for parameter in num_or_name:
                if parameter in names:
                    return names
        return [None, None, None]

    @staticmethod
    def __find_value(value, right_values, values_of_field):
        if value in right_values:
            for key in values_of_field:
                if value in key:
                    return values_of_field[key]
        else:
            return None

    @property
    def vacancy(self):
        return self.__vacancy

    @vacancy.setter
    def vacancy(self, value):
        print(value)
        self.__vacancy = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        print(value)
        try:
            value = int(value)
            if (value > filters_handler.FilterConstants.Age.min_age) \
                    and (value < filters_handler.FilterConstants.Age.max_age):
                self.__age = value
            else:
                self.__age = None
        except ValueError:
            self.__age = None

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value):
        print(value)
        self.__gender = self.__find_value(value.lower(),
                                          filters_handler.FilterConstants.Gender.right_values,
                                          filters_handler.FilterConstants.Gender.values_of_field)

    @property
    def town(self):
        return self.__town

    @town.setter
    def town(self, value):
        print("a")
        print(value)
        self.__town = value

    @property
    def place_of_work(self):
        return self.__place_of_work

    @place_of_work.setter
    def place_of_work(self, value):
        print(value)
        self.__place_of_work = self.__find_value(value.lower(),
                                                 filters_handler.FilterConstants.PlaceOfWork.right_values,
                                                 filters_handler.FilterConstants.PlaceOfWork.values_of_field)

    @property
    def type_of_work(self):
        return self.__type_of_work

    @type_of_work.setter
    def type_of_work(self, value):
        print(value)
        self.__type_of_work = self.__find_value(value.lower(),
                                                filters_handler.FilterConstants.TypeOfWork.right_values,
                                                filters_handler.FilterConstants.TypeOfWork.values_of_field)

    @property
    def payment(self):
        return self.__payment

    @payment.setter
    def payment(self, value):
        print(value)
        try:
            if len(value) == 2:
                if not value[0].isdigit():
                    value[1] = int(value[1])
                    self.__payment = [None, value[1]]
                elif not value[1].isdigit():
                    value[0] = int(value[0])
                    self.__payment = [value[0], None]
                else:
                    value[0] = int(value[0])
                    value[1] = int(value[1])
                    self.__payment = [value[0], value[1]]
            else:
                self.__payment = [None, None]
        except ValueError:
            self.__payment = [None, None]

    @property
    def experience(self):
        return self.__experience

    @experience.setter
    def experience(self, value):
        print(value)
        self.__experience = self.__find_value(value.lower(),
                                              filters_handler.FilterConstants.Experience.right_values,
                                              filters_handler.FilterConstants.Experience.values_of_field)

    @property
    def education(self):
        return self.__education

    @education.setter
    def education(self, value):
        print(value)
        self.__education = self.__find_value(value.lower(),
                                             filters_handler.FilterConstants.Education.right_values,
                                             filters_handler.FilterConstants.Education.values_of_field)
