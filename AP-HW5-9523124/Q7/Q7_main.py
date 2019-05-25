import sys

print(*sorted(set([int(sys.argv[i]) for i in range(1, len(sys.argv)) if i%6 == 0 and int(sys.argv[i])%6 == 0])))