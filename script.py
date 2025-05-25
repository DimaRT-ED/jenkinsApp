import fire
def print_hello(name="World"):
    return "Hello %s !" %name

if __name__ == '__main':
    fire.Fire(print_hello)
