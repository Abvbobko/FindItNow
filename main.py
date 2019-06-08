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
    start_message = "Приветствую, {0}.\n".format(message.chat.first_name) \
                    + "Этот бот создан, чтобы помогать людям находить интересующую их работу.\n" \
                    + "Напиши \"{0}\", чтобы вызвать меню справки.".\
                        format(tools_and_constants.CommandsNames.with_slash(tools_and_constants.CommandsNames.help))
    bot.send_message(message.chat.id, start_message)


@bot.message_handler(commands=[tools_and_constants.CommandsNames.help])
def send_help_message(message):
    # тут будет помощь
    pass


@bot.message_handler(commands=[tools_and_constants.CommandsNames.find])
def start_enter_searching_params(message):
    # включаем режим ввода фильтров и самого поиска
    bot.is_find = True
    bot.job_reset()
    # сбрасываем все существующие фильтры и генерируем список новых
    filters_menu = "Фильтры:"
    for filter_name in filters_handler.FilterConstants.names:
        filters_menu += "\n{0}. {1}".format(filter_name.get_name[0], filter_name.get_name[2])
    bot.send_message(message.chat.id, filters_menu)


def filter_help_response(user_arguments, message_id):
    name_of_filter = [None, None, None]
    found = False
    for i in range(1, bot.job_parameters.cnt_of_parameters + 1):
        print(i)
        if int(user_arguments[0]) == i:
            name_of_filter = bot.job_parameters.get_property_name([i, "", ""])
            found = True
            break
    if found:
        for find_filter in filters_handler.FilterConstants.names:
            if name_of_filter == find_filter.get_name:
                possible_values = "Возможные значения:"
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
    error = False
    for i in range(1, bot.job_parameters.cnt_of_parameters + 1):

        if int(user_arguments[0]) == i:
            error = filters_handler.filter_handler(bot,
                                                   bot.job_parameters.get_property_name([i, "", ""])[1],
                                                   user_arguments[1:])
    if not error:
        # выдало ошибку во время попытки установки фильтра
        bot.send_message(message_id, tools_and_constants.ErrorMessage.incorrect_data)


def print_vacancies(message_id, i):
    bot.last_position += 1
    vacancy = "Вакансия: {0};\n".format(bot.list_of_vacancies["objects"][i]["profession"])
    payment_from = bot.list_of_vacancies["objects"][i]["payment_from"]
    payment_to = bot.list_of_vacancies["objects"][i]["payment_to"]
    if payment_from != 0 and payment_to != 0:
        vacancy += "Зарплата: от {0} до {1};\n".format(payment_from, payment_to)
    elif payment_from != 0 and payment_to == 0:
        vacancy += "Зарплата: от {0};\n".format(payment_from)
    elif payment_from == 0 and payment_to != 0:
        vacancy += "Зарплата: до {0};\n".format(payment_to)
    vacancy += "Тип занятости: {0};\n".format(bot.list_of_vacancies["objects"][i]["type_of_work"]["title"])
    vacancy += "Место работы: {0};\n".format(bot.list_of_vacancies["objects"][i]["place_of_work"]["title"])
    vacancy += "Образование: {0};\n".format(bot.list_of_vacancies["objects"][i]["education"]["title"])
    vacancy += "Опыт: {0};\n".format(bot.list_of_vacancies["objects"][i]["experience"]["title"])
    vacancy += "Пол: {0};\n".format(bot.list_of_vacancies["objects"][i]["gender"]["title"])
    vacancy += "Ссылка: {0};\n".format(bot.list_of_vacancies["objects"][i]["link"])
    bot.send_message(message_id, vacancy)


def get_vacancies(message_id):
    header = {"X-Api-App-Id": tools_and_constants.x_api_app_id}
    parameters = {}
    for i in range(1, len(filters_handler.FilterConstants.names) + 1):
        name = bot.job_parameters.get_property_name([i, "", ""])[1]
        value = getattr(bot.job_parameters, name)
        print("name: ", name, " value: ", value)
        if value is not None:
            parameters[name] = value
        # parameters = {"keyword": message.text}
    print(parameters)
    response = requests.get("https://api.superjob.ru/2.0/vacancies/", headers=header, params=parameters)
    print(response.text)
    bot.list_of_vacancies = json.loads(response.text)
    bot.num_of_vacancies = len(bot.list_of_vacancies["objects"])
    num = "Найдено вакансий: {0}".format(bot.num_of_vacancies)
    try:
        bot.send_message(message_id, num)
        if bot.last_position >= bot.num_of_vacancies:
            pass
        for i in range(bot.last_position, bot.job_parameters.cnt):
            print_vacancies(message_id, i)
    except Exception:
        bot.send_message(message_id, "Вы просмотрели все вакансии.")


def add_vacancies(message_id):
    try:
        if bot.last_position >= bot.num_of_vacancies:
            pass
        for i in range(bot.last_position, bot.last_position + bot.job_parameters.cnt):
            print_vacancies(message_id, i)
    except Exception:
        bot.send_message(message_id, "Вы просмотрели все вакансии.")


@bot.message_handler(content_types=["text"])
def send_vacancies(message):
    if bot.is_find:
        # режим для ввода фильтров для поиска
        user_arguments = message.text.split()
        try:
            if len(user_arguments) == 1:
                if message.text.lower() in tools_and_constants.CommandsNames.words_for_find:
                    # посылаем запрос на спецуху
                    bot.last_position = 0
                    get_vacancies(message.chat.id)
                elif message.text.lower() in ["+", "еще", "ещё", "далее", "next", "further"]:
                    add_vacancies(message.chat.id)
                else:
                    # вызываем справку для этого фильтра
                    filter_help_response(user_arguments, message.chat.id)
            else:
                # устанавливаем значения для этого фильтра
                put_filter_response(user_arguments, message.chat.id)
        except ValueError:
            # где то произошла ошибка ввода значения
            bot.send_message(message.chat.id, tools_and_constants.ErrorMessage.incorrect_data)
    else:
        # пользователь просто пишет случайный текст
        bot.send_message(message.chat.id, tools_and_constants.ErrorMessage.not_understand)


@bot.message_handler(content_types=["audio"])
def send_on_audio(message):
    bot.send_message(message.chat.id, tools_and_constants.UnusualMessage.on_audio)


@bot.message_handler(content_types=["document"])
def send_on_document(message):
    bot.send_message(message.chat.id, tools_and_constants.UnusualMessage.on_document)


@bot.message_handler(content_types=["photo"])
def send_on_photo(message):
    bot.send_message(message.chat.id, tools_and_constants.UnusualMessage.on_photo)


@bot.message_handler(content_types=["sticker"])
def send_on_sticker(message):
    bot.send_message(message.chat.id, tools_and_constants.UnusualMessage.on_sticker)


@bot.message_handler(content_types=["video"])
def send_on_video(message):
    bot.send_message(message.chat.id, tools_and_constants.UnusualMessage.on_video)


@bot.message_handler(content_types=["location"])
def send_on_location(message):
    bot.send_message(message.chat.id, tools_and_constants.UnusualMessage.on_location)


if __name__ == '__main__':
    bot.polling(none_stop=True)
