import os

name = 'eqt_ext'


def get_eqt_ext_static_dir():
    return os.path.join(os.path.dirname(__file__), '_static')
