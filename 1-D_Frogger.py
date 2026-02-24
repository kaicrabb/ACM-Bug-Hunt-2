n, s, m = map(input().split())
board = list(map(input().split()))


frog_pos = 
pos_list = [s-1]
total_moves = 0
if board[frog_pos] == m:
    print("magic")
else:
    while :
        next_pos = frog_pos + board[frog_pos]
        total_moves += 1
        if next_pos < 0:
            print("left")
            break
        elif next_pos >= n:
            print("right")
            break
        elif board[next_pos] == m:
            print("magic")
            break
        elif next_pos in pos_list:
            print("cycle")
            break
        else:
            pos_list.append(next_pos)
            frog_pos = next_pos

print(total_moves)
