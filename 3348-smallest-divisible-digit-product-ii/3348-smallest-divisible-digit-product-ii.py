class Solution:

    def smallestNumber(self, num: str, t: int) -> str:
        # Step 1: Decompose t into prime factors 2, 3, 5, 7
        temp = t
        a = b = c = d = 0

        while temp % 2 == 0:
            a += 1
            temp //= 2
        while temp % 3 == 0:
            b += 1
            temp //= 3
        while temp % 5 == 0:
            c += 1
            temp //= 5
        while temp % 7 == 0:
            d += 1
            temp //= 7

        # If t has prime factors > 7, no zero-free number can satisfy the condition
        if temp > 1:
            return "-1"

        # Prime factors provided by digits 0..9 (twos, threes, fives, sevens)
        digit_factors = [
            (0, 0, 0, 0),  # 0
            (0, 0, 0, 0),  # 1
            (1, 0, 0, 0),  # 2
            (0, 1, 0, 0),  # 3
            (2, 0, 0, 0),  # 4
            (0, 0, 1, 0),  # 5
            (1, 1, 0, 0),  # 6
            (0, 0, 0, 1),  # 7
            (3, 0, 0, 0),  # 8
            (0, 2, 0, 0),  # 9
        ]

        # DP Table: dp[i][j] = min digits needed for at least i twos and j threes
        dp = [[float("inf")] * 65 for _ in range(65)]
        dp[0][0] = 0

        for i in range(65):
            for j in range(65):
                if i == 0 and j == 0:
                    continue
                res = float("inf")
                res = min(res, 1 + dp[max(0, i - 3)][j])  # digit 8
                res = min(res, 1 + dp[i][max(0, j - 2)])  # digit 9
                res = min(res, 1 + dp[max(0, i - 1)][max(0, j - 1)])  # digit 6
                res = min(res, 1 + dp[max(0, i - 2)][j])  # digit 4
                res = min(res, 1 + dp[i][max(0, j - 1)])  # digit 3
                res = min(res, 1 + dp[max(0, i - 1)][j])  # digit 2
                dp[i][j] = res

        def min_digits(req_a, req_b, req_c, req_d):
            """Returns min digits required to satisfy remaining factor counts."""
            req_a = max(0, req_a)
            req_b = max(0, req_b)
            req_c = max(0, req_c)
            req_d = max(0, req_d)
            return req_c + req_d + dp[req_a][req_b]

        N = len(num)

        # Precompute prefix factor counts for num
        pref_a = [0] * (N + 1)
        pref_b = [0] * (N + 1)
        pref_c = [0] * (N + 1)
        pref_d = [0] * (N + 1)

        for k in range(N):
            dig = int(num[k])
            fa, fb, fc, fd = digit_factors[dig]
            pref_a[k + 1] = pref_a[k] + fa
            pref_b[k + 1] = pref_b[k] + fb
            pref_c[k + 1] = pref_c[k] + fc
            pref_d[k + 1] = pref_d[k] + fd

        z = num.find("0")
        if z == -1:
            z = N

        # Step 2: Check if num itself is valid
        if z == N:
            if (
                pref_a[N] >= a
                and pref_b[N] >= b
                and pref_c[N] >= c
                and pref_d[N] >= d
            ):
                return num

        # Step 3: Try to keep a prefix of length i, change digit at i, and fill suffix
        max_prefix_len = min(N - 1, z)

        for i in range(max_prefix_len, -1, -1):
            req_a = a - pref_a[i]
            req_b = b - pref_b[i]
            req_c = c - pref_c[i]
            req_d = d - pref_d[i]

            min_d = int(num[i]) + 1
            for digit in range(min_d, 10):
                fa, fb, fc, fd = digit_factors[digit]
                rem_a = req_a - fa
                rem_b = req_b - fb
                rem_c = req_c - fc
                rem_d = req_d - fd

                rem_len = N - 1 - i
                if min_digits(rem_a, rem_b, rem_c, rem_d) <= rem_len:
                    # Construct the lexicographically smallest suffix of length rem_len
                    res = list(num[:i]) + [str(digit)]
                    curr_a, curr_b, curr_c, curr_d = rem_a, rem_b, rem_c, rem_d

                    for p in range(rem_len):
                        rem_p_len = rem_len - 1 - p
                        for x in range(1, 10):
                            x_fa, x_fb, x_fc, x_fd = digit_factors[x]
                            if (
                                min_digits(
                                    curr_a - x_fa,
                                    curr_b - x_fb,
                                    curr_c - x_fc,
                                    curr_d - x_fd,
                                )
                                <= rem_p_len
                            ):
                                res.append(str(x))
                                curr_a -= x_fa
                                curr_b -= x_fb
                                curr_c -= x_fc
                                curr_d -= x_fd
                                break
                    return "".join(res)

        # Step 4: If no solution of length N exists, construct solution of target length L > N
        M = min_digits(a, b, c, d)
        L = max(N + 1, M)

        res = []
        curr_a, curr_b, curr_c, curr_d = a, b, c, d

        for p in range(L):
            rem_p_len = L - 1 - p
            for x in range(1, 10):
                x_fa, x_fb, x_fc, x_fd = digit_factors[x]
                if (
                    min_digits(
                        curr_a - x_fa,
                        curr_b - x_fb,
                        curr_c - x_fc,
                        curr_d - x_fd,
                    )
                    <= rem_p_len
                ):
                    res.append(str(x))
                    curr_a -= x_fa
                    curr_b -= x_fb
                    curr_c -= x_fc
                    curr_d -= x_fd
                    break

        return "".join(res)