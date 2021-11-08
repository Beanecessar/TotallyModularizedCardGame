from Core.MHand import *
from Core.MRuler import *
import random

tilesNoJoker = [
	"1p", "2p", "3p", "4p", "5p", "6p", "7p", "8p", "9p",
	"1s", "2s", "3s", "4s", "5s", "6s", "7s", "8s", "9s",
	"1m", "2m", "3m", "4m", "5m", "6m", "7m", "8m", "9m",
	"1z", "2z", "3z", "4z", "5z", "6z", "7z"
]

ruler = MRuler(MRuleSet())
for i in range(10):
	# 每种牌4张
	walls = tilesNoJoker*4
	# 洗牌
	random.shuffle(walls)
	handStr = " ".join(walls[:14])
	hand = MHand()
	hand.SetupFromBrief(handStr)
	hand.Sort()
	print(hand)

	results = ruler.CheckHand(hand)
	if len(results) > 0:
		print("Can")
	else:
		print("Can't")

hands = [
	"1p 1p 1p 2p 3p 4p 5p 6p 7p 8p 9p 9p 9p",
	"1p 1p 1p 2p 2p 2p 3p 3p 3p 7p 8p 9p 9p",
	"1p 1p 1p 2p 2p 2p 3p 3p 3p 4p 5p 6p 7p",
]
for handStr in hands:
	hand = MHand()
	hand.SetupFromBrief(handStr)
	hand.Sort()
	print(hand)

	solves = ruler.FindSolve(hand)
	if len(solves) > 0:
		print(" ".join(solves))
