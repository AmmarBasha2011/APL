#!/usr/bin/env python3
# APL - Ammar Programming Language
# Entry point — runs the core runner

import sys, os

# Add script directory to path so core/ can be found
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.apl_runner import main

if __name__ == "__main__":
    main()
