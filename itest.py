from __future__ import unicode_literals
import os

if __name__ == '__main__':
    for i in range(10000):
        f = open("/Users/data/{}.txt".format(i), "w")
        f.write("test: " + str(i))
        f.close()
