import re
from collections import deque

def get_sequence(max, players):
    sequence = deque()
    scores = [0] * players
    for marble in range(0, max + 1):
        if marble % 23 == 0 and marble > 0:
            current_player = marble % players
            sequence.rotate(-7)

            scores[current_player] += marble + sequence.pop()
            #print(sequence)
            print("Special", sequence)
        else:
            sequence.rotate(2)
            #print(sequence)
            sequence.append(marble)
            print(sequence)
    return scores

scores = get_sequence(10, 423)
print(max(scores))
