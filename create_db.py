import sqlite3
import os



db = \
"""
BEGIN TRANSACTION;
INSERT INTO auth_user VALUES(1,'pbkdf2_sha256$180000$TYSMLRe7zRCg$3zEKLYW5kn48O9JTmh5tvbbCrKOzfHGeeM6xGVAEZL8=','2020-07-18 18:54:48.549576',0,'bob','','',0,1,'2020-07-18 18:54:06.551643','');
INSERT INTO auth_user VALUES(2,'pbkdf2_sha256$180000$XNnR1s8tCrTw$0c1ikgpTeNoOTXEz4ZO5QOtkUyFRfVjyNyjpMoXGUVc=','2020-07-18 18:54:41.483579',0,'alice','','',0,1,'2020-07-18 18:54:15.508656','');
INSERT INTO pages_account(user_id, firstquestion, secondquestion) VALUES ('1', 'Finland', 'Bush');
INSERT INTO pages_account(user_id, firstquestion, secondquestion) VALUES ('2', 'Null', 'Null');
COMMIT;
"""


conn = sqlite3.connect('db.sqlite3')
conn.cursor().executescript(db)
conn.commit()
