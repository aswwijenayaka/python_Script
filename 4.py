# Anagrams
"""
def anagrams(s):
    d = {}  # initiating aa dictionary to store signature and corresponding word
    for words in s:
        s = ''.join(sorted(words))  # finding the signature for the word
        if s in d:
            d[s].append(words)  # append the word to existing key
        else:
            # or add a new index
            d[s] = words

    return [d[s] for s in d if len(d[s]) > 1]

"""


class stack:
    def __init__(self):
        self.items = []  # creating a list

    def is_empty(self):
        return self.items == []  # creating a function to check whether the stack is empty

    def push(self, item):
        self.items.insert(0, item)  # pushing an item to the top of the stack

    def pop(self):
        self.items.pop(0)  # popping the item from the top of the stack

    def print_stack(self):
        print(self.items)


def is_balanced(s):
    curl_b = stack()
    sq_b = stack()
    norm_b = stack()
    prev_b = ""
    for items in s:
        if items == "{":
            curl_b.push(items)
            prev_b = items
        elif items == "[":
            sq_b.push(items)
            prev_b = items
        elif items == "(":
            norm_b.push(items)
            prev_b = items

        elif items == "}":
            if curl_b.is_empty():
                return "NO"
            elif prev_b == "(" or prev_b == "[":
                return "NO"
            else:
                curl_b.pop()
                prev_b = items
        elif items == "]":
            if sq_b.is_empty():
                return "NO"
            elif prev_b == "(" or prev_b == "{":
                return "NO"
            else:
                sq_b.pop()
                prev_b = items
        elif items == ")":
            if norm_b.is_empty():
                return "NO"
            elif prev_b == "{" or prev_b == "[":
                return "NO"
            else:
                norm_b.pop()
                prev_b = items

    if (sq_b.is_empty()) and (curl_b.is_empty()) and (norm_b.is_empty()):
        return "YES"

    else:
        return "NO"


s = "{[(])}"
print(is_balanced(s))
