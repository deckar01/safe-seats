# Safe Seats

Simulate theater seating capacity with the COVID-19 pandemic distancing requirements.

## Usage

`./compare.py` run trials to compare the average capacity with and without blocking alternating rows.

`./preview_row_block.py` a terminal rendering of a random theater simulation with blocking alternating rows.

`./preview_free_block.py` a terminal rendering of a random theater simulation without blocking rows.

## Visualization key

- Blue cells are reserved. The letter indicates which group it belongs to.
- Red cells are removed to enforce distancing after each reservation. The letter indicates the group that made the reservation.
- Grey cells are blocked by the theater.
- The white bar at the top represents the screen.

## Assumptions

The layout and blocked rows were sampled from a screen at my local theater. The seat and isle sizes
were estimated based on my own experiences.

The number of people in a group (seated without distancing) is assumed to have a log-normal distributed that
peaks just below 2 and falls off slowly around 5.

The ideal theater seat is assumed to be centered horizontally and the distance from the screen is assumed to be
a random preference with a normal distrobution centered around the middle row.

The logic for choosing the first seat is to pick the closest available seat to a randomly selected ideal seat.

The logic for choosing additional seats for a group favors the same row by squaring the Y distance twice
when minimizing the euclidean distance to the first seat.

All of these models can be tweaked at the top of `theater.py`.

## Legal

This is not medical advice.
