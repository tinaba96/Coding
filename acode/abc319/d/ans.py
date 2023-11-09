n, m = map(int, input().split())
li = list(map(lambda x: x + 1, map(int, input().split())))

m_start = max(li) - 1
m_end = sum(li) - 1

ans_width = m_end

while m_start <= m_end:
    # current max length for a line.
    mid = (m_start + m_end) // 2

    cur_length = 0
    cur_row = 1
    for i in li:
        cur_length += i
        if cur_length - 1 > mid:
            cur_length = i
            cur_row += 1

    if cur_row <= m:
        ans_width = mid
        m_end = mid - 1
    else:
        m_start = mid + 1

print(ans_width)

