
def th(ints):
    total = 0
    for start, end in ints:
        total += end - start
    return total

ints = ((8, 18), (19,27), (16,29))
print(th(ints))