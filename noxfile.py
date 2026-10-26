import nox

pyproject = nox.project.load_toml("pyproject.toml")


@nox.session
def tests(session: nox.Session) -> None:
    session.install(".", *nox.project.dependency_groups(pyproject, "test"))
    session.run("python", "-m", "pytest", *session.posargs)


@nox.session
def docs(session: nox.Session) -> None:
    session.install(".", *nox.project.dependency_groups(pyproject, "docs"))
    for builder in ("html", "markdown"):
        session.run(
            "sphinx-build",
            "-M",
            builder,
            "docs",
            "docs/_build",
            "-W",
            "--keep-going",
        )
