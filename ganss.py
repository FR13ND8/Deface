#!/bin/python

import time

import os

import sys

import random

from time import sleep as timeout


def rus(s):

	for c in s + '\n':

		sys.stdout.write(c)

		sys.stdout.flush()

		time.sleep(random.random() * 0.2)


def tes(s):

	for c in s + '\n':

		sys.stdout.write(c)

		sys.stdout.flush()

		time.sleep(random.random() * 0.2)

os.system("clear")

tes('''\033[41;1;39m[ Loading ] \033[0m..............................................................................................................................................................\033[42;1;39m [ Success ]\033[0m
''')

os.system("sh Riski.sh")