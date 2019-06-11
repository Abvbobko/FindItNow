# -*- coding: utf-8 -*-
import tools_and_constants
import requests
import json
import bot
import filters_handler

bot = bot.Bot(tools_and_constants.token)


@bot.message_handler(commands=[tools_and_constants.CommandsNames.start])
def send_start_message(message):
    # бот встречает нас
    start_message = tools_and_constants.HelloWords.hello.format(
                        message.chat.first_name,
                        tools_and_constants.CommandsNames.with_slash(tools_and_constants.CommandsNames.help))
    bot.send_message(message.chat.id, start_message)


@bot.message_handler(commands=["help11"])
def find_vacancies_filters_help(message):
    help_message = "Чтобы подбирать нужные вам вакансии в боте существуют специальные фильтры. " \
                   "Меню фильтров появляется после вызова команды /find. " \
                   "Чтобы узнать, какие значения может принимать данный фильтр, " \
                   "введите его номер из меню, после чего вы можете посмотреть возможные значения и ввести нужное. " \
                   "Также, если вы знаете доступные значения, " \
                   "вы можете ввести номер фильтра и его значение через пробел. " \
                   "Чтобы посмотреть установленные фильтры, введите команду /show. " \
                   "Для отмены введенного фильтра наберите номер фильтра и символ '-' через пробел."
    bot.send_message(message.chat.id, help_message)


@bot.message_handler(commands=["help1"])
def find_vacancies_help(message):
    help_message = "Чтобы искать вакансии, необходимо ввести команду /find, " \
                   "поставить интересующие фильтры и ввести одно из слов:\n" \
                   + ", ".join(tools_and_constants.CommandsNames.words_for_find) \
                   + "\nЧтобы вывести больше вакансий, введите одно из следующих значений:\n" \
                   + ", ".join(tools_and_constants.CommandsNames.add_on_page) \
                   + "\n/help11. Подробнее о фильтрах."
    bot.send_message(message.chat.id, help_message)


@bot.message_handler(commands=["help2"])
def authorization_help(message):
    help_message = "Для авторизации напишите команду /login, после чего введите логин и пароль."
    bot.send_message(message.chat.id, help_message)


@bot.message_handler(commands=["help31"])
def favorite_vacancies_add_help(message):
    help_message = "Чтобы добавить вакансию к избранным, напиши команду /add и укажи ID нужной вакансии через пробел."
    bot.send_message(message.chat.id, help_message)


@bot.message_handler(commands=["help32"])
def favorite_vacancies_del_help(message):
    help_message = "Чтобы удалить вакансию из избранных, напиши команду /del и укажи ID нужной вакансии через пробел."
    bot.send_message(message.chat.id, help_message)


@bot.message_handler(commands=["help33"])
def favorite_vacancies_get_help(message):
    help_message = "Чтобы вывести список избранных вакансий, напиши команду /get. " \
                   "Чтобы вывести еще вакансий из списка избранных, напиши одно из значений:\n" \
                   + ", ".join(tools_and_constants.CommandsNames.add_on_page)
    bot.send_message(message.chat.id, help_message)


@bot.message_handler(commands=["help3"])
def favorite_vacancies_help(message):
    help_message = "Бот умеет добавлять, удалять и показывать избранные вакансии с сайта superjob.ru. " \
                   "Для того, чтобы совершать эти действия, тебе подтребуется авторизоваться. " \
                   "Смотри подробнее:" \
                   + "\n/help31. Добавление избранных вакансий;" \
                   + "\n/help32. Удаление из избранных вакансий;" \
                   + "\n/help33. Вывод избранных вакансий."
    bot.send_message(message.chat.id, help_message)


@bot.message_handler(commands=["help4"])
def about_help(message):
    help_message = "Данный бот умеет отвечать на разные типы сообщений: " \
                   "стикеры, фото, видео, аудио, локацию, документы. " \
                   "Попробуй проверить в действии."
    bot.send_message(message.chat.id, help_message)


@bot.message_handler(commands=["help5"])
def favorite_vacancies_get_help(message):
    help_message = "FindItNow - бот для поиска работы на сайте superjob.ru\n" \
                   "Автор: Бобко Алексей.\n" \
                   "Для связи: abvbobko@mail.ru"
    bot.send_message(message.chat.id, help_message)


@bot.message_handler(commands=[tools_and_constants.CommandsNames.help])
def send_help_message(message):
    # тут будет помощь
    help_message = "Добро пожаловать в меню справки. Что тебя интересует?" \
                   + "\n/help1. Поиск вакансий;" \
                   + "\n/help2. Авторизация;" \
                   + "\n/help3. Избранные вакансии;" \
                   + "\n/help4. Дополнительные возможности;" \
                   + "\n/help5. Об авторе и программе."
    bot.send_message(message.chat.id, help_message)


