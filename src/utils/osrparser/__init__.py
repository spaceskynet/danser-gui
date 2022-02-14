#!/usr/bin/env python3
import glob
from osrparse import Replay
from os.path import getctime, join

def parse_replay_file_from_path(replay_path):
	return Replay.from_path(replay_path)

def get_latest_replay(osu_root_path):
    replays_list = [f for f in glob.glob(join(osu_root_path, "Replays", "*.osr"))]
    if not replays_list:
        return None
    return max(replays_list, key=getctime)