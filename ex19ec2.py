def nba_finals(heat_win, pacers_win):
	print "if the %s, they'll play the spurs!" % heat_win
	print "if the %s, they'll play the spurs!" % pacers_win
	print "either way, they're going down. \n"
	
print "I can't wait til June 6th"
nba_finals("heat win", "pacers win")

print "using variables to run the same function, i'll assign the same string"
heat_win = "heat win"
pacers_win = "pacers win"

nba_finals(heat_win, pacers_win)

print "i also got a little math with strings to run the same function."

nba_finals("heat" + " win", "pacers " + "win")

print "can we do math, variables, and strings?"
nba_finals(heat_win + " (booooooooooo)", pacers_win + " (booooooooooo)"