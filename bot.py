import telebot
import job


class Bot(telebot.TeleBot):
    def __init__(self, token):
        super().__init__(token)
        self.job_parameters = None
        self.num_of_vacancies = 0
        self.last_position = 0
        self.list_of_vacancies = []

    def job_reset(self):
        self.job_parameters = job.Job()
        self.num_of_vacancies = 0
        self.last_position = 0
        self.list_of_vacancies = []

    is_find = False
