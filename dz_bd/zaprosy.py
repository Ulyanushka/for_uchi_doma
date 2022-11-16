import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

if __name__ == "__main__":
    con = QSqlDatabase.addDatabase("QSQLITE")
    con.setDatabaseName("contacts.sqlite")

    if not con.open():
        print("Database Error: %s" % con.lastError().databaseText())
        sys.exit(1)

    selectQuery = QSqlQuery()
    selectQuery.exec(
        """SELECT name, job, email FROM contacts""")

    print(selectQuery.first())

    name, job, email = range(3)
    print(selectQuery.value(name))

    selectQuery.next()
    selectQuery.next()

    print(selectQuery.value(email))

    while selectQuery.next():
        print(selectQuery.value(name), selectQuery.value(job), selectQuery.value(email))

    print(selectQuery.value(name))

    email = selectQuery.record().indexOf("email")

    selectQuery.last()
    print(selectQuery.value(email))

    print(selectQuery.isActive())
    selectQuery.finish()
    print(selectQuery.isActive())

    con.close()

    print(con.isOpen())
