# сделать константами класс
token = '640881508:AAGBp-rt5DKK8ld75Z8K-4v-qfX2liBOSzQ'
x_api_app_id = 'v3.r.129793082.5c2adfa4e6e84aceba2233647afc5e349bc0d78a.f2fa1ffeb2de25adca0a6ef7ec975079b140ce65'
app_id = 1033


class CommandsNames:
    help = "help"
    find = "find"
    words_for_find = ["найти", "find", "search"]
    add_on_page = ["+", "еще", "ещё", "далее", "next", "further"]
    start = "start"
    show = "show"
    get_favorite = "get"
    add_favorite = "add"
    del_favorite = "del"
    login = "login"

    @staticmethod
    def with_slash(command_name):
        return "/{0}".format(command_name)


class UnusualMessage:
    on_audio = "Хорошая песня."
    on_video = "Интересное видео."
    on_photo = "Красивое фото."
    on_document = "Увы, не могу прочесть."
    on_location = "Спасибо, теперь я знаю, где что-то находится."
    on_sticker = "Увы, никогда не разбирался в стикерах."


class ErrorMessage:
    not_understand = "Прости, я тебя не понимаю.\nКоманда {0} поможет тебе вести диалог со мной.". \
        format(CommandsNames.help)
    incorrect_data = "Ошибка. Проверьте корректность введенных данных."
    no_such_filter = "Нет такого поля."
    authorization_error = "Не удалось авторизоваться, пожалуйста, проверьте введенные данные."
    end_of_vacancies_list = "Вы просмотрели все вакансии."
    not_logged_in = "Войдите в систему, чтобы выполнить операцию."
    no_vacancy_id = "Ошибка, введите id вакансии сразу после команды"
    unable_to_del_vacancy = "Не удалось удалить вакансию, проверьте введенные данные"
    unable_to_add_vacancy = "Не удалось добавить вакансию, проверьте введенные данные"


class Authorization:
    login = "Логин:"
    password = "Пароль:"


class ListTitle:
    filters = "Фильтры:"
    possible_values = "Возможные значения:"
    fixed_filters = "Установленные фильтры:"
    vacancies_found = "Найдено вакансий:"


class SuccessMessage:
    vacancy_added = "Вакансия успешно добавлена к избранным"
    vacancy_deleted = "Вакансия успешно удалена из избранных"
    auth_succeeded = "Авторизация прошла успешно.\n" \
                     + "Для сохранности данных рекомендуем удалить сообщение с вводом пароля."


class HelloWords:
    hello = "Приветствую, {0}.\n"\
             + "Этот бот создан, чтобы помогать людям находить интересующую их работу.\n" \
             + "Напиши \"{1}\", чтобы вызвать меню справки."


class PrintVacancy:
    vacancy_name = "Вакансия:"
    vacancy_id = "ID:"

    payment_from = "Зарплата: от {0}"
    payment_to = "Зарплата: до {0}"
    payment_from_to = "Зарплата: от {0} до {1}"

    type_of_work = "Тип занятости:"
    place_of_work = "Место работы:"
    education = "Образование:"
    experience = "Опыт:"
    gender = "Пол:"
    link = "Ссылка:"


class Links:
    superjob = "api.superjob.ru"
    superjob_favorites = "https://api.superjob.ru/2.0/favorites/"
    superjob_vacancies = "https://api.superjob.ru/2.0/vacancies/"
    superjob_password = "https://api.superjob.ru/2.0/oauth2/password/"


class IFilter:
    @property
    def get_name(self):
        raise NotImplementedError
