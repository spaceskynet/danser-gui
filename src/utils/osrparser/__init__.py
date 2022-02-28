#!/usr/bin/env python3
import glob
import logging
from osrparse import Replay
from os.path import getctime, join

def parse_replay_file(replay_path):
	return Replay.from_path(replay_path)

def get_latest_replay(osu_root_path):
    replays_list = [f for f in glob.glob(join(osu_root_path, "Replays", "*.osr"))]
    if not replays_list:
        return None
    return max(replays_list, key=getctime)

def modify_replay_beatmap_hash(danser_root_path, beatmap_hash):
    replays_list = [f for f in glob.glob(join(danser_root_path, "replays", "*.osr"))]
    for replay_file in replays_list:
        replay = Replay.from_path(replay_file)
        logging.info(f"[GUI] {replay_file} is modified! Beatmap Hash Before: {replay.beatmap_hash}, Now: {beatmap_hash}")
        replay.beatmap_hash = beatmap_hash
        replay.write_path(replay_file)

def add_date_after_user_name(danser_root_path, date_format_index):
    date_format = ["%Y-%m-%d", "%m-%d-%Y", "%d-%m-%Y",]
    replays_list = [f for f in glob.glob(join(danser_root_path, "replays", "*.osr"))]
    for replay_file in replays_list:
        replay = Replay.from_path(replay_file)
        date = replay.timestamp.astimezone(tz=None).strftime(date_format[date_format_index])
        is_modified = len(replay.username) > 11 and replay.username[-11:] == f' {date}'
        if is_modified: continue
        logging.info(f"[GUI] {replay_file} is modified! User Name: {replay.username}, Date: {date}")
        replay.username = f"{replay.username} {date}"
        replay.write_path(replay_file)