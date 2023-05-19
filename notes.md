## GAME RULES:
- elevation 1 to 6
- to move elevation difference must be 2 or less
- cannot move to tile, if there is laser door
- door has one of 3 colors
- key has one of 3 colors and opens all same color doors
- one player
- one goal
- multiple number of doors
- multiple number of keys
- only one object on a tile

## FITNESS FUNCTIONS:
- feasible:
	- length of level
	
- infeasible:
	- penalty for each violation of rules
	- small penalty if all rules are followed, but level is unsolvable

## PROCEEDINGS:
- 30 generations
- feasible max 200 individuals
- infeasible max 1000 individuals
- restults from averaging all feasible levels