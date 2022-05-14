def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述
  
    left = 0
    right = len(sorted_array)
    
    while left <= right:
        # 中間index
        mid = right + (left - right) // 2

        # target が mid にあれば，mid を返す
        if sorted_array[mid] == target_number:
            return mid

        # target より小さい場合 left を更新
        elif sorted_array[mid] < target_number:
            left = mid + 1

        # そうでない場合 right を更新
        else:
            right = mid - 1

    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()