import telebot
import job


class Bot(telebot.TeleBot):
    def __init__(self, token):
        super().__init__(token)
        # self.job_parameters = None
        self.num_of_vacancies = 0
        self.last_position = 0
        self.list_of_vacancies = []
        self.job_parameters = job.Job()

        self.__is_authorization = False
        self.__is_auth_login = False
        self.user_login = ""
        self.user_password = ""

        self.waiting_filter_value = ""

        self.access_token = ""

    def reset_filters(self):
        self.job_parameters = job.Job()
        self.num_of_vacancies = 0
        self.last_position = 0
        self.list_of_vacancies = []
        self.waiting_filter_value = ""

    def reset_auth_data(self):
        self.__is_authorization = False
        self.__is_auth_login = False
        self.user_login = ""
        self.user_password = ""

    is_find = False

    @property
    def is_authorization(self):
        return self.__is_authorization

    @is_authorization.setter
    def is_authorization(self, value):
        if value in [True, False]:
            self.__is_authorization = value
        else:
            self.__is_authorization = False

    @property
    def is_auth_login(self):
        return self.__is_auth_login

    @is_auth_login.setter
    def is_auth_login(self, value):
        if value in [True, False]:
            self.__is_auth_login = value
        else:
            self.__is_auth_login = False
