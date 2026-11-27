#!/usr/bin/env python3
# APL - لغة عمار البرمجية
# Copyright (c) 2026 Ammar Elkhateeb (AmmarBasha2011)
# Distributed under the Python Software Foundation License Version 2 (PSF-2.0),
# the same license as Python. See LICENSE and NOTICE.
"""Entry point: `python apl.py` or the عمار command."""

import sys, os

# Add script directory to path so core/ can be found
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.cli import main

if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except BrokenPipeError:
        # `python apl.py help | head` closes the pipe early: exit quietly
        try:
            sys.stdout.close()
        finally:
            os._exit(0)
    except KeyboardInterrupt:
        print()
        os._exit(130)
