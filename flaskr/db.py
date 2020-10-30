import psycopg2

import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    if "db" not in g:
        g.db = psycopg2.connect(
            dbname=current_app.config["DATABASE_NAME"],
            user=current_app.config["DATABASE_USER"],
            password=current_app.config["DATABASE_PASSWORD"],
            host=current_app.config["DATABASE_HOST"],
            port=current_app.config["DATABASE_PORT"],
        )
    return g.db


def init_db():
    db = get_db()

    with current_app.open_resource("schema.sql") as f:
        cur = db.cursor()
        cur.execute(f.read().decode("utf8"))
        db.commit()
        cur.close()


def create_user(user):
    db = get_db()
    cur = db.cursor()
    cur.execute(
        """
        INSERT INTO public.user (username, email, firstname, jumpcloud_id)
        VALUES (%s, %s, %s, %s);
        """,
        (user["username"], user["email"], user["firstname"], user["_id"]),
    )
    db.commit()
    cur.close()


def update_user(user):
    db = get_db()
    cur = db.cursor()
    cur.execute(
        """
        UPDATE public.user SET
        username = %s, email = %s, firstname = %s
        WHERE jumpcloud_id = %s
        """,
        (user["username"], user["email"], user["firstname"], user["_id"]),
    )
    db.commit()
    cur.close()


def delete_user(user):
    db = get_db()
    cur = db.cursor()
    cur.execute(
        """
        DELETE FROM public.user
        WHERE jumpcloud_id = %s
        """,
        (user["id"],),
    )
    db.commit()
    cur.close()


def close_db(e=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


@click.command("init-db")
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo("Initialized the database.")


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
