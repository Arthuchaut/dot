import sys
from libs.dot import Dot

if __name__ == '__main__':
    dot: Dot = Dot()
    dot.run(' '.join(sys.argv[1:]))