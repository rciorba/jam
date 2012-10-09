import collections

Result = collections.namedtuple("Result", ["best", "surprising"])

def cap(func):
    def capped(total):
        return tuple(
            r for r in func(total)
            if r.best<=10)
    return capped

@cap
def maximums(total):
    if total == 0:
        return (Result(0, False), )
    elif total == 1:
        return (Result(1, False), )
    root = total / 3
    mod = total % 3
    if mod == 0:
        return (Result(root, False),
                Result(root+1, True))
    elif mod == 1:
        return (Result(root+1, False),
                Result(root+1, True))
    elif mod == 2:
        return (Result(root+1, False),
                Result(root+2, True))

def combinator(solutions):
    if len(solutions) == 0:
        yield []
        return
    for solution in solutions[0]:
        for _solutions in combinator(solutions[1:]):
            yield [solution ,] + _solutions

def acceptor(solution, expected_s, min_score):
    surprising = 0
    count = 0
    for result in solution:
        if result.best >= min_score:
            count += 1
        surprising += int(result.surprising)
    return (count, solution) if (surprising == expected_s) else (None, solution)

# for sol in (acceptor(s, 1) for s in combinator([maximums(n) for n in [5, 20]])):
#     print sol


def solve(problem):
    # print problem
    surprising = problem[1]
    min_score = problem[2]
    solutions = [s for s in combinator([maximums(n) for n in problem[3:]])]
    # print ">>", solutions
    solutions = [
        acceptor(s, surprising, min_score)
        for s in solutions]
    # for s in solutions:
    #     print s
    return max([s[0] for s in solutions if s[0] is not None])

def main():
    import sys
    data = open(sys.argv[1]).readlines()
    case = 1
    for line in data[1:]:
        # print >> sys.stderr, line[0:-1]
        problem = [int(n) for n in line.split()]
        print "Case #%d: %s" % (case, solve(problem))
        # solve([int(r) for r in line.split()])
        case += 1
        
if __name__ == "__main__":
    main()
