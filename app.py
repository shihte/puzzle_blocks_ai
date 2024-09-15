import turtle

#region 初始化設定
blocks = []

def init():
    global blocks

    #region 建立棋盤
    block_pan = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ]

    #endregion

    #region 田型方塊
    block_99 = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
    ]

    block_44 = [
        [1, 1],
        [1, 1],
    ]

    block_11 = [
        [1],
    ]
    #endregion

    #region I型方塊
    block_I5 = [
        [1],
        [1],
        [1],
        [1],
        [1],
    ]

    block_I4 = [
        [1],
        [1],
        [1],
        [1],
    ]

    block_I3 = [
        [1],
        [1],
        [1],
    ]

    block_I2 = [
        [1],
        [1],
    ]
    #endregion

    #region L型方塊
    block_L = [
        [1, 0],
        [1, 0],
        [1, 1],
    ]

    block_l = [
        [0, 1],
        [0, 1],
        [1, 1],
    ]

    block_Big_L = [
        [1, 0, 0, 0],
        [1, 0, 0, 0],
        [1, 0, 0, 0],
        [1, 1, 1, 1],
    ]

    block_Big_l = [
        [0, 0, 0, 1],
        [0, 0, 0, 1],
        [0, 0, 0, 1],
        [1, 1, 1, 1],
    ]

    block_Big_L2 = [
        [1, 1, 1, 1],
        [1, 0, 0, 0],
        [1, 0, 0, 0],
        [1, 0, 0, 0],
    ]

    block_Big_l2 = [
        [1, 1, 1, 1],
        [0, 0, 0, 1],
        [0, 0, 0, 1],
        [0, 0, 0, 1],
    ]

    block_Mini_L = [
        [1, 0],
        [1, 1],
    ]

    block_Mini_l = [
        [0, 1],
        [1, 1],
    ]

    block_Mini_L2 = [
        [1, 1],
        [1, 0],
    ]

    block_Mini_l2 = [
        [1, 1],
        [0, 1],
    ]
    #endregion

    #region T型方塊
    block_T = [
        [1, 1, 1],
        [0, 1, 0],
    ]

    block_t = [
        [0, 1, 0],
        [1, 1, 1],
    ]

    block_T2 = [
        [0, 1],
        [1, 1],
        [0, 1],
    ]

    block_t2 = [
        [1, 0],
        [1, 1],
        [1, 0],
    ]
    #endregion

    #region H型方塊
    block_H2 = [
        [1, 1],
    ]

    block_H3 = [
        [1, 1, 1],
    ]

    block_H4 = [
        [1, 1, 1, 1],
    ]

    block_H5 = [
        [1, 1, 1, 1, 1],
    ]
    #endregion

    #region 將所有積木放入 blocks 字典
    blocks = {
        "block_99": block_99,
        "block_44": block_44,
        "block_11": block_11,
        "block_I5": block_I5,
        "block_I4": block_I4,
        "block_I3": block_I3,
        "block_I2": block_I2,
        "block_L": block_L,
        "block_l": block_l,
        "block_Big_L": block_Big_L,
        "block_Big_l": block_Big_l,
        "block_Big_L2": block_Big_L2,
        "block_Big_l2": block_Big_l2,
        "block_Mini_L": block_Mini_L,
        "block_Mini_l": block_Mini_l,
        "block_Mini_L2": block_Mini_L2,
        "block_Mini_l2": block_Mini_l2,
        "block_T": block_T,
        "block_t": block_t,
        "block_T2": block_T2,
        "block_t2": block_t2,
        "block_H2": block_H2,
        "block_H3": block_H3,
        "block_H4": block_H4,
        "block_H5": block_H5,
    }
    #endregion

#endregion

#region 即時繪製
import turtle

def draw_pan(pan, cell_size=40, margin=20):
    width, height = len(pan[0]), len(pan)
    screen_width = width * cell_size + 2 * margin
    screen_height = height * cell_size + 2 * margin

    screen = turtle.Screen()
    screen.setup(screen_width, screen_height)
    screen.title("俄羅斯方塊遊戲板")
    screen.bgcolor("white")
    screen.tracer(0)  # 關閉動畫以提高效率

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.pensize(2)  # 設置較粗的線寬，用於繪製外框

    # 計算起始位置，使繪圖區域居中
    start_x = -width * cell_size / 2
    start_y = height * cell_size / 2

    # 繪製黑色外框
    t.penup()
    t.goto(start_x, start_y)
    t.pendown()
    t.color("black")
    for _ in range(4):
        t.forward(width * cell_size)
        t.right(90)

    # 繪製內部方格
    t.pensize(1)  # 恢復較細的線寬，用於繪製內部格子
    for i, row in enumerate(pan):
        for j, cell in enumerate(row):
            x = start_x + j * cell_size
            y = start_y - i * cell_size - cell_size  # 調整 y 座標以從上到下繪製
            t.penup()
            t.goto(x, y)
            if cell == 1:
                t.fillcolor("black")
                t.begin_fill()
            t.pendown()
            for _ in range(4):
                t.forward(cell_size)
                t.left(90)
            if cell == 1:
                t.end_fill()

    screen.update()
    screen.exitonclick()
#endregion

#region 自定義棋盤函式
def set_pan():
    # 提示用戶輸入棋盤狀態
    board_input = input("請輸入棋盤狀態 (一段由0和1組成，必須是64個數字)：")

    # 確保輸入的長度是64
    if len(board_input) != 64 or not all(c in '01' for c in board_input):
        print("輸入無效！請確保輸入的是64個0和1。")
        return
    
    # 將輸入分成8行，每行8列
    pan = []
    for i in range(8):
        row = board_input[i*8:(i+1)*8]
        pan.append([int(char) for char in row])

    # 輸出棋盤
    print("\n棋盤狀態：")
    for row in pan:
        print(' '.join(map(str, row)))
        
    return pan
#endregion

#region 尋找並判斷積木放置位置以及評分
def check_and_evaluate_placement (blocks,pan) :

    pan_cope = pan
    
    try_block_name = "block_I5"
    block = blocks[try_block_name] #TODO 暫時將取用積木定義，稍後改成用inuput
    if try_block_name not in blocks :
        print("該積木不存在")
    
    draw_pan(pan_cope)
    
    # 尋找所有可能的放置位置
    possible_placements = []
    for y in range(len(pan_cope) - len(block) + 1):
        for x in range(len(pan_cope[0]) - len(block[0]) + 1):
            if can_place_block(pan_cope, block, x, y):
                possible_placements.append((x, y))

    if not possible_placements:
        print("沒有可用的放置位置")
        draw_pan(pan_cope)
        return
#endregion

#region 判定放置

def can_place_block(pan, block, x, y):
    for i in range(len(block)):
        for j in range(len(block[0])):
            if block[i][j] == 1:
                if (y + i >= len(pan) or x + j >= len(pan[0]) or 
                    pan[y + i][x + j] == 1):
                    return False
    return True

#endregion

# 初始化設定
init()

# 使用函式來設置棋盤
pan = set_pan()

check_and_evaluate_placement(blocks,pan)