from backend import percent_change as pc
from args import make_args

highestPosMovingStocks = pc.percent_change().get_highest_positive_movers()
print(highestPosMovingStocks)