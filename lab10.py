# Problem-solving practice 2 (competition / LeetCode style) - a step up in difficulty.
#
# Most of these are natural fits for a STACK or a QUEUE (this week's data structures).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.
import collections

def eval_rpn(tokens):
    # Outline (write your plan here first):
    #  Have da list
    # if it is a number, put ito a new list.
    # when u approach an operation, perform that operation with the last two in the list digits
    #recursive loop  until empty
    result = []
    for elem in tokens:
        if elem.lstrip("-").isdigit():
            result.append(int(elem))
        else:
            a = result.pop()
            b = result.pop()
            if elem == "+":
                result.append(a+b)
            elif elem == "-":
                result.append(a-b)
            elif elem == "*":
                result.append(a*b)
            elif elem == "/":
                result.append(int(b/a))
    return result[0]
                


    # TODO: `tokens` is a list of strings in Reverse Polish Notation - either an integer
    #   or one of the operators "+", "-", "*", "/". Evaluate it and return the integer
    #   result. Division should truncate toward zero (int(a / b)).
    #   Example: ["2","1","+","3","*"]  ->  9


def decode_string(s):
    stack = []

    for i in range (len(s)):
        if s[i] != "]":
            stack.append(s[i])
        else:
            substr = ""
            while stack[-1] != "[":
                substr = stack.pop() + substr
            stack.pop()

            k = ""
            while stack and stack[-1].isdigit():
                k = stack.pop() + k
            stack.append(int(k) * substr)

    return "".join(stack)
    # Outline:
    # first case:
    # k[k[k[c]]]
    # it would k1 * c = ccc
    # then k2 * ccc
    # then k3 * (k2*ccc)
    # then final resukt
    # SECOND CASE:
    # (k[ck[c]])
    # take first case [c] and multiply by k
    # (k[c[k*c]])
    # then add c to front
    # (k[c(k*c)])
    # then multiply whole thing by k
    # k(c(k*c))

    # TODO: decode a string written with the rule k[encoded], meaning `encoded` repeated
    #   k times. The brackets can be nested.
    #   Example: "3[a2[c]]"  ->  "accaccacc"

def daily_temperatures(temps):
    # Outline:
    #  a for loop
    # for each integer at [i], pop it out and compare with rest values
    # once you find something at [i+n] which is > [i]
    # return aount of positions
    # then move to tbe next and repeat
    # if not [i+n] is never > [i], return zero
    res = [0] * len(temps)
    stack = []

    for i, t in enumerate(temps):
        while stack and t > stack[-1][0]:
            stackT, stackI = stack.pop()
            res[stackI] = (i - stackI)
        stack.append([t, i])
    return res
    # TODO: for each day, return how many days you'd wait for a WARMER temperature.
    #   Put 0 if no warmer day ever comes.
    #   Example: [73,74,75,71,69,72,76,73]  ->  [1,1,4,2,1,1,0,0]
    


def num_islands(grid):   # Part 4 - stretch (optional)
    # Outline:
    #   Start a position zero 
    # if its a one, check left right up and down if there are neighboring
    # if so, check those til you create a border of zeros. 
    # count that island
    # keep doing that

    # lowkeyy followed a video for all of these to understand, lots of popping going on
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visit = set()
    islands = 0

    def bfs(r, c):
        q = collections.deque()
        visit.add((r,c))
        q.append((r,c))

        while q:
            row, col = q.popleft()
            directions = [[1,0], [-1, 0], [0, 1], [0, -1]]

            for dr, dc in directions:
                r, c = row + dr, col + dc
                if (r in range(rows) and
                    c in range(cols) and
                    grid [r][c] == "1" and
                    (r, c) not in visit):
                    q.append((r, c))
                    visit.add((r,c))
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visit:
                bfs(r, c)
                islands += 1

    # TODO: `grid` is a list of equal-length strings of "1" (land) and "0" (water).
    #   Count the islands - groups of "1"s connected up/down/left/right (not diagonally).
    #   Example: ["11000","11000","00100","00011"]  ->  3
    return islands


def main():
    # Optional scratch space - try your functions here, then run: python lab10.py
    # print(eval_rpn(["2", "1", "+", "3", "*"]))   # 9
    pass


if __name__ == "__main__":
    main()
