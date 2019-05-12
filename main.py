# -*- coding: utf-8 -*-
import tools_and_constants
import telebot
import requests
import re
import json
import bot
import filters_handler

bot = bot.Bot(tools_and_constants.token)


@bot.message_handler(commands=[tools_and_constants.CommandsNames.start])
def send_start_message(message):
    start_message = "Приветствую, {0}.\n".format(message.chat.first_name) \
                    + "Этот бот создан, чтобы помогать людям находить интересующую их работу.\n" \
                    + "Напиши \"{0}\", чтобы вызвать меню справки.".\
                        format(tools_and_constants.CommandsNames.with_slash(tools_and_constants.CommandsNames.help))
    bot.send_message(message.chat.id, start_message)


@bot.message_handler(commands=[tools_and_constants.CommandsNames.help])
def send_help_message(message):
    pass


@bot.message_handler(commands=[tools_and_constants.CommandsNames.find])
def start_enter_searching_params(message):
    bot.is_find = True
    bot.job_reset()
    filters_menu = "Фильтры:"
    for filter_name in filters_handler.FilterConstants.names:
        filters_menu += "\n{0}. {1}".format(filter_name[0], filter_name[2])
    bot.send_message(message.chat.id, filters_menu)


@bot.message_handler(content_types=["text"])
def send_vacancies(message):
    if bot.is_find:
        user_arguments = message.text.split()
        if len(user_arguments) == 1:
            pass    # будет вызов метода в котором справка к этой цифре
        else:
            try:
                error = False
                for i in range(1, bot.job_parameters.cnt_of_parameters + 1):
                    if int(user_arguments[0]) == i:
                        if i in bot.job_parameters.list_number:
                            if len(user_arguments) >= 3:
                                error = filters_handler.filter_handler(bot,
                                                                       bot.job_parameters.
                                                                       get_property_name([i, "", ""])[1],
                                                                       True, [user_arguments[1], user_arguments[2]])
                            elif len(user_arguments) == 2:
                                error = filters_handler.filter_handler(bot,
                                                                       bot.job_parameters.
                                                                       get_property_name([i, "", ""])[1],
                                                                       True, [user_arguments[1], ""])
                        else:
                            error = filters_handler.filter_handler(bot,
                                                                   bot.job_parameters.
                                                                   get_property_name([i, "", ""])[1],
                                                                   False, user_arguments[1:])
                if not error:
                    bot.send_message(message.chat.id, tools_and_constants.ErrorMessage.incorrect_data)
            except ValueError:
                bot.send_message(message.chat.id, tools_and_constants.ErrorMessage.incorrect_data)
    else:
        bot.send_message(message.chat.id, tools_and_constants.ErrorMessage.not_understand)

    # header = {"X-Api-App-Id": config.x_api_app_id}
    #parameters = {"keyword": message.text}
    #response = requests.get("https://api.superjob.ru/2.0/vacancies/", headers=header, params=parameters)
    #todos = json.loads(response.text)

 #   """bot.send_message(message.chat.id, todos["objects"][0]["profession"])
  #  bot.send_message(message.chat.id, todos["objects"][1]["profession"])
  #  bot.send_message(message.chat.id, todos["objects"][3]["profession"])
  #  bot.send_message(message.chat.id, todos["objects"][4]["profession"])
  #  bot.send_message(message.chat.id, todos["objects"][5]["profession"])"""


if __name__ == '__main__':
    bot.polling(none_stop=True)
