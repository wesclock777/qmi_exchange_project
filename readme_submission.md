# Build your own Exchange Coding Test Submission


# Submission Structure

system.py - contains code for running the actual exchange,
  includes:
    Exchange class
    Order class

trading.py - handles the endpoints for the exchange

app.py - brings it all together, falcon routes are added here

test.json - is a json file that was used to do POST requests to
  the server using curl.

The answers to the questions are in the old readme.md

# Assumptions

- The exchange operates on a first in first out basis
(Older listings and prioritized over later listings because
No prices are listed)

- Orders can be split, for example: a buy order for 100 shares with a sell order for 50 shares on the market will be filled for 50 shares when submitted and a new buy order of the 50 remaining shares will be listed.
