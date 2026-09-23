"""One place for the folder_nature version floor.

Import this AFTER the sys.path insert, so it checks whatever this script will actually
resolve — not what you hoped it would.

Six entry points need the same floor. Keeping it here means one place to move it, and one
place to change how a version string is parsed.
"""

from __future__ import annotations

import folder_nature

# The mark layer changed in 0.2.2 and 0.2.3, and both changes matter to this library:
#   0.2.2 — re-stamping became idempotent again. Before it, an indented channel-A mark line
#           was not recognised, so the OLD frame survived beside the new one while the file
#           still verified as authentic. This tree carries channel-A frames in 2,997 files.
#   0.2.3 — the manifest's `created` is the UTC date, not the local clock.
MIN_VERSION = (0, 2, 3)

RELEASES = "https://github.com/myfjin/folder-nature/releases"


def require() -> None:
    """Raise unless the resolved folder_nature is at least MIN_VERSION.

    Names the version found AND the path it came from: this repository resolves
    folder_nature by inserting a source path into sys.path, so which mark layer it runs
    depends on where that checkout happens to be — and on .8 the path does not exist, so
    the import falls through to whatever pip installed there.
    """
    found = tuple(int(p) for p in folder_nature.__version__.split(".") if p.isdigit())[:3]
    if found < MIN_VERSION:
        raise RuntimeError(
            f"this project needs folder-nature >= {'.'.join(map(str, MIN_VERSION))}, "
            f"found {folder_nature.__version__} at {folder_nature.__file__}. "
            f"See {RELEASES}"
        )
