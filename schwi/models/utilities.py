# This file is part of Schwi.
# Copyright 2019-2020, Frostflake (L.A.)
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

from os import path


def get_db_path():
    return path.join(path.expanduser("~"), ".config", "schwi")


def get_global_config_path():
    return path.join(get_db_path(), "db", "global.json")


def get_anime_path(id):
    return path.join(get_db_path(), "db", "anime", str(id) + ".json")
