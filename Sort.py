def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    #print(r, l)
    [print(i) for i in sortedArray]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]

    # ここから記述

    # 先頭位置と末端位置
    l = 0
    r = len(array) - 1

    while True:
        # 先頭から探索
        while l <= r and array[l] < pivot:
            l += 1
        
        # 末端から探索
        while l <= r and array[r] >= pivot:
            r -= 1

        # ぶつかったら探索終了
        if l > r: 
            break

        # 見つかったら交換
        array[l], array[r] = array[r], array[l]
    
    # 先頭要素が最小値の例外処理
    p = l + 1 if (l == 0) else l

    # 空配列でなければ再帰的にソート
    if len(array[:p]): left_array = sort(array[:p])
    if len(array[p:]): right_array = sort(array[p:])

    # ソート済み配列を統合し返す
    return left_array + right_array 

    # ここまで記述

if __name__ == '__main__':
    main()