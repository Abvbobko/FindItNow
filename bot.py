import telebot
import job


class Bot(telebot.TeleBot):
    def __init__(self, token):
        super().__init__(token)
        self.job_parameters = None

    def job_reset(self):
        self.job_parameters = job.Job()

    is_find = False
