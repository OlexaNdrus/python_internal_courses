from typing import List
from collections import defaultdict

def removeDuplicates(nums: List[int]) -> int:
    for ind, num in enumerate(nums):
        while num in nums[ind+1:]:
            nums.remove(num)
    return len(nums)


def singleNumber(nums: List[int]) -> int:
    for i in nums:
        if nums.count(i) == 1:
            return i


def rotate(nums: List[int], k: int) -> None:
    #nums = nums[-k:-1:1] + nums[0:len(nums)-k]

    for i in range(k):
        nums.insert(0, nums[-1])
        del nums[-1]


def twoSum(nums: List[int], target: int):
    '''Weak solution'''
    # for ind, el in enumerate(nums):
    #     try:
    #         ind2 = nums[ind + 1:].index(target - el)
    #         return ind, ind2 + ind + 1
    #     except ValueError as e:
    #         pass

    '''Strong solution'''
    dicty = {}
    for ind, el in enumerate(nums):
        el = nums[ind]
        try:
            return dicty[target - el], ind
        except:
            dicty[el] = ind

def plusOne(digits: List[int]) -> List[int]:

    ind = len(digits) - 1
    while digits[ind] == 9:
        digits[ind] = 0
        ind -= 1

    if ind == -1:
        digits.insert(0, 1)
    else:
        digits[ind] = digits[ind] + 1
    return

def moveZeroes(nums: List[int]) -> None:
    count = 0
    for i in range(len(nums)):
        el = nums[i]
        if el != 0:
            nums[count], nums[i] = el, nums[count]
            count += 1

def containsDuplicate(nums: List[int]) -> bool:
    if len(nums) - len(set(nums))>0:
        return True

def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    hash, return_arr = defaultdict(lambda: 0), []
    if len(nums1) < len(nums2):
        nums1, nums2 = nums2, nums1

    for num in nums1:
        hash[num] += 1

    for num in nums2:
        if num in hash and hash[num]>0:
            hash[num] -= 1
            return_arr.append(num)

    return return_arr

def rotate_matrix(matrix: List[List[int]]) -> None:
    pos, dim_len = 0, len(matrix)
    for row_ind in range(int((dim_len) / 2)):
        for ind in range(pos, dim_len - pos - 1):
            matrix[row_ind][ind], matrix[ind][-(pos + 1)], matrix[-(pos + 1)][-(ind + 1)], matrix[-(ind + 1)][pos] = \
                matrix[-(ind + 1)][pos], matrix[row_ind][ind], matrix[ind][-(pos + 1)], matrix[-(pos + 1)][-(ind + 1)]
        pos += 1

def maxProfit(prices: List[int]) -> int:
    ''''Own Sollution'''
    # sum = 0
    # lazy_pointer, fast_pointer = 0, 1
    # while lazy_pointer != len(prices) - 1:
    #
    #     buy = True
    #     for fast_pointer in range(lazy_pointer+1, len(prices)):
    #         if prices[fast_pointer] < prices[fast_pointer-1]:
    #             if fast_pointer - 1 == lazy_pointer:
    #                 buy = False
    #             else:
    #                 fast_pointer -= 1
    #             break
    #
    #     if buy:
    #         sum += prices[fast_pointer] - prices[lazy_pointer]
    #     lazy_pointer, fast_pointer = fast_pointer, fast_pointer + 1
    #
    # return sum

    ''''Easiest One'''
    sum = 0
    for ind in range(1, len(prices) - 1):
        diff = prices[ind] - prices[ind - 1]
        if diff > 0:
            sum += diff

    return sum


def reverse_num(x: int) -> int:
    result, multip, sign = 0, 1, 1

    if x >= 0:
        stringy = str(x)
    else:
        stringy = str(x)[1:]
        sign = -1


    for num in stringy:
        result += int(num) * multip
        multip *= 10
        if result.bit_length() > 31:
            return 0

    return result * sign

def firstUniqChar(s: str) -> int:
    maximum_val, hash = len(s) + 1, {}
    for ind, el in enumerate(s):
        if el in hash:
            hash[el] = maximum_val
        else:
            hash[el] = ind
    uniques = hash.values()

    if uniques and min(uniques) != maximum_val:
        return min(uniques)
    return -1

    ''''Best solution'''
    # def firstUniqChar(s: str) -> int:
    #     hash = defaultdict(int)
    #     for el in s:
    #         hash[el] += 1
    #
    #     for ind, el in enumerate(s):
    #         if hash[el] == 1:
    #             return ind
    #
    #     return -1

def reverseString(s: List[str]) -> None:
    for ind in range(int(len(s)/2)):
        s[ind], s[-(ind+1)] = s[-(ind+1)], s[ind]


def myAtoi(str: str) -> int:
    stringy, res = str.strip(), 0

    def int_gether(string):
        res = 0
        for num in string:
            if num.isnumeric():
                res = res * 10 + int(num)
            else:
                return res
        return res

    if len(stringy) > 0:

        first_el = stringy[0]

        if first_el.isnumeric():
            res = int_gether(stringy)


        elif first_el == "-":
            res = int_gether(stringy[1:]) * (-1)


        elif first_el == "+":
            res = int_gether(stringy[1:])


        else:
            return 0

        top, bot = 2147483647, -2147483648
        if res > top:
            res = top
        if res < bot:
            res = bot

    if res > pow(2, 31):
        res = pow(2, 31)

    return res

def isAnagram(s: str, t: str) -> bool:
    hash = defaultdict(int)
    for i in t:
        hash[i] += 1

    for j in s:
        if j in hash:
            hash[j] -= 1
        else:
            return False

    if all(value == 0 for value in hash.values()):
        return True

    return False

def strStr(haystack: str, needle: str) -> int:
    if haystack == needle:
        return 0

    for ind in range(0, len(haystack) - len(needle) + 1):
        if all(True if sym == haystack[ind + ind_s] else False for ind_s, sym in enumerate(needle)):
            return ind
    return -1

def longestCommonPrefix(strs: List[str]) -> str:
    common_pref = []
    if strs:

        word = strs[0]
        for string in strs:
            if len(string) < len(word):
                word = string

        for ind in range(len(word)):
            if all(True if string[ind] == word[ind] else False for string in strs):
                common_pref.append(word[ind])
            else:
                break

    return ''.join(common_pref)

def countAndSay(n: int) -> str:
    '''''0<n<30'''''
    def iterationCount(string):
        count_sim, num = 0, string[0]
        result_arr = []
        for sym in string:

            if num == sym:
                count_sim += 1
            else:
                result_arr.append(str(count_sim))
                result_arr.append(num)
                num, count_sim = sym, 1

        result_arr.append(str(count_sim))
        result_arr.append(num)
        return ''.join(result_arr)

    starting_str = '1'
    for iteration in range(1, n):
        starting_str = iterationCount(starting_str)
    return starting_str


nums= [1,2,3,4,5,6]


print(countAndSay(30))
