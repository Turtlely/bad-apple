def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[39m".format(r, g, b, text)

import time

text = "Hello, World"
start = time.time()
colored_text = colored(132, 204, 247, text)
print("Time Taken: ", time.time()-start)
print(colored_text)