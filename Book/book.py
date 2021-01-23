from colorama import Fore
from time import sleep
from Book.case import Case
import platform
import os


class Book(object):

    def __init__(self, casos: dict = {},  vel: int = 10):
        self.casos = casos
        self.vel = vel
        self.actual = 0

    def init(self):
        while (self.actual != -2):
            c: Case = self.casos[self.actual]
            c.dm_print()
            c.u_print()
            while True:
                self.actual = c.read_option()
                if self.actual != -1:
                    break

    def load_file(self, path: str):
        c = {}
        try:
            with open(path, 'r') as reader:
                line = "init"
                while line != '':
                    line = reader.readline()
                    if line.strip() == "@META":
                        line = reader.readline()
                        self.vel = int(line.split(':')[1])
                    if line.strip() == "@CASE":
                        line = reader.readline()

                        num_case = int(line.split(':')[1])
                        text = ""
                        op = "d"
                        opt_c = {}
                        opt_o = {}
                        while line.strip() != "@END_CASE":
                            line = reader.readline()
                            if line.strip() == "@END_CASE":
                                break

                            if line.strip() == "@TEXT":
                                op = "t"
                            elif line.strip() == "@OPT":
                                op = "o"
                            else:
                                if op == "t" and line.strip() != "":
                                    text = text + (line.strip()) + "\n"
                                if op == "o":
                                    aux = line.split(':')
                                    opt_c[aux[0].strip()] = aux[1].strip()
                                    opt_o[aux[0].strip()] = aux[2]

                        c[num_case] = Case(text, opt_c, opt_o, self.vel)
        except FileNotFoundError as fnfe:
            print(f'File "{path}" does not exist.')

        self.casos = c