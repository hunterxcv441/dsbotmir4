import sqlite3

con = sqlite3.connect('database.db')
c = con.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS dsbot
          ([discord_id] TEXT PRIMARY KEY, [discord_name] TEXT, [date] TEXT,  [ticket] TEXT,  [plocal] TEXT)
          ''')

c.execute('''
          CREATE TABLE IF NOT EXISTS dsbot_p2
          ([discord_id] TEXT PRIMARY KEY, [discord_name] TEXT, [date] TEXT,  [ticket] TEXT,  [plocal] TEXT)
          ''')
c.execute('''
          CREATE TABLE IF NOT EXISTS dsbot_p3
          ([discord_id] TEXT PRIMARY KEY, [discord_name] TEXT, [date] TEXT,  [ticket] TEXT,  [plocal] TEXT)
          ''')
c.execute('''
          CREATE TABLE IF NOT EXISTS dsbot_p4
          ([discord_id] TEXT PRIMARY KEY, [discord_name] TEXT, [date] TEXT,  [ticket] TEXT,  [plocal] TEXT)
          ''')
c.execute('''
          CREATE TABLE IF NOT EXISTS dsbot_p5
          ([discord_id] TEXT PRIMARY KEY, [discord_name] TEXT, [date] TEXT,  [ticket] TEXT,  [plocal] TEXT)
          ''')

c.execute('''
          CREATE TABLE IF NOT EXISTS dsbot_p6
          ([discord_id] TEXT PRIMARY KEY, [discord_name] TEXT, [date] TEXT,  [ticket] TEXT,  [plocal] TEXT)
          ''')

c.execute('''
          CREATE TABLE IF NOT EXISTS dsbot_p7
          ([discord_id] TEXT PRIMARY KEY, [discord_name] TEXT, [date] TEXT,  [ticket] TEXT,  [plocal] TEXT)
          ''')



c.execute('''
          CREATE TABLE IF NOT EXISTS dsbot_roles
          ([id] INTEGER PRIMARY KEY, [discord_role_name] TEXT, [date] TEXT)
          ''')