"""Entrypoint for frozen (PyInstaller) builds; also works as `python run.py`."""

from __future__ import annotations

from app.main import run

if __name__ == "__main__":
    run()
