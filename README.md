## Leetcode Algorithms Practice



| # | Difficulty | Title |  Example (in/outputs)  |  Solution  |  Plot  |
|---| ---------- | ----- | ---------------------- | ---------- | ------ |
|1|Easy|[Two Sum](https://leetcode.com/problems/two-sum/) | Input: nums = [2,7,11,15], target = 9; Output: [0,1] <br> Because nums[0] + nums[1] == 9, we return [0, 1].| [Python (Hashmap)](two_sum_hash.py)||
|2|Medium|[Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) | Input: l1 = [2,4,3], l2 = [5,6,4]; Output: [7,0,8]; <br> Explanation: 342 + 465 = 807.| [Python (2 pointers for each input linked list, remember to take care of reminders)](add_two_numbers.py)||
|3|Medium|[Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Input: s = "abcabcbb"; Output: 3; <br> Explanation: The answer is "abc", with the length of 3.| [Python (2 pointers both start from index 0)](longest_substring_without_repeating_characters.py)||
|5|Medium|[Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | Input: s = "babad"; Output: "bab"; Note: "aba" is also a valid answer.| [Python (1 iteration thru the string with helper function to find max substr at each position)](longest_palindromic_substring.py)||
|6|Medium|[ZigZag Conversion](https://leetcode.com/problems/zigzag-conversion/) | Input: s = "PAYPALISHIRING", numRows = 3; Output: "PAHNAPLSIIGYIR" | [Python (first figure out interval from number of rows)](zigzag_conversion.py)|[plot](photos/zigzag.png)|
|7|Easy|[Reverse Integer](https://leetcode.com/problems/reverse-integer/) | Input: x = 123; Output: 321 | [Python (x mode 10 & Floor division, and remember to deal with negative number)](reverse_integer.py)||
|9|Easy|[Palindrome Number](https://leetcode.com/problems/palindrome-number/) | Input: x = 121; Output: true | [Python (similar to 7 Reverse Integer)](palindrome_number.py)||
|9|Medium|[Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | Input: height = [1,8,6,2,5,4,8,3,7]; Output: 49; Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49. | [Python (2 pointers starting from left and right, calculate and find max area)](container_with_most_water.py)|[plot](photos/container_most_water.png)|
|12|Medium|[Integer to Roman](https://leetcode.com/problems/integer-to-roman/) | Input: num = 1994; Output: "MCMXCIV"; Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.| [Python (Given some based mapping, loop over integers mapping from largest to smallest, and if input number is larger than mapping, subtract the int mapping, and append corresponding roman character)](integer_to_roman.py)||
