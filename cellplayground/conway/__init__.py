from .playground import ConwayPlayground
from .cell import ConwayCell

def run_playground(width, height, num_starting_cells, num_steps):
    playground = ConwayPlayground(width, height)
    # playground.init_cells(num_starting_cells)
    playground.init_fun_stuff()
    print(playground)

    for i in range(num_steps):
        playground.play()
        print(playground)