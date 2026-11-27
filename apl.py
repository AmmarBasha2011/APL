#!/usr/bin/env python3
# APL - Ammar Programming Language
# Entry point — runs the core runner

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
