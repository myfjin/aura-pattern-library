"""How this project resolves folder_nature, and which version it insists on.

Import this and call `add_dev_checkout()` BEFORE importing folder_nature, then
`require()` after. Both matter, and the order matters:

    from _check_folder_nature import add_dev_checkout as _dev, require as _require
    _dev()
    from folder_nature.mark import signing
    _require()

The default is the **installed package** — a released, verified artifact. That is
deliberate: this project used to insert a source checkout into sys.path unconditionally,
so on `.5` it ran whatever the working tree happened to contain, and on `.8` the path did
not exist and it silently ran whatever pip had installed there. From the same commit of
this repository, the two machines ran different mark layers, and nothing recorded which
was intended.

Set **FOLDER_NATURE_DEV=1** to develop against `~/Projects/folder-nature` instead. If the
flag is set and that checkout is missing, that is an error, not a fallback: you asked for
the checkout, and quietly getting the installed copy is how the drift started.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

DEV_FLAG = "FOLDER_NATURE_DEV"
DEV_CHECKOUT = Path.home() / "Projects" / "folder-nature"

# The mark layer changed in 0.2.2 and 0.2.3, and both changes matter here:
#   0.2.2 — re-stamping became idempotent again. Before it, an indented channel-A mark line
#           was not recognised, so the OLD frame survived beside the new one while the file
#           still verified as authentic. This tree carries channel-A frames in 2,997 files.
#   0.2.3 — the manifest's `created` is the UTC date, not the local clock.
MIN_VERSION = (0, 2, 3)

RELEASES = "https://github.com/myfjin/folder-nature/releases"


def _dev_requested() -> bool:
    return os.environ.get(DEV_FLAG, "").strip().lower() in ("1", "true", "yes", "on")


def add_dev_checkout() -> None:
    """Put the local checkout on sys.path — only if asked, and only if it exists."""
    if not _dev_requested():
        return
    if not DEV_CHECKOUT.is_dir():
        raise RuntimeError(
            f"{DEV_FLAG} is set but {DEV_CHECKOUT} does not exist. You asked for the local "
            "checkout; getting the installed package instead would be exactly the silent "
            f"substitution this flag exists to prevent. Unset {DEV_FLAG} to use the "
            "installed folder-nature."
        )
    sys.path.insert(0, str(DEV_CHECKOUT))


def require() -> None:
    """Raise unless the resolved folder_nature is at least MIN_VERSION.

    Imports folder_nature *here*, not at module import, so the answer is whatever
    add_dev_checkout() just decided. Names the version found AND the path it came from.
    """
    import folder_nature

    found = tuple(int(p) for p in folder_nature.__version__.split(".") if p.isdigit())[:3]
    if found < MIN_VERSION:
        raise RuntimeError(
            f"this project needs folder-nature >= {'.'.join(map(str, MIN_VERSION))}, "
            f"found {folder_nature.__version__} at {folder_nature.__file__}. "
            f"See {RELEASES}"
        )
