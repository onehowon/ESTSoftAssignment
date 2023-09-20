def choose(things, cartsize):
  chosen = []
  chosen_size = 0
  for thing in things:
    if chosen_size+thing <= cartsize:
      chosen.append(thing)
      chosen_size += thing
  return chosen

import random

total_moves = 0

for mission in range(10000):

  things = []
  for i in range(10):
    things.append(random.randrange(1,11))

  while len(things) >0:
    chosen = choose(things, 15)

    for thing in chosen:
      things.remove(thing)
    total_moves += 1

print('총 이동: ', total_moves)