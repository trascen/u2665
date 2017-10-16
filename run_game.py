#! /usr/bin/env python

from gamelib.depcheck import check_dependencies

if check_dependencies():
    from gamelib import main
    main.main()