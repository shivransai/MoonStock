from backend import absolute_percent_change as apc

highestMovingStocks = apc.absolute_percent_change().get_highest_movers()
print(highestMovingStocks)