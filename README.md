# wxPython project template

A minimal, production-oriented starting point for desktop applications built with [wxPython](https://www.wxpython.org/) and managed with [uv](https://docs.astral.sh/uv/). The project uses a standard **src layout**, an installable package under `src/wx_python_project_template`, and a small demo window (menus, status bar, and a simple interactive panel).

## Requirements

- Python **3.10** or newer
- [uv](https://docs.astral.sh/uv/installation/) installed on your system

On Windows, wxPython ships wheels for common architectures; use a supported Python build (64-bit recommended) for the best experience.

## Quick start

Clone or copy this repository, then from the project root:

```bash
uv sync
```

That creates a virtual environment (`.venv`), installs dependencies from the lockfile, and installs this project in editable mode.

### Run the application

Any of the following work:

```bash
uv run main.py
```

```bash
uv run python -m wx_python_project_template
```

```bash
uv run wx-python-app
```

The last command uses the console script defined in `pyproject.toml`.

## Project layout

```
.
├── main.py                      # Optional root entrypoint (calls the packaged app)
├── pyproject.toml               # Project metadata, dependencies, build, scripts
├── uv.lock                      # Locked dependency versions (commit this for reproducible installs)
└── src/
    └── wx_python_project_template/
        ├── __init__.py          # Package exports and version
        ├── __main__.py          # Enables: python -m wx_python_project_template
        ├── main.py              # wx.App bootstrap and event loop
        └── main_window.py       # Main frame and UI
```

## Development

| Task | Command |
|------|---------|
| Install dependencies and sync the environment | `uv sync` |
| Add a dependency | `uv add <package>` |
| Add a dev-only dependency | `uv add --dev <package>` |
| Run the app with the project environment | `uv run …` (see above) |
| Build wheel and sdist | `uv build` |

After changing dependencies, `uv.lock` is updated automatically when you run `uv add` or `uv lock`; commit the lockfile so others get the same resolved versions.

## Customizing this template

1. Rename the package directory under `src/` and the import name `wx_python_project_template` to match your product (update `pyproject.toml` `[tool.hatch.build.targets.wheel]` `packages` and `[project.scripts]` accordingly).
2. Bump the version in `pyproject.toml` and in `wx_python_project_template/__init__.py` if you keep a `__version__` string there.
3. Replace the demo UI in `main_window.py` with your real screens and dialogs.

## References

- [wxPython documentation](https://docs.wxpython.org/)
- [uv documentation](https://docs.astral.sh/uv/)