@bot.message_handler(commands=[tools_and_constants.CommandsNames.find])
def start_enter_searching_params(message):
    # включаем режим ввода фильтров и самого поиска
    bot.is_find = True
    bot.reset_filters()
    # сбрасываем все существующие фильтры и генерируем список новых
    filters_menu = tools_and_constants.ListTitle.filters
    for filter_name in filters_handler.FilterConstants.names:
        filters_menu += "\n{0}. {1}".format(filter_name.get_name[0], filter_name.get_name[2])
    bot.send_message(message.chat.id, filters_menu)


def filter_help_response(user_arguments, message_id):
    # получаем все возможные значения для данного фильтра
    name_of_filter = [None, None, None]
    found = False
    for i in range(1, bot.job_parameters.cnt_of_parameters + 1):
        if int(user_arguments[0]) == i:
            # определяем имя нашего фильтра
            name_of_filter = bot.job_parameters.get_property_name([i, "", ""])
            found = True
            break
    if found:
        # выводим возможные значения фильтра
        for find_filter in filters_handler.FilterConstants.names:
            if name_of_filter == find_filter.get_name:
                possible_values = tools_and_constants.ListTitle.possible_values
                for i in range(len(find_filter.valid_values)):
                    possible_values += "\n{0}. ".format(i + 1)
                    for value in find_filter.valid_values[i]:
                        possible_values += " {0},".format(value)
                    possible_values = possible_values[:-1] + ";"
                possible_values = possible_values[:-1] + "."
                bot.send_message(message_id, possible_values)
    else:
        bot.send_message(message_id, tools_and_constants.ErrorMessage.no_such_filter)


def put_filter_response(user_arguments, message_id):
    # устанавливаем значения фильтра
    error = False
    for i in range(1, bot.job_parameters.cnt_of_parameters + 1):
        if int(user_arguments[0]) == i:
            error = filters_handler.filter_handler(bot,
                                                   bot.job_parameters.get_property_name([i, "", ""])[1],
                                                   user_arguments[1:])
    if not error:
        # выдало ошибку во время попытки установки фильтра
        bot.send_message(message_id, tools_and_constants.ErrorMessage.incorrect_data)
    else:
        bot.waiting_filter_value = ""


def decryption(value, i):
    # расшифровываем значение фильтра, так как в некоторых просто цифра
    for necessary_filter in filters_handler.FilterConstants.need_to_decryption:
        # ищу нужный параметр фильтра по значению и вывожу второй элемент ключа, ведь в нем значение
        if i in necessary_filter.get_name:
            for key in necessary_filter.values_of_field.keys():
                if value == necessary_filter.values_of_field[key]:
                    value = key[1]
    return value


@bot.message_handler(commands=[tools_and_constants.CommandsNames.show])
def show_filters(message):
    # показ установленных фильтров
    response = ""
    j = 1
    for i in range(1, bot.job_parameters.cnt_of_parameters + 1):
        value = getattr(bot.job_parameters, bot.job_parameters.get_property_name([i, "", ""])[1])
        value = decryption(value, i)
        if value is not None:
            response += "\n{0}. {1}:  {2};".format(j, bot.job_parameters.get_property_name([i, "", ""])[2], value)
            j += 1
    if response != "":
        response = tools_and_constants.ListTitle.fixed_filters + response[:-1] + "."
        bot.send_message(message.chat.id, response)


@bot.message_handler(commands=[tools_and_constants.CommandsNames.get_favorite])
def get_favorites(message):
    # получение списка избранных вакансий
    if bot.access_token != "":
        header = {"Host": tools_and_constants.Links.superjob,
                  "X-Api-App-Id": tools_and_constants.x_api_app_id,
                  "Content-Type": "application/x-www-form-urlencoded",
                  "Authorization": "Bearer " + bot.access_token}
        response = requests.get(tools_and_constants.Links.superjob_favorites, headers=header)
        bot.list_of_vacancies = json.loads(response.text)
        bot.num_of_vacancies = len(bot.list_of_vacancies["objects"])
        bot.last_position = 0
        bot.is_find = True
        num = tools_and_constants.ListTitle.vacancies_found + " {0}".format(bot.num_of_vacancies)
        try:
            bot.send_message(message.chat.id, num)
            for i in range(bot.last_position, bot.job_parameters.cnt):
                print_vacancies(message.chat.id, i)
        except Exception:
            bot.send_message(message.chat.id, tools_and_constants.ErrorMessage.end_of_vacancies_list)
    else:
        bot.send_message(message.chat.id, tools_and_constants.ErrorMessage.not_logged_in)


@bot.message_handler(commands=[tools_and_constants.CommandsNames.add_favorite],
                     content_types=["text"])
