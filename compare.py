#!python3

import theater


trials = 200

if __name__ == '__main__':
    row_block_capacity = 0
    for _ in range(trials):
        results = theater.simulate()
        row_block_capacity += theater.capacity(*results)
    row_block_capacity /= trials
    print('row_block_capacity =', '{:.2f}%'.format(100*row_block_capacity))

    theater.blocked_rows = []
    free_block_capacity = 0
    for _ in range(trials):
        results = theater.simulate()
        free_block_capacity += theater.capacity(*results)
    free_block_capacity /= trials
    # print(preview(*results))
    print('free_block_capacity =', '{:.2f}%'.format(100*free_block_capacity))
