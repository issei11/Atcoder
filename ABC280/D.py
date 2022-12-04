def prime_factorize(N):
    # 答えを表す可変長配列
    res = []

    # √N まで試し割っていく
    for p in range(2, N):
        # p * p <= N の範囲でよい
        if p * p > N:
            break

        # N が p で割り切れないならばスキップ
        if N % p != 0:
            continue

        # N の素因数 p に対する指数を求める
        e = 0
        while N % p == 0:
            # 指数を 1 増やす
            e += 1

            # N を p で割る
            N //= p

        # 答えに追加
        res.append((p, e))

    # 素数が最後に残ることがありうる
    if N != 1:
        res.append((N, 1))

    return res

#二分探索を用いて、seqの中からkey以上の要素で最小のものを返す関数
def binary_search(K):
    pf = prime_factorize(K)
    left = 2
    right = K
    while left < right-1:
        pivot = (left+right)//2
        flag = 0
        for i in range(len(pf)):
            p = pf[i][0]
            cnt = 0
            while p <= pivot:
                cnt += pivot//p
                p *= pf[i][0]
            if cnt >= pf[i][1]:
                flag += 1
        if flag == len(pf):
            right = pivot
        else:
            left = pivot
    return right

K = int(input())

print(binary_search(K))

