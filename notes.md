## GAME RULES:
- elevation 1 to 6
- to move elevation difference must be 2 or less
- cannot move to tile, if there is laser door
- door has one of 3 colors
- key has one of 3 colors and opens all same color doors
- one player
- one goal
- multiple number of doors
- multiple number of keys <-- this is missing
- only one object on a tile

## FITNESS FUNCTIONS:
- feasible:
	- length of level
	
- infeasible:
	- penalty for each violation of rules
  		- elevation > 6
    	- elevation < 1
        - more than 1 thing on tile
        - doors > 3
        - doors < 0
        - keys > 3
        - keys < 0
        - more than 1 player
        - more than 1 exit
	- small penalty if all rules are followed, but level is unsolvable

## PROCEEDINGS:
- 30 generations
- feasible max 200 individuals
- infeasible max 1000 individuals
- results from averaging all feasible levels

## TODO:
- optimize BFS algorithm by probably:
  - find a way to determine if maze is unsolvable to save time
  - decrease number of solving iteration form 10 (based on experiments or research)
- implement FI-2POP instead of current algorithm

