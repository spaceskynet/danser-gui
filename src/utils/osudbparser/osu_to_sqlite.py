#!/usr/bin/env python3
# from https://github.com/jaasonw/osu-db-tools
import sqlite3
import sys
import os
from utils.osudbparser import buffer
import logging
from autologging import traced, logged

# osu db can be really big and we probably shouldnt store it in ram
# but we still want to be able to query it quickly
# solution: parse the db into an sqlite db
@logged(logging.getLogger(__name__))
@traced
def create_db(osu_db_path, osu_sqlite3_db_path):
    if os.path.isfile(osu_sqlite3_db_path):
        try:
            os.remove(osu_sqlite3_db_path)
        except Exception as e:
            logging.info(f"[GUI][SongsDBUpdateThread][osu!] Can't remove old osu! db! Because of {traceback.format_exc()}")
    
    sql = sqlite3.connect(osu_sqlite3_db_path)
    c = sql.cursor()
    c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='maps' ''')
    if c.fetchone()[0] == 1:
        sql.execute("DROP TABLE maps")
    sql.execute("""
        CREATE TABLE maps (
            artist TEXT,
            artist_unicode TEXT,
            title TEXT,
            title_unicode TEXT,
            mapper TEXT,
            difficulty TEXT,
            audio_file TEXT,
            md5_hash TEXT,
            map_file TEXT,
            ranked_status INTEGER,
            num_hitcircles INTEGER,
            num_sliders INTEGER,
            num_spinners INTEGER,
            last_modified INTEGER,
            approach_rate NUMERIC,
            circle_size NUMERIC,
            hp_drain NUMERIC,
            overall_difficulty NUMERIC,
            slider_velocity NUMERIC,
            drain_time INTEGER,
            total_time INTEGER,
            preview_time INTEGER,
            beatmap_id INTEGER,
            beatmap_set_id INTEGER,
            thread_id INTEGER,
            grade_stadard INTEGER,
            grade_taiko INTEGER,
            grade_ctb INTEGER,
            grade_mania INTEGER,
            local_offset INTEGER,
            stack_leniency NUMERIC,
            gameplay_mode INTEGER,
            song_source TEXT,
            song_tags TEXT,
            online_offset INTEGER,
            font TEXT,
            is_unplayed INTEGER,
            last_played INTEGER,
            is_osz2 INTEGER,
            folder_name TEXT,
            last_checked INTEGER,
            ignore_sounds INTEGER,
            ignore_skin INTEGER,
            disable_storyboard INTEGER,
            disable_video INTEGER,
            visual_override INTEGER,
            last_modified2 INTEGER,
            mania_speed INTEGER
        );
    """)
    with open(osu_db_path, "rb") as db:
        version = buffer.read_uint(db)
        folder_count = buffer.read_uint(db)
        account_unlocked = buffer.read_bool(db)
        # skip this datetime shit for now (8 bytes)
        buffer.read_uint(db)
        buffer.read_uint(db)
        name = buffer.read_string(db)
        num_beatmaps = buffer.read_uint(db)

        for _ in range(num_beatmaps):
            artist = buffer.read_string(db)
            artist_unicode = buffer.read_string(db)
            song_title = buffer.read_string(db)
            song_title_unicode = buffer.read_string(db)
            mapper = buffer.read_string(db)
            difficulty = buffer.read_string(db)
            audio_file = buffer.read_string(db)
            md5_hash = buffer.read_string(db)
            map_file = buffer.read_string(db)
            ranked_status = buffer.read_ubyte(db)
            num_hitcircles = buffer.read_ushort(db)
            num_sliders = buffer.read_ushort(db)
            num_spinners = buffer.read_ushort(db)
            last_modified = buffer.read_ulong(db)
            approach_rate = buffer.read_float(db)
            circle_size = buffer.read_float(db)
            hp_drain = buffer.read_float(db)
            overall_difficulty = buffer.read_float(db)
            slider_velocity = buffer.read_double(db)
            # skip these int double pairs, personally i dont think they're 
            # important for the purpose of this database
            i = buffer.read_uint(db)
            for _ in range(i):
                buffer.read_int_double(db)

            i = buffer.read_uint(db)
            for _ in range(i):
                buffer.read_int_double(db)

            i = buffer.read_uint(db)
            for _ in range(i):
                buffer.read_int_double(db)

            i = buffer.read_uint(db)
            for _ in range(i):
                buffer.read_int_double(db)

            drain_time = buffer.read_uint(db)
            total_time = buffer.read_uint(db)
            preview_time = buffer.read_uint(db)
            # skip timing points
            # i = buffer.read_uint(db)
            for _ in range(buffer.read_uint(db)):
                buffer.read_timing_point(db)
            beatmap_id = buffer.read_uint(db)
            beatmap_set_id = buffer.read_uint(db)
            thread_id = buffer.read_uint(db)
            grade_standard = buffer.read_ubyte(db)
            grade_taiko = buffer.read_ubyte(db)
            grade_ctb = buffer.read_ubyte(db)
            grade_mania = buffer.read_ubyte(db)
            local_offset = buffer.read_ushort(db)
            stack_leniency = buffer.read_float(db)
            gameplay_mode = buffer.read_ubyte(db)
            song_source = buffer.read_string(db)
            song_tags = buffer.read_string(db)
            online_offset = buffer.read_ushort(db)
            title_font = buffer.read_string(db)
            is_unplayed = buffer.read_bool(db)
            last_played = buffer.read_ulong(db)
            is_osz2 = buffer.read_bool(db)
            folder_name = buffer.read_string(db)
            last_checked = buffer.read_ulong(db)
            ignore_sounds = buffer.read_bool(db)
            ignore_skin = buffer.read_bool(db)
            disable_storyboard = buffer.read_bool(db)
            disable_video = buffer.read_bool(db)
            visual_override = buffer.read_bool(db)
            last_modified2 = buffer.read_uint(db)
            scroll_speed = buffer.read_ubyte(db)
            
            sql.execute(
                "INSERT INTO maps VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (artist,artist_unicode,song_title,song_title_unicode,mapper,difficulty,audio_file,md5_hash,map_file,ranked_status,num_hitcircles,num_sliders,num_spinners,last_modified,approach_rate,circle_size,hp_drain,overall_difficulty,slider_velocity,drain_time,total_time,preview_time,beatmap_id,beatmap_set_id,thread_id,grade_standard,grade_taiko,grade_ctb,grade_mania,local_offset,stack_leniency,gameplay_mode,song_source,song_tags,online_offset,title_font,is_unplayed,last_played,is_osz2,folder_name,last_checked,ignore_sounds,ignore_skin,disable_storyboard,disable_video,visual_override,last_modified2,scroll_speed)
            )
        sql.commit()
        sql.close()

if __name__ == "__main__":
    if (len(sys.argv) != 3):
        print("Invalid args: osu_to_sqlite.py <osu!.db> <sqlite3.db>")
    else:
        create_db(sys.argv[1], sys.argv[2])