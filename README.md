APC 524 - Homework 3

Either accept the GitHub classroom link on Canvas or clone this repository into a new private one under `https://github.com/APC524-F2026`.
We recommend that you use the name `ci-exercice-{NETID}`.

In this repo is a basic project, with some code in `src/unc/__init__.py` and
some tests in `tests/`. The main code requires `typing_extensions` if running
on Python < 3.13, while the tests require `pytest` and `uncertainties`. The minimum
supported Python is 3.11.

Add the following files:

* `pyproject.toml`: Setup a basic project. Include at least:
    * A build backend. `hatchling` recommended, but any one should work.
    * A project table with at least name, version, requires-python, and dependencies. The only dependency is `typing_extesions; python_version<"3.13"`.
    * A `[dependency-groups]` table with a `test` group (dependencies listed above) and a `docs` group, with `"sphinx"`, `"furo"`, `"myst_parser"`, and `"sphinx-markdown-builder"`.
* `.pre-commit-config.yaml`: Add at least the following checks:
    * Basic checks (pre-commit/pre-commit-hooks) with at least `trailing-whitespace`.
    * A formatter check (probably ruff-format)
    * Ruff with at least the default checks,  bugbear (B), isort (I),
      Ruff-specific (RUF), and PyUpgrade (UP). Use `extend-select` to ensure
      the default checks are present.
* `docs/conf.py`: The configuration file for Sphinx documentation. This should have:
    * `project`: the name of the project
    * `extensions`: This should have `myst_parser`, `sphinx.ext.autodoc`, and `sphinx-markdown-builder`.
    * `source_suffix`: This should have both `".rst"` and `".md"`
    * `html_theme`: This should be set to `"furo"`

> [!tip]
>
> `sphinx-markdown-builder` is used to generate a markdown version of the API page, which is appended to the summary of the `online_doc.yml` workflow, which can be viewed on GitHub. After setting up your `pyproject.toml` and `docs/conf.py`, this workflow should run successfully.
* `noxfile.py`: Add at least the following sessions. Optionally, you can add a formatting session or anything else useful, but at least include:
    * `tests`: `nox -s tests` should run your tests. Use the `tests` group defined above, do not list dependencies explicitly here.
    * `docs`: `nox -s docs` should build your documentation. You can have it also open a web browser if you like.
* `.github/workflows/ci.yml`: Add two jobs.
    * Format: this should run pre-commit. Manually implement, or use the pre-commit action, or nox. Doesn't matter how you do it, but it should show the diff on failure.
    * Tests: run your tests. Either through nox or by hand, but again, use the `tests` group, don't list `pytest`, etc. Use `ubuntu-latests` and run both minimum and maximum supported Pythons (3.11 and 3.13), either with a matrix, or with nox, or both. Feel free to uv to install, either directly or through nox.
    * The workflow to generate docs has already been made for you. The workflow generates HTML which can be downloaded as an artifact and outputs the `API` page as a workflow summary (see the actions tab of your private repository). This page is automatically generated from the type hints and docstrings in `src/unc/__init__.py`, as per `docs/api.rst`.
    * For full credit, make sure that the `main` branch performs all jobs successfully. You may need to format `src/unc/__init__.py` to pass `Format`.
* `tests/conftest.py`
    * Replace the `@pairs` `pytest`-mark in `test_stdunc.py` with a fixture in `conftest.py`. By naming the fixture `ab`, e.g.:

      ```python
      @pytest.fixture(params=list_of_permutations)
      def ab(request): ...
      ```

      you can remove the `@pairs` decorators in `test_stdunc.py` without needing to change the argument to each test.

    * Add a test (using the above fixture) to `test_labunc.py` for the following mathematical properties:
      * Commutativity of addition: `LabUnc(*a) + LabUnc(*b) == LabUnc(*b) + LabUnc(*a)`
      * Commutativity of multiplication: `LabUnc(*a) * LabUnc(*b) == LabUnc(*b) * LabUnc(*a)`

      You should have 126 tests in total. Note that by adding the fixture to `conftest.py`, it is usable in both `test_labunc.py` and `test_stdunc.py`.

As you add these, verify it works at each step. There might be mistakes in the code that you will expose with these checks, fix them if needed and list each fix in `CHANGELOG.md`. You do not need to list automatic formatting changes, just bugfixes.

> [!tip]
>
> This is covered (including documentation setup) in the [Scientific-Python Development Guide](https://learn.scientific-python.org/development). Also see [week 5 of the course material](https://se-for-sci.github.io/ci/).

> [!tip]
>
> [`uv`](https://docs.astral.sh/uv) can help. Specifically, you can even get started with your `pyproject.toml` using `uv init --lib --name unc`!
