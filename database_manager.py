import sqlite3 as sql


def listExtension():
    with sql.connect("database/data_source.db") as con:
        cur = con.cursor()
        data = cur.execute("SELECT * FROM extension").fetchall()
    return data


def insertContact(email, name):
    con = sql.connect("database/data_source.db")
    try:
        with con:
            con.execute(
                "INSERT INTO contact_list (email, name) VALUES (?, ?)",
                (email, name),
            )
    finally:
        con.close()


def deleteContact(email):

    with sql.connect("database/data_source.db") as con:
        cur = con.cursor()
        # Using parameterised query to prevent SQL injection
        cur.execute("DELETE FROM contact_list WHERE email = ?", (email,))
        con.commit()
