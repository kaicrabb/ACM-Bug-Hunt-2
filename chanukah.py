input_num = input.nextInt()

for i in range(iterations){
    y, x = input().split("-")
    candles = ((int(y)+3)*int(y)/2)
    print(x + " " + int(candles))
}
