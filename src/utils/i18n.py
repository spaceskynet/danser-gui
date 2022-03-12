#!/usr/bin/env python3
import glob
import consts
from os.path import join, isfile, basename

class TranslationLoader(object):
    def __init__(self, is_setup=False):
        self.is_setup = is_setup
        self.exec_root_path = consts.exec_langs_path
        self.res_root_path = consts.res_langs_path
        self.langs_name_file = "lang.txt"
        self.langs_file = "lang.qm"
        self.getValidLanguages()

    def getValidLanguages(self):
        root_path = self.res_root_path if self.is_setup else self.exec_root_path
        langs_list = [f for f in glob.glob(join(root_path, "*"))]
        self.valid_langs_name_list, self.valid_langs_path_list = [], []
        for lang_path in langs_list:
            lang_name_file = join(lang_path, self.langs_name_file)
            lang_file = join(lang_path, self.langs_file)
            if not isfile(lang_name_file) or not isfile(lang_file): continue
            with open(lang_name_file, "r", encoding = "utf-8") as f:
                lang_name = f.readline()
            self.valid_langs_name_list.append(lang_name)
            self.valid_langs_path_list.append(basename(lang_path))
    
    def getDefaultLanguagePath(self):
        return join(self.res_root_path, 'en-US', self.langs_file)

    def getSelectedLanguagePath(self, section):
        root_path = self.res_root_path if self.is_setup else self.exec_root_path
        return join(root_path, self.getSelectedLanguageTag(section), self.langs_file)    

    def getSelectedLanguageTag(self, section):
        index = self.getSelectedLanguageIndex(section) if type(section) == str else section
        return self.valid_langs_path_list[index]

    def getSelectedLanguageIndex(self, section:str):
        try: index = self.valid_langs_path_list.index(section)
        except: index = 0
        return index
