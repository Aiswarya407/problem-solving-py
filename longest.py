def length_of_longest_substring(s: str) -> int:
    """
    Return length of the longest substring without repeating characters.
    Sliding window with dictionary storing last index of each char.
    """
    last_index = {}   # char -> last index seen
    l = 0             # left boundary of window (inclusive)
    max_len = 0

    for r, ch in enumerate(s):
        if ch in last_index and last_index[ch] >= l:
            # ch repeats inside current window, move left boundary
            l = last_index[ch] + 1
        # update last seen index for ch
        last_index[ch] = r
        # current window length is r - l + 1
        cur_len = r - l + 1
        if cur_len > max_len:
            max_len = cur_len

    return max_len


# quick tests
if __name__ == "__main__":
    tests = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        (" ", 1),
        ("au", 2),
        ("abba", 2),  # tricky: "ab" or "ba"
    ]

    for s, expected in tests:
        res = length_of_longest_substring(s)
        print(f"Input: {s!r:10}  -> Output: {res:2}  Expected: {expected:2}  {'OK' if res == expected else 'WRONG'}")
