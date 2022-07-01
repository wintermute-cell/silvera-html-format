#!/usr/bin/env python3

import sys
from bs4 import BeautifulSoup as bs

file_path = sys.argv[1]
if file_path is not None and file_path != "":
    formatted = ""

    with open(file_path, "r") as f:
        s = bs(f.read(), features='lxml')
        formatted = s.prettify()

    with open(file_path, "w") as f:
        f.write(formatted)