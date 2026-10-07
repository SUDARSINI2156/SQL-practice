class Solution:
    def removeInvalidParentheses(self, s):
        def isValid(x):
            count = 0

            for ch in x:
                if ch == '(':
                    count += 1

                elif ch == ')':
                    count -= 1

                    if count < 0:
                        return False

            return count == 0

        current = {s}

        while True:
            answer = []

            # Check current strings
            for x in current:
                if isValid(x):
                    answer.append(x)

            # If valid strings found,
            # this is the minimum number of removals
            if answer:
                return answer

            next_level = set()

            # Remove one parenthesis
            for x in current:
                for i in range(len(x)):
                    if x[i] == '(' or x[i] == ')':
                        new_string = x[:i] + x[i + 1:]
                        next_level.add(new_string)

            current = next_level