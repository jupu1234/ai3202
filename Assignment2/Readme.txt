To choose a maze the command line prompt you to enter World1 or World2 to read in a maze
The second command prompt is to choose a heuristic to choose the manhatten heuristic enter 1 to choose the choosen heuristic enter a 2
There is no defined default if you enter any other value

My choosen heuristic is a best first search but the heuristic value is scaled to the area of the remaining maze from the current node.

The equation I used:

(smallest initial travel distance)*(abs(Xend - Xcurr)*abs(Yend - Ycurr))

It searches the adjecent nodes of an adjecent node to the current node to find the the adjacent nodes heuristic value.
The reason I choose this is that I thought if you choose the best initial choice each time that it would produce a reasonable result, probably not the best route though. Scaling the initial travel distance by the remaining board shows that you are getting closer to your end goal and not farther away.

The performance of my heuristic:
World 1:
Manhatten distance heuristic visited 12 places to reach the goal with a total cost of 156
My heuristic visited 11 places to reach the goal with a total cost of 130

World 2:
Manhatten distance heuristic visited 13 places to reach the goal with a toal cost of 142
My heuristic visited 11 places to reach the goal with a total cost of 150

In world 1 it outperformed the Manhatten distance but in World 2 it had a higher cost to reach the end but visited fewer places.

Though a big pitfall of my heuristic is that the first adjacent node you look at could change the path that is taken. Depending on the direction you look first it could change the results from the ones that I got.
