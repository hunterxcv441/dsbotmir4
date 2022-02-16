import discord
import time
import json
import pandas as pd
from discord.ext import commands
import sqlite3
con = sqlite3.connect('database.db')
c = con.cursor()

#c.execute("INSERT INTO dsbot VALUES ('Buch','16:00:00','Stone I')")
#c.execute("INSERT INTO dsbot VALUES ('Buch2','16:00:00','Stone II')")
#data = c.execute('SELECT * FROM dsbot')delete from mytable where id = 1
#c.execute("DELETE FROM dsbot WHERE discord_name = 'Buch2'")
#df = pd.read_sql('SELECT * FROM dsbot', con)
#df = df.rename(columns={'discord_name': 'Nome', 'date': 'Hora de inicio', 'plocal': 'Local'})
#df2 = pd.DataFrame(df, columns=['discord_name'])
selectquery = "SELECT discord_role_name FROM dsbot_roles"
c.execute("SELECT discord_role_name FROM dsbot_roles")
xf = c.fetchone()[0]
print(xf)
con.commit()
#print(df)
con.close()