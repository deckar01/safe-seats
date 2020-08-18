import random


theater_size = (30, 17) # seats
seat_spacing = (30, 36) # inches
distancing = 72 # inches
rows = [
    (0, 1, 29),
    (1, 4, 24),

    (3, 4, 23),
    (4, 4, 23),
    (5, 4, 23),
    (6, 4, 23),

    (8, 0, 30),
    (9, 0, 30),
    (10, 0, 30),
    (11, 0, 30),
    (12, 0, 30),
    (13, 0, 30),
    (14, 0, 30),
    (15, 0, 28),
    (16, 0, 27),
]

blocked_rows = [0, 4, 6, 9, 11, 13, 15]

minimum_group_size = 1

def random_group_size():
    return max(minimum_group_size, int(random.lognormvariate(0.8, 0.5)))

def random_screen_distance():
    return random.normalvariate(0.5, 0.125)

###############################################################################

def random_good_seat():
    return (
        seat_spacing[0]*(theater_size[0]/2 - 0.5),
        seat_spacing[1]*(theater_size[1]*random_screen_distance() - 0.5),
    )

def distance(A, B):
    w = A[0] - B[0]
    h = A[1] - B[1]
    return (w * w + h * h) ** 0.5

def friend_distance(A, B):
    w = A[0] - B[0]
    h = A[1] - B[1]
    return (w * w + h ** 4) ** 0.5

def quality(seat, favorite_seat):
    worst_quality = distance((0, 0), favorite_seat)
    d = distance(seat, favorite_seat)
    return 1 - d / worst_quality

def preview(reserved, removed, blocked):
    ID = 'ABCDEFGHIJLMNPQRSTUVWXYZabcdefghijmnpqrstuvwxyz0123456789' + '$' * 999
    preview = [['   ' for _ in range(theater_size[0])] for _ in range(theater_size[1])]
    for i, seats in enumerate(reserved):
        for seat in seats:
            preview[seat[3]][seat[2]] = '\u001b[44m ' + ID[i] + ' \u001b[0m'
    for i, seats in enumerate(removed):
        for seat in seats:
            preview[seat[3]][seat[2]] = '\u001b[41m ' + ID[i] + ' \u001b[0m'
    for seat in blocked:
        preview[seat[3]][seat[2]] = '\u001b[48;5;237m   \u001b[0m'
    screen = '\n\u001b[47m' + (' ' * (4*theater_size[0] - 1)) + '\u001b[0m\n\n\n'
    return screen + '\n\n'.join(' '.join(row) for row in preview)

def capacity(reserved, removed, blocked):
    r = 0
    t = 0
    for i, seats in enumerate(reserved):
        for seat in seats:
            r += 1
            t += 1
    for i, seats in enumerate(removed):
        for seat in seats:
            t += 1
    t += len(blocked)
    return r/t

def simulate():
    seats = [
        (seat_spacing[0] * x, seat_spacing[1] * y, x, y)
        for y, o, w in rows
        for x in range(o, w + o)
    ]

    reserved = []
    removed = []
    blocked = [seat for seat in seats if seat[3] in blocked_rows]
    seats = [seat for seat in seats if seat[3] not in blocked_rows]

    while len(seats) >= minimum_group_size:
        count = random_group_size()
        if count > len(seats):
            continue
        favorite_seat = random_good_seat()
        seats.sort(key=lambda s: quality(s, favorite_seat))
        primary = seats.pop()
        closest = sorted(seats, key=lambda s: -friend_distance(primary, s))
        guests = [closest.pop() for _ in range(count - 1)]
        for seat in guests:
            seats.remove(seat)
        selection = [primary] + guests
        reserved.append(selection)
        removed.append([s for s in seats if min(distance(seat, s) for seat in selection) < distancing])
        seats = [s for s in seats if min(distance(seat, s) for seat in selection) >= distancing]
    removed.append(seats)
    return reserved, removed, blocked
