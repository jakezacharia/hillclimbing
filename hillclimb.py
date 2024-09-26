import random

# input range bounds
bounds1 = [-5.0, 5.0]
bounds2 = [0, 10.0]

# objective functions
def obj_f(x):
  return 2 - x**2

def obj_g(x):
  return (0.0051 * (x**5)) - (0.1367 * (x**4)) + (1.24 * (x**3)) - (4.456 * (x**2)) + (5.66 * (x)) - (0.287)


# hill climbing local search algorithm
def hillclimbing(objective, bounds, iterations, step_size):
  # create initial starting point
  solution = [bounds[0] + random.random() * (bounds[1] - bounds[0])]
  # evaluate the initial point
  solution_eval = objective(solution[0])
  for i in range(iterations):
    # step
    step_direction = random.choice([-1, 1])
    candidate = [solution[0] + step_direction * random.random() * step_size]
    # ensure the candidate is within bounds
    candidate[0] = max(bounds[0], min(bounds[1], candidate[0]))
    # evaluate candidate point w/ objective function f(x)
    candidate_eval = objective(candidate[0])
    # check if we should keep the new point
    if candidate_eval >= solution_eval:
      # store the new point
      solution, solution_eval = candidate, candidate_eval
      # report progress
  print('>%d f(%s) = %.5f' % (i, solution, solution_eval))
  return [solution, solution_eval]


def main():
  ## test cases
  hillclimbing(obj_f, bounds1, 100, 0.5)
  hillclimbing(obj_f, bounds1, 100, 0.1)



if __name__ == "__main__":
  main()