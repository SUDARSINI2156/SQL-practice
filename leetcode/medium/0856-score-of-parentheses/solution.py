class Solution:
    def scoreOfParentheses(self, s):
        score = 0
        depth = 0

        for i in range(len(s)):
            if s[i] == '(':
                depth += 1
            else:
                depth -= 1

                if s[i - 1] == '(':
                    score += 2 ** depth

        return score

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna