"""
Vacuum cleaner route
  "LR", return true
  "URURD", return false
  "RUULLDRD", return true
"""
def return_to_origin(moves):
    count_lr = 0
    count_ud = 0

    for move in moves:
        if move == 'L':
            count_lr += 1
        elif move == 'R':
            count_lr -= 1
        elif move == 'U':
            count_ud += 1
        elif move == 'D':
            count_ud -= 1

    return count_lr == 0 and count_ud == 0

# Examples
print(return_to_origin("LR"))          
print(return_to_origin("URURD"))       
print(return_to_origin("RUULLDRD"))    

            
    
