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

    #region 將所有積木放入 blocks 列表
    blocks = [
        block_99,
        block_44,
        block_11,
        block_I5,
        block_I4,
        block_I3,
        block_I2,
        block_L,
        block_l,
        block_Big_L,
        block_Big_l,
        block_Big_L2,
        block_Big_l2,
        block_Mini_L,
        block_Mini_l,
        block_Mini_L2,
        block_Mini_l2,
        block_T,
        block_t,
        block_T2,
        block_t2,
        block_H2,
        block_H3,
        block_H4,
        block_H5,
    ]
    #endregion
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

#region 判斷積木放置位置以及分數
def can_place (blocks,pan) :
    pan_cope = pan
    

# 初始化設定
init()

# 使用函式來設置棋盤
pan = set_pan()

can_place(blocks,pan)