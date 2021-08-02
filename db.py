import sqlite3
import os
from pathlib import Path

class db:

    def __init__(self,path):
        self.path = Path(path)
        if not self.path.exists():
            self.__create_table()

    def __create_table(self):
        con = sqlite3.connect(self.path.absolute().as_posix())
        try:
            cur = con.cursor()
            cur.executescript(
                '''
                CREATE TABLE uuts(
                    id INTEGER PRIMARY KEY,
                    platform VARCHAR(50),
                    sn VARCHAR(50),
                    bios VARCHAR(50),
                    os VARCHAR(50),
                    operator VARCHAR(50),
                    imsi VARCHAR(50),
                    iccid VARCHAR(50),
                    module text,
                    tracker_version VARCHAR(50)
                );

                CREATE TABLE ftdata(
                    id INTEGER PRIMARY KEY,
                    uut_id INTEGER,
                    time DATETIME,
                    lat text,
                    lng text,
                    status VARCHAR(50),
                    apn VARCHAR(50),
                    cellid VARCHAR(50),
                    rsrp_rssi VARCHAR(50),
                    bandinfo  VARCHAR(50),
                    error_status text,
                    FOREIGN KEY (uut_id) REFERENCES uuts(id)
                );
                '''
            )
            con.close()
        except:
            con.close()
            os.remove(self.path.absolute().as_posix())

def create_db():
    db('tracker_data.db')


    

    