import nox

locations = "flaskr", "tests", "noxfile.py"
nox.options.sessions = "lint", "tests"


@nox.session(python=["3.8", "3.7"])
def lint(session):
    args = session.posargs or locations
    session.install("flake8", "flake8-black", "flake8-import-order")
    session.run("flake8", *args)


@nox.session
def tests(session):
    session.install("pytest")
    session.run("pytest")


@nox.session(python="3.7")
def black(session):
    args = session.posargs or locations
    session.install("black")
    session.run("black", *args)
