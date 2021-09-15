import sys

argc = len(sys.argv)
for i in range (0, argc):
  print("[" + str(i) + "]: " + sys.argv[i])

print("__doc__: " + str(__doc__))
print("__file__: " + __file__)
print("__name__: " + __name__)
