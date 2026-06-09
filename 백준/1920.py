from sys import stdin, stdout

n = stdin.readline()
set_n = set(stdin.readline().split())
m = stdin.readline()
set_m = stdin.readline().split()

for flag in set_m:
    stdout.write('1\n') if flag in set_n else stdout.write('0\n')