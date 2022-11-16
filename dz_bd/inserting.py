import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQuery


if __name__ == "__main__":
    con = QSqlDatabase.addDatabase("QSQLITE")
    con.setDatabaseName("contacts.sqlite")

    if not con.open():
        print("Database Error: %s" % con.lastError().databaseText())
        sys.exit(1)

    #var 1

    name = "Ivan"
    job = "engineering assistant"
    email = "Ivan@bestcompany.com"

    insertQuery = QSqlQuery()
    insertQuery.exec(
        f"""
        INSERT INTO contacts (name, job, email)
        VALUES ('{name}', '{job}', '{email}')
        """)

    #var 2

    insertDataQuery = QSqlQuery()
    insertDataQuery.prepare(
        """
        INSERT INTO contacts (name, job, email)
        VALUES (?, ?, ?)
        """)

    data = [
        ("Nadya", "Project Manager", "Nadya@bestcompany.com"),
        ("Egor", "Scrum Master", "Egor@bestcompany.com"),
        ("Sofia", "Technical Leader", "Sofia@bestcompany.com")]

    for n, j, e in data:
        insertDataQuery.addBindValue(n)
        insertDataQuery.addBindValue(j)
        insertDataQuery.addBindValue(e)
        insertDataQuery.exec()

    con.close()
