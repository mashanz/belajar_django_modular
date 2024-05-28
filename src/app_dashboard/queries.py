from django.db import connection
from collections import namedtuple

# Merubah tuple menjadi dict/json
def dictfetchall(cursor):
    """
    Return all rows from a cursor as a dict.
    Assume the column names are unique.
    """
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]

def dictfetchone(cursor):
    """
    Return one row from a cursor as a dict.
    Assume the column names are unique.
    """
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, cursor.fetchone()))

# merubah tuple menjadi namedtuple
def namedtuplefetchall(cursor):
    """
    Return all rows from a cursor as a namedtuple.
    Assume the column names are unique.
    """
    desc = cursor.description
    nt_result = namedtuple("Result", [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def namedtuplefetchone(cursor):
    """
    Return one row from a cursor as a namedtuple.
    Assume the column names are unique.
    """
    desc = cursor.description
    nt_result = namedtuple("Result", [col[0] for col in desc])
    return nt_result(*cursor.fetchone())


# Create
def book_create(title: str, author: str) -> str:
    with connection.cursor() as cursor:
        cursor.execute("""
                INSERT INTO book
                    (title, author)
                VALUES (%s, %s)
                RETURNING *
        """, [title, author])
    return namedtuplefetchone(cursor)

# Read All
def book_read_all(limit:int = 10):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT id, title, author FROM book LIMIT %s
        """, [limit])
        return namedtuplefetchall(cursor)

# Read One
def book_read_one_by_id(id: str):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT id, title, author FROM book
            WHERE id = %s
        """, [id])
        return namedtuplefetchone(cursor)

# Update
def book_update(id: str, title: str, author: str):
    with connection.cursor() as cursor:
        cursor.execute("""
                UPDATE book
                SET title = %s, author = %s
                WHERE id = %s
                RETURNING *
        """, [title, author, id])
        return namedtuplefetchone(cursor)

# Delete
def book_delete(id: str):
    with connection.cursor() as cursor:
        cursor.execute("""
                DELETE FROM book
                WHERE id = %s
        """, [id])
        return f"Data dengan id={id} berhasil dihapus!"
