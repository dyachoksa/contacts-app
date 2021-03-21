import datetime as dt
import sqlite3
import sys


def create_tables(conn):
    sql = """
CREATE TABLE contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(150) NOT NULL,
    email VARCHAR(150) NOT NULL,
    created_at DATETIME
);

CREATE INDEX idx_contacts_name ON contacts(name);
CREATE INDEX idx_contacts_email ON contacts(email);
    """

    cur = conn.cursor()

    res = cur.executescript(sql)
    print(res.rowcount, "queries were executed.")


def create_records(conn):
    records = [
        {
            "name": "Jackson Alexander",
            "email": "jackson.alexander@example.com",
            "created_at": dt.datetime.utcnow(),
        },
        {
            "name": "Jacks Nichols",
            "email": "jacks.nichols@example.com",
            "created_at": dt.datetime.utcnow(),
        },
    ]

    sql = "INSERT INTO contacts (name, email, created_at) VALUES (:name, :email, :created_at)"
    cur = conn.cursor()

    res = cur.executemany(sql, records)
    print(res.rowcount, "records were inserted.")

    conn.commit()


def query_data(conn):
    sql = "SELECT * FROM contacts"

    cur = conn.cursor()
    res = cur.execute(sql)

    for row in cur:
        print(dict(row))
        # print(tuple(row))

    # data = res.fetchall()


def main():
    conn = sqlite3.connect("data/contacts.sqlite3")
    conn.row_factory = sqlite3.Row

    if len(sys.argv) > 1:
        if sys.argv[1] == "--create":
            create_tables(conn)
        elif sys.argv[1] == "--insert":
            create_records(conn)

    query_data(conn)
    conn.close()


if __name__ == "__main__":
    main()
