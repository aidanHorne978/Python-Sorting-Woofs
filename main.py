import sys

data = sys.stdin.readline().rstrip()
lines = []

while data:
    lines.append(data.split())
    data = sys.stdin.readline().rstrip()

woof = ['p', 'q', 'r', 's']
leader = ['C', 'A', 'K', 'E']


# go backwards through the string
def findWoof(data):
    woof_count = 0
    for result in data:
        for r in result[::-1]:
            if r not in woof:
                if r not in leader:
                    if r != "N":
                        return False
            if r in woof:
                woof_count += 1
            if r in leader and woof_count < 2:
                woof_count = 0
                break
            if r in leader and woof_count >= 2:
                woof_count -= 1
            if r == "N" and woof_count < 1:
                woof_count = 0
                break
            if r == 'N' and woof_count == 1:
                pass

    if woof_count == 1:
        return True
    else:
        return False


for result in lines:
    if findWoof(result):
        print("woof")
    else:
        print("not woof")