def add_to_favorites(message):
    # добавляем ваканию в список избранных
    if bot.access_token != "":
        if len(message.text.split()) > 1:
            vacancy_id = message.text.split()[1]
            header = {"Host": tools_and_constants.Links.superjob,
                      "X-Api-App-Id": tools_and_constants.x_api_app_id,
                      "Content-Type": "application/x-www-form-urlencoded",
                      "Authorization": "Bearer " + bot.access_token}
            response = requests.post(tools_and_constants.Links.superjob_favorites + "{0}/".format(vacancy_id),
                                     headers=header)
            if int(response.status_code / 100) == 2:
                bot.send_message(message.chat.id, tools_and_constants.SuccessMessage.vacancy_added)
            else:
                bot.send_message(message.chat.id, tools_and_constants.ErrorMessage.unable_to_add_vacancy)
        else:
            bot.send_message(message.chat.id, tools_and_constants.ErrorMessage.no_vacancy_id)
    else:
        bot.send_message(message.chat.id, tools_and_constants.ErrorMessage.not_logged_in)


@bot.message_handler(commands=[tools_and_constants.CommandsNames.del_favorite],
                     content_types=["text"])
def del_from_favorites(message):
    # удаляем вакансию из списка избранных
    if bot.access_token != "":
        if len(message.text.split()) > 1:
            vacancy_id = message.text.split()[1]
            header = {"Host": tools_and_constants.Links.superjob,
                      "X-Api-App-Id": tools_and_constants.x_api_app_id,
                      "Content-Type": "application/x-www-form-urlencoded",
                      "Authorization": "Bearer " + bot.access_token}
            response = requests.delete(tools_and_constants.Links.superjob_favorites + "{0}/".format(vacancy_id),
                                       headers=header)
            if int(response.status_code / 100) == 2:
                bot.send_message(message.chat.id, tools_and_constants.SuccessMessage.vacancy_deleted)
            else:
                bot.send_message(message.chat.id, tools_and_constants.ErrorMessage.unable_to_del_vacancy)
        else:
            bot.send_message(message.chat.id, tools_and_constants.ErrorMessage.no_vacancy_id)
    else:
        bot.send_message(message.chat.id, tools_and_constants.ErrorMessage.not_logged_in)


def print_vacancies(message_id, i):
    # выводим полученные вакансии
    bot.last_position += 1
    vacancy = tools_and_constants.PrintVacancy.vacancy_name + " {0};\n". \
        format(bot.list_of_vacancies["objects"][i]["profession"])
    vacancy += tools_and_constants.PrintVacancy.vacancy_id + " {0};\n". \
        format(bot.list_of_vacancies["objects"][i]["id"])
    payment_from = bot.list_of_vacancies["objects"][i]["payment_from"]
    payment_to = bot.list_of_vacancies["objects"][i]["payment_to"]
    if payment_from != 0 and payment_to != 0:
        vacancy += tools_and_constants.PrintVacancy.payment_from_to.format(payment_from, payment_to) + ";\n"
    elif payment_from != 0 and payment_to == 0:
        vacancy += tools_and_constants.PrintVacancy.payment_from.format(payment_from) + ";\n"
    elif payment_from == 0 and payment_to != 0:
        vacancy += tools_and_constants.PrintVacancy.payment_to.format(payment_to) + ";\n"
    vacancy += tools_and_constants.PrintVacancy.type_of_work + " {0};\n".format(
        bot.list_of_vacancies["objects"][i]["type_of_work"]["title"])

    vacancy += tools_and_constants.PrintVacancy.place_of_work + " {0};\n".format(
        bot.list_of_vacancies["objects"][i]["place_of_work"]["title"])

    vacancy += tools_and_constants.PrintVacancy.education + " {0};\n".format(
        bot.list_of_vacancies["objects"][i]["education"]["title"])

    vacancy += tools_and_constants.PrintVacancy.experience + " {0};\n".format(
        bot.list_of_vacancies["objects"][i]["experience"]["title"])

    vacancy += tools_and_constants.PrintVacancy.gender + " {0};\n".format(
        bot.list_of_vacancies["objects"][i]["gender"]["title"])

    vacancy += tools_and_constants.PrintVacancy.link + " {0};\n".format(
        bot.list_of_vacancies["objects"][i]["link"])
    bot.send_message(message_id, vacancy)


