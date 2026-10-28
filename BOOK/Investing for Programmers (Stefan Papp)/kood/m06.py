"""[NÄIDE] Varamonitor, valuuta ja SQL — vt mooduli selgitust."""
import sqlite3
with sqlite3.connect(':memory:') as c:
    c.execute('CREATE TABLE pos(nimi TEXT, kogus REAL, hind REAL, eur_kurss REAL)')
    c.executemany('INSERT INTO pos VALUES (?,?,?,?)',[('Aktsia',10,100,.92),('EUR',500,1,1)])
    print('Väärtus EUR',c.execute('SELECT SUM(kogus*hind*eur_kurss) FROM pos').fetchone()[0])
