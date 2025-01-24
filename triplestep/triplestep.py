#Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time. Implement a method to count how many possible ways the child can run up the stairs.

#tip: use recursion
times_called  = 0

def triplestep(steps: int):
   global times_called
   times_called += 1
   print(f'times_called {times_called}')
   if steps <= 0:
         return 0
   if steps == 1:
         return 1
   return (1 + triplestep(steps - 1) + triplestep(steps - 2) + triplestep(steps - 3))

def triplestep_nonrecursive(steps: int):
   # Your solution goes here
   return "the answer"

