import colorama
from colorama import Fore
from time import sleep
import platform


class Case:

    def __init__(self, text: str, options: dict = {}, option_select: dict = {}, vel: int = 10):
        self.text = text
        self.options = options
        self.option_select = option_select
        self.vel = vel
        self.user_c = Fore.WHITE
        self.dm_c = Fore.GREEN
        if(platform.system() == "Windows"):
            colorama.init()

    def u_print(self, end_="\n"):
        if(not bool(self.options)):
            return
        for k in self.options.keys():
            print("{}{}) {}".format(self.user_c, k, self.options[k]), end=end_)

    def dm_print(self, end_="\n"):
        for let in self.text:
            print("{}{}".format(self.dm_c, let), end="")
            sleep(self.vel * 0.001)
        print("", end=end_)

    def read_option(self) -> int:
        if bool(not self.option_select):
            return -2

        op = input("Select a option: ")
        try:
            return int(self.option_select[op])
        except KeyError:
            return -1
