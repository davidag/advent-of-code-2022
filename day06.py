from collections import deque
import common as c

START_PACKET_MARKER_LENGTH = 4
START_MSG_MARKER_LENGTH = 14

# part 1: find start packer marker

signal = c.day(6)


def find_marker(signal, length):
    d = deque(maxlen=length)

    for i, s in enumerate(signal):
        d.append(s)
        if len(set(d)) == length:
            return i + 1


print(find_marker(signal, START_PACKET_MARKER_LENGTH))

# part 2: find start msg marker

print(find_marker(signal, START_MSG_MARKER_LENGTH))
