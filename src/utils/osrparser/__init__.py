#!/usr/bin/env python3
import glob
from .replay import parse_replay_file
from os.path import getctime, join

def get_latest_replay(osu_root_path):
    replays_list = [f for f in glob.glob(join(osu_root_path, "Replays", "*.osr"))]
    if not replays_list:
        return None
    return max(replays_list, key=getctime)