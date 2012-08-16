import random


def toss(seed, choices, winner_count=1):
    choices_len = len(choices)
    if winner_count > choices_len:
        winner_count = choices_len
    r = random.Random(seed)
    return sorted(r.sample(sorted(choices), winner_count))
