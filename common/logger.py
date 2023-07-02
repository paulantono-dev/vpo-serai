import os
from datetime import datetime
from pathlib import Path



class Logger :
    def __init__(self):
        self.__logger = ''
        Path(f'{os.getcwd()}/log').mkdir(parents=True, exist_ok=True)
        self.__logger = f'{os.getcwd()}/log/{datetime.now().strftime("%Y-%m-%d")}.txt'

    def __logStruct(self, severity, **kwargs):
        fileOpen = open(self.__logger, "a")
        dictParam = f"{severity} | {datetime.now().strftime('%Y-%m-%d')} | {datetime.now().strftime('%H:%M:%S')} | {kwargs}"
        fileOpen.write(f'{str(dictParam)}\n')
        fileOpen.close()


    def debug(self, **kwargs):
        self.__logStruct(severity='DEBUG', **kwargs)

    def info(self, **kwargs):
        self.__logStruct(severity='INFO', **kwargs)

    def warning(self, **kwargs):
        self.__logStruct(severity='WARNING', **kwargs)

    def error(self, **kwargs):
        self.__logStruct(severity='ERROR', **kwargs)

    def critical(self, **kwargs):
        self.__logStruct(severity='CRITICAL', **kwargs)