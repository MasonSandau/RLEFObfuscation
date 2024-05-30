import random

#Execution functions

def block1():
    print("Executing Block 1")

def block2():
    print("Executing Block 2")

def block3():
    print("Executing Block 3")


# List of functions
blocks = [block1, block2, block3]

#index and random exec list.
def execute_blocks():
    next_block_index = 0
    while blocks:
        i = random.randint(0, len(blocks) - 1)
        if i == next_block_index:
            blocks[i]()
            blocks.pop(i)
            next_block_index = min(next_block_index, len(blocks) - 1)

if __name__ == "__main__":
    execute_blocks()
