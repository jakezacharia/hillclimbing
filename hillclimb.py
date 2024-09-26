import random

# input range bounds
bounds1 = [-5.0, 5.0]
bounds2 = [0.0, 10.0]

# objective functions
def obj_f(x):
  return 2 - x**2

def obj_g(x):
  return (0.0051 * (x**5)) - (0.1367 * (x**4)) + (1.24 * (x**3)) - (4.456 * (x**2)) + (5.66 * (x)) - (0.287)


def hillclimbing(objective, bounds, step_size):
    # create initial randomized starting point
    solution = [bounds[0] + random.random() * (bounds[1] - bounds[0])]
    solution_eval = objective(solution[0])
    while True:
        # check both directions
        left_candidate = [solution[0] - step_size]
        right_candidate = [solution[0] + step_size]

        # ensure candidates are within bounds
        left_candidate[0] = max(bounds[0], min(bounds[1], left_candidate[0]))
        right_candidate[0] = max(bounds[0], min(bounds[1], right_candidate[0]))

        # evaluate candidate points with the objective function
        left_eval = objective(left_candidate[0])
        right_eval = objective(right_candidate[0])

        # determine the best candidate
        if left_eval > solution_eval or right_eval > solution_eval:
            if left_eval > right_eval:
                # move left if left is better
                solution, solution_eval = left_candidate, left_eval
            else:
                # move right if right is better
                solution, solution_eval = right_candidate, right_eval
        else:
            # if no improvement, stop (local maximum found)
            print(f"|| Local Maximum Found: {solution[0]:.5f} || Objective Value: {solution_eval:.5f} || Bounds: {bounds} || Step Size: {step_size}")
            break

    return solution[0], solution_eval

def random_restart(objective, bounds, step_size, restarts):
    best_solution = None
    best_solution_eval = float('-inf')  # start with negative infinity for maximization

    # run hill climbing multiple times from different random starting points
    for i in range(restarts):
        print(f"=>Restart [{i + 1}/{restarts}]")
        solution, solution_eval = hillclimbing(objective, bounds, step_size)

        # keep track of the best solution found
        if solution_eval > best_solution_eval:
            best_solution_eval = solution_eval
            best_solution = solution  # this will be a float now

    # p›››rint the best overall solution found
    if best_solution is not None:
        print(f"Best Local Maximum: {best_solution:.5f}, Objective Value: {best_solution_eval:.5f}")
    else:
        print("No valid solutions were found during the random restarts.")
    return best_solution, best_solution_eval


def main():
  # hill climbing
  print("Hill-Climbing Algorithm Results")
  hillclimbing(obj_f, bounds1, 0.5)
  hillclimbing(obj_f, bounds1, 0.1)
  print("Random-Restart Algorithm Results")
  random_restart(obj_g, bounds2, 0.5, 20)

  print("Comparison of g(x) between Hill-Climbing and Random-Restart")
  hillclimbing(obj_g, bounds2, 0.5)
  random_restart(obj_g, bounds2, 0.5, 20)


if __name__ == "__main__":
  main()