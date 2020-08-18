#!python3

import theater


if __name__ == '__main__':
    theater.blocked_rows = []
    results = theater.simulate()
    free_block_capacity = theater.capacity(*results)
    print(theater.preview(*results))
    print()
    print('row_block_capacity =', '{:.2f}%'.format(100*free_block_capacity))
    print()
