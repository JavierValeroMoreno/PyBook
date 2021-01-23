from colorama import Fore
from time import sleep
from Case import Case
import colorama
import platform
import os
    
class Book:

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
                            if op == "t":
                                text = text + line
                            if op == "o":
                                aux = line.split(':')
                                opt_c[aux[0]] = aux[1]
                                opt_o[aux[0]] = aux[2]

                    c[num_case] = Case(text, opt_c, opt_o, self.vel)
        self.casos = c
