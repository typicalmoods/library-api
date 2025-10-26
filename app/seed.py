#!/usr/bin/env python3
"""
Standalone script to seed the database with initial test data.
Run this script from the app directory: python seed.py
"""
import sys
from pathlib import Path

# Add the parent directory to the path to import src modules
sys.path.insert(0, str(Path(__file__).parent))

from src.seed_data import main

if __name__ == "__main__":
    main()
