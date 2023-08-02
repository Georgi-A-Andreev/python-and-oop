def complex_resolver(expression):
    def evaluate(sub_expr):
        if '?' not in sub_expr:
            return sub_expr.strip()

        condition_idx = sub_expr.find('?')
        condition = sub_expr[:condition_idx].strip()
        remaining_expr = sub_expr[condition_idx + 1:].strip()

        if condition == 't':
            true_expr, false_expr = split_expression(remaining_expr)
            return evaluate(true_expr)
        elif condition == 'f':
            true_expr, false_expr = split_expression(remaining_expr)
            return evaluate(false_expr)

    def split_expression(expr):
        colon_idx = expr.rfind(':')
        true_expr = expr[:colon_idx].strip()
        false_expr = expr[colon_idx + 1:].strip()
        return true_expr, false_expr

    return evaluate(expression)


input_expression1 = input()

print(complex_resolver(input_expression1))



