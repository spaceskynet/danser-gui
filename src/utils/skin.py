#!/usr/bin/env python3
import glob
from os.path import join, isfile, basename

def get_skins(osu_skins_path):
    skins_list = [f for f in glob.glob(join(osu_skins_path, "*"))]
    valid_skins_list = ['default']
    for skin_path in skins_list:
        if isfile(join(skin_path, 'skin.ini')):
            valid_skins_list.append(basename(skin_path))
    return valid_skins_list