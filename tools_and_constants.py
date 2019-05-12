# сделать константами класс
token = '640881508:AAGBp-rt5DKK8ld75Z8K-4v-qfX2liBOSzQ'
x_api_app_id = 'v3.r.129793082.5c2adfa4e6e84aceba2233647afc5e349bc0d78a.f2fa1ffeb2de25adca0a6ef7ec975079b140ce65'


class CommandsNames:
    help = "help"
    find = "find"
    start = "start"

    @staticmethod
    def with_slash(command_name):
        return "/{0}".format(command_name)


class ErrorMessage:
    not_understand = "Прости, я тебя не понимаю.\nКоманда {0} поможет тебе вести диалог со мной.".\
        format(CommandsNames.help)
    incorrect_data = "Ошибка. Проверьте корректность введенных данных."
