from simpleeval import simple_eval
def calculator(expression):
    try:
        
        result=simple_eval(expression)
        return result

    except Exception as e:
        return f"An unexpected error occured: {e}"

print(calculator("18 * 4500"))
print(calculator("18 % of 4500"))


    