from tools_and_constants import IFilter


def filter_handler(bot, property_name, parameters):
    # обрабатываем и устанавливаем значение фильтру
    try:
        setattr(bot.job_parameters, property_name, " ".join(parameters))
        value = getattr(bot.job_parameters, property_name)

        if value is None:
            return False
        return True
    except ValueError:
        return False


class FilterConstants:
    class Count(IFilter):
        @property
        def get_name(self):
            return [0, "count", "Счётчик"]

        default_value = 3
        valid_values = [["Любое натуральное число"]]

    class Vacancy(IFilter):
        @property
        def get_name(self):
            return [1, "keyword", "Вакансия"]

        default_value = None
        valid_values = [["Любая строка"]]

    class Age(IFilter):
        @property
        def get_name(self):
            return [2, "age", "Возраст"]

        default_value = None
        min_age = 0
        max_age = 120
        valid_values = [["Целое число от {0} до {1}".format(min_age, max_age)]]

    class Town(IFilter):
        @property
        def get_name(self):
            return [4, "town", "Город"]

        default_value = "Moscow"
        valid_values = [["Любая строка"]]

    class Gender(IFilter):
        @property
        def get_name(self):
            return [3, "gender", "Пол"]

        default_value = None
        m = ("1", "m", "м", "man", "male", "муж", "мужчина", "мужской")
        f = ("2", "f", "ж", "female", "woman", "жен", "женщина", "женский")
        not_important = ("0", "-", "не важно", "not important")
        right_values = m + f + not_important
        values_of_field = {m: 1, f: 2, not_important: 3}
        valid_values = [m, f, not_important]

    class PlaceOfWork(IFilter):
        @property
        def get_name(self):
            return [5, "place_of_work", "Место работы"]

        default_value = None
        employers_territory = ("1", "на территории работодателя", "on the employer's territory")
        at_home = ("2", "на дому", "дома", "at home")
        traveling_character = ("3", "разъездного характера", "traveling character")
        right_values = employers_territory + at_home + traveling_character
        values_of_field = {employers_territory: 1, at_home: 2, traveling_character: 3}
        valid_values = [employers_territory, at_home, traveling_character]

    class TypeOfWork(IFilter):
        @property
        def get_name(self):
            return [6, "type_of_work", "Тип занятости"]

        default_value = None
        full_day = ("6", "full day", "полный день")
        incomplete_day = ("10", "incomplete day", "неполный день")
        shift_schedule = ("12", "shift schedule", "сменный график")
        part_time_employment = ("13", "part-time employment", "частичная занятость")
        temporary_work = ("7", "temporary work", "временная работа")
        shift_method = ("9", "shift method", "вахтовой метод")
        right_values = full_day + incomplete_day + shift_schedule + part_time_employment \
                                + temporary_work + shift_method
        values_of_field = {full_day: 6, incomplete_day: 10, shift_schedule: 12, part_time_employment: 13,
                           temporary_work: 7, shift_method: 9}
        valid_values = [full_day, incomplete_day, shift_schedule, part_time_employment, temporary_work, shift_method]

    class PaymentFrom(IFilter):
        @property
        def get_name(self):
            return [7, "payment_from", "Зарплата от"]

        default_value = None
        valid_values = [["Любые натуральные числа"]]

    class Experience(IFilter):
        @property
        def get_name(self):
            return [8, "experience", "Опыт"]

        default_value = None
        no_experience = ("1", "без опыта", "no experience")
        from_1_year = ("2", "от 1 года", "from 1 year")
        from_3_years = ("3", "от 3 лет", "from 3 years")
        from_6_years = ("4", "от 6 лет", "from 6 years")
        right_values = no_experience + from_1_year + from_3_years + from_6_years
        values_of_field = {no_experience: 1, from_1_year: 2, from_3_years: 3, from_6_years: 4}
        valid_values = [no_experience, from_1_year, from_3_years, from_6_years]

    class Education(IFilter):
        @property
        def get_name(self):
            return [9, "education", "Образование"]

        default_value = None
        higher = ("2", "высшее", "higher")
        incomplete_higher = ("3", "неполное высшее", "incomplete higher")
        medium_special = ("4", "среднее-специальное", "medium-special")
        average = ("5", "среднее", "average")
        student = ("6", "учащийся", "студент", "student")
        right_values = higher + incomplete_higher + medium_special + average + student
        values_of_field = {higher: 2, incomplete_higher: 3, medium_special: 4, average: 5, student: 6}
        valid_values = [higher, incomplete_higher, medium_special, average, student]

    count = Count()
    vacancy = Vacancy()
    age = Age()
    town = Town()
    gender = Gender()
    place_of_work = PlaceOfWork()
    type_of_work = TypeOfWork()
    payment_from = PaymentFrom()
    experience = Experience()
    education = Education()

    names = [vacancy, age, town, gender, place_of_work, type_of_work, payment_from, experience, education]

