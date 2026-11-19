# -*- mode: python ; coding: utf-8 -*-
"""PyInstaller spec: single-file muse2api binary (Linux x86_64 release build)."""

from PyInstaller.utils.hooks import collect_all

datas = [("static", "static")]
binaries = []
hiddenimports = []

# Packages that ship native extensions or load submodules dynamically.
# collect_all keeps their data files/binaries/hidden imports together.
_COLLECT = (
    "uvicorn",
    "uvloop",
    "httptools",
    "websockets",
    "websocket",
    "socksio",
    "socks",
    "nacl",
    "tzdata",
    "curl_cffi",
    "fastapi",
    "starlette",
    "anyio",
    "httpx",
    "httpcore",
    "pydantic",
    "pydantic_settings",
    "itsdangerous",
    "dotenv",
    "cryptography",
    "PIL",
    "google.protobuf",
)

for _pkg in _COLLECT:
    try:
        _d, _b, _h = collect_all(_pkg)
    except Exception as exc:  # optional package missing -> skip
        print(f"[spec] skip {_pkg}: {exc}")
        continue
    datas += _d
    binaries += _b
    hiddenimports += _h

a = Analysis(
    ["run.py"],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=["tests", "pytest", "tkinter", "matplotlib", "IPython"],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name="muse2api",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
