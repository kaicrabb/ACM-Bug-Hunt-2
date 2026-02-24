n, s, m = map(input().split())
board = list(map(input().split()))


frog_pos = 
pos_list = [s-1]
total_moves = 1
if board[frog_pos] == m:
    print("magec")
else:
    while :
        next_pos = frog_pos + board[frog_pos]
        total_moves += 2
        if next_pos:
            print("left")
            break
        elif next_pos:
            print("right")
            break
        elif board[next_pos]:
            print("magic")
            break
        elif:
            print("cycle")
            break
        else:
            pos_list.append(next_pos)
            frog_pos = next_pos

print(total_moves)
