class Solution(object):
    def evaluate(self, s, knowledge):
        # Ubah knowledge menjadi dictionary
        d = {key: value for key, value in knowledge}
        
        res = []
        in_bracket = False
        current_key = []
        
        for char in s:
            if char == '(':
                in_bracket = True
            elif char == ')':
                in_bracket = False
                key_str = "".join(current_key)
                res.append(d.get(key_str, '?'))
                current_key = []  # Reset penampung key
            else:
                if in_bracket:
                    current_key.append(char)
                else:
                    res.append(char)
                    
        return "".join(res)
