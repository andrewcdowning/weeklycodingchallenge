# def uncompress(s):
#   times = ''
#   uncompressed = ''
#   for i in s:
#     if i.isdigit():
#       times += i
#     else:
#       uncompressed += (i * int(times))
#       times = ''
#   return uncompressed


def uncompress(s):
    uncompressed = []
    i = 0
    j = 0
    while j < len(s):
        if s[j].isdigit():
            j += 1
        else:
            uncompressed.append(s[j] * int(s[i:j]))
            j += 1
            i = j

    # string concat outside of loop
    return ''.join(uncompressed)
