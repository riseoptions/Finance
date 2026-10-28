"""Iseseisva ülesande näidislahendus."""
import sqlite3
with sqlite3.connect(':memory:') as c:
    c.execute('CREATE TABLE p(currency TEXT, value REAL)')
    c.executemany('INSERT INTO p VALUES (?,?)',[('USD',100),('EUR',200),('USD',50)])
    total=c.execute('SELECT SUM(value) FROM p WHERE currency=?',('USD',)).fetchone()[0]
    assert total==150
    print(total)
