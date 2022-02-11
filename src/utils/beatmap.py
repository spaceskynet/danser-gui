#!/usr/bin/env python3
import sqlite3, munch
from utils.osrparser import parse_replay_file
from os.path import isfile, join, basename

osu_db_select_cols = "folder_name, map_file, artist, artist_unicode, title, title_unicode, mapper, difficulty, gameplay_mode, circle_size, approach_rate, hp_drain, overall_difficulty, total_time, beatmap_id, beatmap_set_id, md5_hash"
danser_db_select_cols = "dir, file, artist, artistUnicode, title, titleUnicode, creator, version, mode, cs, ar, hpdrain, od, endTime, mapID, setID, md5"

def db_query(db_path, query):
    db = sqlite3.connect(db_path)
    cur = db.cursor()
    cur.execute(query)
    result = cur.fetchall()
    cur.close()
    db.close()
    return result

def osu_db_query(osu_db_path):
    query = f"SELECT {osu_db_select_cols} FROM maps"
    return db_query(osu_db_path, query)

def danser_db_query(danser_db_path):
    query = f"SELECT {danser_db_select_cols} FROM beatmaps"
    return db_query(danser_db_path, query)

def osu_db_hash_query(osu_db_path, hash):
    query = f"SELECT {osu_db_select_cols} FROM maps WHERE md5_hash = '{hash}'"
    return db_query(osu_db_path, query)

def danser_db_hash_query(danser_db_path, hash):
    query = f"SELECT {danser_db_select_cols} FROM beatmaps WHERE md5 = '{hash}'"
    return db_query(danser_db_path, query)

def osu_db_mapfile_query(osu_db_path, mapfile):
    query = f'SELECT {osu_db_select_cols} FROM maps WHERE map_file = "{mapfile}"'
    return db_query(osu_db_path, query)

def danser_db_mapfile_query(danser_db_path, mapfile):
    query = f'SELECT {danser_db_select_cols} FROM beatmaps WHERE file = "{mapfile}"'
    return db_query(danser_db_path, query)

def get_beatmap_munch(result):
    data = munch.Munch()
    data.FolderName, data.MapFile, data.Artist, data.ArtistUnicode, data.MapTitle, data.MapTitleUnicode, data.Creator, data.Difficulty, data.GameMode, data.CS, data.AR, data.HP, data.OD, data.TotalTime, data.MapID, data.SetID, data.MD5 = result
    return data

def get_beatmap_info_by_hash(db_path, songs_db_mode, hash):
    if songs_db_mode == 'osu!':
        result = osu_db_hash_query(join(db_path, 'osu!.sqlite3.db'), hash)
    else:
        result = danser_db_hash_query(join(db_path, 'danser.db'), hash)
    if len(result) == 0:
        return None
    return get_beatmap_munch(result[0])

def get_beatmap_info_by_mapfile(db_path, songs_db_mode, mapfile):
    if songs_db_mode == 'osu!':
        result = osu_db_mapfile_query(join(db_path, 'osu!.sqlite3.db'), mapfile)
    else:
        result = danser_db_mapfile_query(join(db_path, 'danser.db'), mapfile)
    if len(result) == 0:
        return None
    return get_beatmap_munch(result[0])

def get_beatmaps(db_path, songs_db_mode):
    maps = []
    if songs_db_mode == 'osu!':
        result = osu_db_query(join(db_path, 'osu!.sqlite3.db'))
    else:
        result = danser_db_query(join(db_path, 'danser.db'))
    if len(result) == 0:
        return None
    for map in result:
        maps.append(get_beatmap_munch(map))
    return maps

def find_beatmap_by_mapfile(mapfile_path, db_path, songs_db_mode):
    mapfile = basename(mapfile_path)
    return get_beatmap_info_by_mapfile(db_path, songs_db_mode, mapfile)

def find_beatmap_by_replay(replay_path, db_path, songs_db_mode):
    replay_file = parse_replay_file(replay_path)
    return get_beatmap_info_by_hash(db_path, songs_db_mode, replay_file.beatmap_hash)

if __name__ == "__main__":
    pass