#! /usr/bin/env python

from gamelib.depcheck import check_dependencies
from gamelib.depcheck import check_version

if check_version() and check_dependencies():
    from gamelib import main
    main.main()