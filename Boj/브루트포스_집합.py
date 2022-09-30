import sys

S = set()
T = int(sys.stdin.readline())
for i in range(T):
    cmd1 = sys.stdin.readline().split()
    if len(cmd1) == 1:
        if cmd1[0] == 'all':
            S = set([x for x in range(1, 21)])
        else:
            S = set()

    else:
        cmd, x = cmd1[0], int(cmd1[1])
        if cmd == 'add':
            S.add(x)
        elif cmd == 'check':
            if x in S:
                print(1)
            else:
                print(0)
        elif cmd == 'remove':
            if x in S:
                S.discard(x)
        elif cmd == 'toggle':
            if x in S:
                S.discard(x)
            else:
                S.add(x)