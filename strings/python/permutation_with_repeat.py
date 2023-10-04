# References:
# https://code.luasoftware.com/tutorials/coding-interview/permutations-with-repeating-characters
# https://www.superprof.co.uk/resources/academic/maths/probability/combinatorics/permutations-with-repetition.html#chapter_permutations-with-repetition

combination: list[str] = []


def _permutation_repeat(text, prefix, n, k):
    if k == 0:  # base, len(prefix) == len(text)
        combination.append(prefix)
        return
    for i in range(n):
        new_prefix = prefix + text[i]  # a, aa, aaa, aab, aac ab, aba, abb, abc

        # print(new_prefix)
        _permutation_repeat(text, new_prefix, n, k - 1)
    # print('---')


def permutation_repeat(text, k):
    _permutation_repeat(text, "", len(text), k)


permutation_repeat("10", 4)

SET = ["IE", "NS", "TF", "PJ"]

for i in range(0, len(combination)):
    for s in range(0, len(combination[i])):
        print(SET[s][int(combination[i][s])], end="")
    print(" ")
