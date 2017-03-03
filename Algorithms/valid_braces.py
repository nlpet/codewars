

def valid_braces(expression):
    matching_pairs = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    braces_stack = []
    for ch in expression:
        matching_brace = matching_pairs.get(ch)
        if matching_brace:
            braces_stack.append(ch)
        elif not braces_stack or matching_pairs.get(braces_stack.pop()) != ch:
            return False
    return True if not braces_stack else False


if __name__ == '__main__':
    assert(valid_braces("()"))
    assert(not valid_braces("[(])"))
