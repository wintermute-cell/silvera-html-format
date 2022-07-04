#!/usr/bin/env python3

import re
import sys
from bs4 import BeautifulSoup as bs

# this is used to hack custom indent width on prettify()
r = re.compile(r'^(\s*)', re.MULTILINE)
def prettify_cust_space(s, encoding=None, formatter="minimal", indent_width=2):
    return r.sub(r'\1'*indent_width, s.prettify(encoding, formatter))

file_path = sys.argv[1]
if file_path is not None and file_path != "":
    formatted = ""

    with open(file_path, "r") as f:
        s = bs(f.read(), features='lxml')
        formatted = prettify_cust_space(indent_width=4)

    with open(file_path, "w") as f:
        f.write(formatted)