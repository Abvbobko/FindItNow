import filters_handler


class Job(object):
    """Class with job parameters"""

    def __init__(self):
        self.__cnt_of_parameters = len(filters_handler.FilterConstants.names)

        self.__keyword = filters_handler.FilterConstants.Vacancy.default_value
        self.__age = filters_handler.FilterConstants.Age.default_value
        self.__gender = filters_handler.FilterConstants.Gender.default_value
        self.__place_of_work = filters_handler.FilterConstants.PlaceOfWork.default_value
        self.__town = filters_handler.FilterConstants.Town.default_value
        self.__type_of_work = filters_handler.FilterConstants.TypeOfWork.default_value
        self.__payment_from = filters_handler.FilterConstants.PaymentFrom.default_value
        self.__experience = filters_handler.FilterConstants.Experience.default_value
        self.__education = filters_handler.FilterConstants.Education.default_value

        self.__cnt = filters_handler.FilterConstants.Count.default_value

    @property
    def cnt(self):
        return self.__cnt

    @cnt.setter
    def cnt(self, value):
        print(value)
        try:
            value = int(value)
            if value > 0:
                self.__cnt = value
            else:
                self.__cnt = filters_handler.FilterConstants.Count.default_value
        except ValueError:
            self.__cnt = filters_handler.FilterConstants.Count.default_value

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
                if parameter in names.get_name:
                    return names.get_name
        return [None, None, None]

    @staticmethod
    def find_value(value, right_values, values_of_field):
        if value in right_values:
            for key in values_of_field:
                if value in key:
                    return values_of_field[key]
        else:
            return None

    @property
    def keyword(self):
        return self.__keyword

    @keyword.setter
    def keyword(self, value):
        print(value)
        self.__keyword = value

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
        self.__gender = Job.find_value(value.lower(),
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
        self.__place_of_work = Job.find_value(value.lower(),
                                              filters_handler.FilterConstants.PlaceOfWork.right_values,
                                              filters_handler.FilterConstants.PlaceOfWork.values_of_field)

    @property
    def type_of_work(self):
        return self.__type_of_work

    @type_of_work.setter
    def type_of_work(self, value):
        print(value)
        self.__type_of_work = Job.find_value(value.lower(),
                                             filters_handler.FilterConstants.TypeOfWork.right_values,
                                             filters_handler.FilterConstants.TypeOfWork.values_of_field)

    @property
    def payment_from(self):
        return self.__payment_from

    @payment_from.setter
    def payment_from(self, value):
        print(value)
        try:
            self.__payment_from = int(value)
        except ValueError:
            self.__payment_from = None

    @property
    def experience(self):
        return self.__experience

    @experience.setter
    def experience(self, value):
        print(value)
        self.__experience = Job.find_value(value.lower(),
                                           filters_handler.FilterConstants.Experience.right_values,
                                           filters_handler.FilterConstants.Experience.values_of_field)

    @property
    def education(self):
        return self.__education

    @education.setter
    def education(self, value):
        print(value)
        self.__education = Job.find_value(value.lower(),
                                          filters_handler.FilterConstants.Education.right_values,
                                          filters_handler.FilterConstants.Education.values_of_field)
