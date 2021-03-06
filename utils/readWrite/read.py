import os
import sys
from configparser import ConfigParser
from utils.logging.syslog import Logger

class Configuration():
    def __init__(self):
        self.logging = Logger(__name__)
        Logger.get_log(self.logging).info('Start processing ConfigFile')
        self.config()
        Logger.get_log(self.logging).info('ConfigFile Processed\n')

    def config(self):
        cp = ConfigParser()
        cp.read('conf.cfg')
        self.folder = cp.get('configuration', 'folder')
        self.filename = cp.get('configuration', 'filename')
        self.text_level = cp.getint('configuration', 'text_level')
        self.save_text = cp.getboolean('configuration', 'save_text')
        self.save_image = cp.getboolean('configuration', 'save_image')

        self.configCheck()

        self.output_folder = 'output/'
        if not os.path.exists(self.output_folder):
            os.mkdir(self.output_folder)

        if self.save_text or self.save_image:
            self.prediction_folder = self.output_folder + 'prediction/'
            if not os.path.exists(self.prediction_folder):
                os.mkdir(self.prediction_folder)

        if self.save_text == True:
            self.json_folder = self.prediction_folder + 'json/'
            if not os.path.exists(self.json_folder):
                os.mkdir(self.json_folder)

        if self.save_image == True:
            self.img_folder = self.prediction_folder + 'image/'
            if not os.path.exists(self.img_folder):
                os.mkdir(self.img_folder)

        if self.filename == 'all':
            self.fileList = sorted(os.listdir(self.folder))
        else:
            self.fileList = [self.filename]

    def configCheck(self):
        if not self.folder[-1] == '/':
            Logger.get_log(self.logging).critical('Configuration - Folder Format Error')
            print("Configuration - Folder may loss '/' to the end of the path")
            y_n = input("Do you want system add '/' to the end of path ? (Y/N)\n")
            if y_n.lower() == 'y' or y_n.lower() == 'yes':
                self.folder += '/'
            else:
                sys.exit()

        if not self.filename == 'all' and not self.filename[-4:] == '.pdf':
            Logger.get_log(self.logging).critical('Configuration - FileName Not End With .pdf ')
            print('Configuration - FileName Not End With \'.pdf\'')
            y_n = input("Do you want system add '.pdf' to the end of filename ? (Y/N)\n")
            if y_n.lower() == 'y' or y_n.lower() == 'yes':
                self.filename += '.pdf'
            else:
                sys.exit()

        if not (self.text_level == 1 or self.text_level == 2):
            Logger.get_log(self.logging).critical('Configuration - text_level Format Error ')
            while True:
                print('Configuration - text_level Format Error ')
                text_level = input("Please press 1/2 to specify a text_level \n")
                if text_level == '1' or text_level == '2':
                    self.text_level = text_level
                    break