def get_vacancies(message_id):
    # получаем вакансии с сайта
    header = {"X-Api-App-Id": tools_and_constants.x_api_app_id}
    parameters = {}
    for i in range(1, len(filters_handler.FilterConstants.names) + 1):
        name = bot.job_parameters.get_property_name([i, "", ""])[1]
        value = getattr(bot.job_parameters, name)
        if value is not None:
            parameters[name] = value
    response = requests.get(tools_and_constants.Links.superjob_vacancies, headers=header, params=parameters)
    bot.list_of_vacancies = json.loads(response.text)
    bot.num_of_vacancies = len(bot.list_of_vacancies["objects"])
    num = tools_and_constants.ListTitle.vacancies_found + " {0}".format(bot.num_of_vacancies)
    try:
        bot.send_message(message_id, num)
        for i in range(bot.last_position, bot.job_parameters.cnt):
            print_vacancies(message_id, i)
    except Exception:
        bot.send_message(message_id, tools_and_constants.ErrorMessage.end_of_vacancies_list)


def add_vacancies(message_id):
    # выводим еще вакансии
    try:
        for i in range(bot.last_position, bot.last_position + bot.job_parameters.cnt):
            print_vacancies(message_id, i)
    except Exception:
        bot.send_message(message_id, tools_and_constants.ErrorMessage.end_of_vacancies_list)


def authorization(message_id):
    # авторизуемся на сайте
    parameters = {"login": bot.user_login, "password": bot.user_password, "client_id": tools_and_constants.app_id,
                  "client_secret": tools_and_constants.x_api_app_id}
    response = requests.get(tools_and_constants.Links.superjob_password, params=parameters)
    if int(response.status_code / 100) == 4:
        bot.send_message(message_id, tools_and_constants.ErrorMessage.authorization_error)
    elif int(response.status_code / 100) == 2:
        response = json.loads(response.text)
        bot.access_token = response["access_token"]
        bot.send_message(message_id, tools_and_constants.SuccessMessage.auth_succeeded)
    bot.reset_auth_data()


@bot.message_handler(commands=[tools_and_constants.CommandsNames.login])
def log_in(message):
    # начинаем вход, ждем ввода логина
    bot.is_authorization = True
    bot.is_auth_login = True
    bot.send_message(message.chat.id, tools_and_constants.Authorization.login)


@bot.message_handler(content_types=["text"])
def text_handler(message):
    # обрабатываем текстовые сообщения
    if bot.is_find and not bot.is_authorization:
        # режим для ввода фильтров для поиска
        user_arguments = message.text.split()
        try:
            if len(user_arguments) == 1 and bot.waiting_filter_value == "":
                if message.text.lower() in tools_and_constants.CommandsNames.words_for_find:
                    # посылаем запрос на спецуху
                    bot.last_position = 0
                    get_vacancies(message.chat.id)
                elif message.text.lower() in tools_and_constants.CommandsNames.add_on_page:
                    add_vacancies(message.chat.id)
                else:
                    # вызываем справку для этого фильтра
                    filter_help_response(user_arguments, message.chat.id)
                    bot.waiting_filter_value = user_arguments[0]
            else:
                # устанавливаем значения для этого фильтра
                if bot.waiting_filter_value != "":
                    user_arguments = [bot.waiting_filter_value] + user_arguments

                put_filter_response(user_arguments, message.chat.id)
        except ValueError:
            # где то произошла ошибка ввода значения
            bot.send_message(message.chat.id, tools_and_constants.ErrorMessage.incorrect_data)
    elif bot.is_authorization:
        if bot.is_auth_login:
            bot.user_login = message.text
            bot.send_message(message.chat.id, tools_and_constants.Authorization.password)
            bot.is_auth_login = False
        else:
            bot.user_password = message.text
            authorization(message.chat.id)
    else:
        # пользователь просто пишет случайный текст
        bot.send_message(message.chat.id, tools_and_constants.ErrorMessage.not_understand)


@bot.message_handler(content_types=["audio"])
def send_on_audio(message):
    # реакция на отправку пользователем аудио
    bot.send_message(message.chat.id, tools_and_constants.UnusualMessage.on_audio)


@bot.message_handler(content_types=["document"])
def send_on_document(message):
    # реакция на отправку пользователем документа
    bot.send_message(message.chat.id, tools_and_constants.UnusualMessage.on_document)


@bot.message_handler(content_types=["photo"])
def send_on_photo(message):
    # реакция на отправку пользователем фото
    bot.send_message(message.chat.id, tools_and_constants.UnusualMessage.on_photo)


@bot.message_handler(content_types=["sticker"])
def send_on_sticker(message):
    # реакция на отправку пользователем стикера
    bot.send_message(message.chat.id, tools_and_constants.UnusualMessage.on_sticker)


@bot.message_handler(content_types=["video"])
def send_on_video(message):
    # реакция на отправку пользователем видео
    bot.send_message(message.chat.id, tools_and_constants.UnusualMessage.on_video)


@bot.message_handler(content_types=["location"])
def send_on_location(message):
    # реакция на отправку пользователем местоположения
    bot.send_message(message.chat.id, tools_and_constants.UnusualMessage.on_location)


if __name__ == '__main__':
    bot.polling(none_stop=True)
