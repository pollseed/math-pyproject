__author__ = 'shn'

# ランダムウォーク

import random

position = 0
walk = [position]
steps = 1000
for i in xrange(steps):

    # 与えられた整数範囲内での整数乱数を返す.
    step = 1 if random.randint(0, 1) else -1
    position += step
    walk.append(position)