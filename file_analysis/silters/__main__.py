import sys
import os

try:
    option = sys.argv[1]
    file_path = sys.argv[2]
except BaseException as error:
    print('Run program: python -m silters (filter | annotate) <a file path>')
    raise BaseException

if os.path.isfile(file_path):
    pass


