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
|12|Medium|[Integer to Roman](https://leetcode.com/problems/integer-to-roman/) | Input: num = 1994; Output: "MCMXCIV"; Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.| [Python (Given basic mapping (two arrays 1 integers 1 roman, ascending sorted), loop over integers mapping from largest to smallest, and if input number is larger than mapping, subtract the int mapping, and append corresponding roman character)](integer_to_roman.py)||
|13|Easy|[Integer to Roman](https://leetcode.com/problems/roman-to-integer/) | Input: s = "LVIII"; Output: 58; Explanation: L = 50, V= 5, III = 3.| [Python (loop thru input roman from right to left, create a maxdigit var, and for each mapped int check if it is bigger than maxdigit, if so add int to result sum if not subtract it from sum)](roman_to_integer.py)||
|14|Easy|[Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) | Input: strs = ["flower","flow","flight"]; Output: "fl"| [Python (2 loops, loop over first word, within that loop over the array, and check if char is the same)](longest_common_prefix.py)||
|15|Medium|[3Sum](https://leetcode.com/problems/3sum/) | Input: nums = [-1,0,1,2,-1,-4]; Output: [[-1,-1,2],[-1,0,1]]| [Python (sort array, 3 loops, t loops over array, then 2 other indexes, i and j start from right side of t and end of array, move i and j close to the middle and trying to get sum zero.  remember to deal with same consecutive values.)](3sum.py)||
|16|Medium|[3Sum Closest](https://leetcode.com/problems/3sum-closest/) | Input: nums = [-1,2,1,-4], target = 1;Output: 2; Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).| [Python (similar to 15 3sum, with small difference in comparison condition (compare abs difference of sum and target with a placeholder sum ))](3sum.py)||
|19|Medium|[Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | Input: head = [1,2,3,4,5], n = 2;Output: [1,2,3,5]| [Python (fast and slow pointers, the fast pointer first move to the nth node so that there is n steps between fast and slow, and then move both fast and slow until fast reaches the end. Need to deal with corner case when list is shorter than expected)](remove_nth_node_from_end_of_list.py)||
|20|Easy|[Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | Input: s = "([)]"; Output: false| [Python (use hashmap  that is reversed parenthesizes pairs and a stack that temporarily stores one element (when looping over the input str), check if current element in hashmap, if so compare stack.pop() with the corresponding value in Hashmap)](valid_parentheses.py)||
|21|Easy|[Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | Input: l1 = [1,2,4], l2 = [1,3,4]; Output: [1,1,2,3,4,4]| [Python (2 pointers and compare values)](merge_two_sorted_lists.py)||
|22|Medium|[Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) | Input: n = 3; Output: ["((()))","(()())","(())()","()(())","()()()"]| [Python (dfs)](generate_parentheses.py)|[plot](photos/gen_paren.png)|
|23|Hard|[Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | Input: lists = [[1,4,5],[1,3,4],[2,6]]; Output: [1,1,2,3,4,4,5,6]| [Python (heapq, this solution only passes in python2)](merge_k_sorted_lists.py)||
|24|Medium|[Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/) | Input: head = [1,2,3,4];Output: [2,1,4,3]| [Python (Needs to be clear on linked list manipulations (how nodes swapping happens))](swap_nodes_in_pairs.py)||
|26|Easy|[Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | Input: head = [1,2,3,4];Output: [2,1,4,3]| [Python (iterate over the list, and set a global var to compare with ))](remove_duplicates_from_sorted_array.py)||
|27|Easy|[Remove Element](https://leetcode.com/problems/remove-element/) | Given nums = [3,2,2,3], val = 3, Your function should return length = 2, with the first two elements of nums being 2.It doesn't matter what you leave beyond the returned length.| [Python](remove_element.py)||
|28|Easy|[Implement strStr()](https://leetcode.com/problems/implement-strstr/) | Input: haystack = "hello", needle = "ll";Output: 2| [Python](implement_strstr.py)||
|33|Medium|[Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | Input: nums = [4,5,6,7,0,1,2], target = 0; Output: 4| [Python (binary search with more complicated conditions to make decisions)](search_in_rotated_sorted_array.py)||
|34|Medium|[Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | Input: nums = [5,7,7,8,8,10], target = 8;Output: [3,4]| [Python (2 binary searches to find higher bound and lower bound)](find_first_and_last_position_of_element_in_sorted_array.py)||
|35|Easy|[Search Insert Position](https://leetcode.com/problems/search-insert-position/) | Input: [1,3,5,6], 5; Output: 2| [Python ( binary search)](search_insert_position.py)||
|36|Medium|[Valid Sudoku](https://leetcode.com/problems/valid-sudoku/) |[see plot](photos/valid_sudoku.png)| [Python (2 loops over cols and rows, to check each populated cell with helper function that checks 3 conditions, row, col, and 3x3 box on duplicated values)](valid_sudoku.py)|[plot](photos/valid_sudoku.png)|
|38|Easy|[Count and Say](https://leetcode.com/problems/count-and-say/) |Input: 4;Output: "1211";Explanation: For n = 3 the term was "21" in which we have two groups "2" and "1", "2" can be read as "12" which means frequency = 1 and value = 2, the same way "1" is read as "11", so the answer is the concatenation of "12" and "11" which is "1211".| [Python (use a trick via itertools.groupby, e.g. [(k,list(g)) for k, g in itertools.groupby('AAAABBBCCDAABBB')] ---> `[('A', ['A', 'A', 'A', 'A']), ('B', ['B', 'B', 'B']), ('C', ['C', 'C']), ('D', ['D']), ('A', ['A', 'A']), ('B', ['B', 'B', 'B'])]`)](count_and_say.py)||
|39|Medium|[Combination Sum](https://leetcode.com/problems/combination-sum/) |Input: candidates = [2,3,6,7], target = 7; Output: [[2,2,3],[7]]; Explanation:2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.; 7 is a candidate, and 7 = 7.; These are the only two combinations.| [Python (dfs)](combination_sum.py)|[plot](photos/combination_sum.png)|
|40|Medium|[Combination Sum II](https://leetcode.com/problems/combination-sum-ii/) |Input: candidates = [2,5,2,1,2], target = 5,;A solution set is:[  [1,2,2],  [5]]| [Python (dfs with one more condition checks if current values is the same as the previous)](combination_sum_ii.py)||
|43|Medium|[Multiply Strings](https://leetcode.com/problems/multiply-strings/) |Input: num1 = "123", num2 = "456";Output: "56088"| [Python (replicate rule of multiplication on multi-digit numbers with 2 arrays)](multiply_strings.py)||
|46|Medium|[Permutations](https://leetcode.com/problems/permutations/) |Input: [1,2,3];Output:[  [1,2,3],  [1,3,2],  [2,1,3],  [2,3,1],  [3,1,2],  [3,2,1]]| [Python (dfs)](permutations.py)|[plot](photos/permutations.png)|
|47|Medium|[Permutations II](https://leetcode.com/problems/permutations-ii/) |Input: [1,1,2];Output:[  [1,1,2],  [1,2,1],  [2,1,1]]| [Python (dfs additional check {if nums[i] == previousNum: continue})](permutations_ii.py)||
|48|Medium|[Rotate Image](https://leetcode.com/problems/rotate-image/) |Input: matrix = [[1,2,3],[4,5,6],[7,8,9]];Output: [[7,4,1],[8,5,2],[9,6,3]]| [Python (2 steps, 1st flip columns to rows, 2nd reverse each row)](rotate_image.py)|[plot](photos/rotate_image.png)|
|49|Medium|[Group Anagrams](https://leetcode.com/problems/group-anagrams/) |Input: strs = ["eat","tea","tan","ate","nat","bat"];Output: [["bat"],["nat","tan"],["ate","eat","tea"]]| [Python (use collections.defaultdict(list))](group_anagrams.py)||
|50|Medium|[Pow(x, n)](https://leetcode.com/problems/powx-n/) |Input: x = 2.00000, n = 10;Output: 1024.00000| [Python (keep on floor division with 2, and deal with corner cases such as negative number, 0, and x or n == 1)](powx_n.py)||
|51|Hard|[N-Queens](https://leetcode.com/problems/n-queens/) |[see plot](photos/queens.png)| [Python (dfs)](n_queens.py)|[see plot](photos/queens.png)|
|53|Easy|[Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) |Input: nums = [-2,1,-3,4,-1,2,1,-5,4];Output: 6; Explanation: [4,-1,2,1] has the largest sum = 6.| [Python (create 2 vars 1) tmp to record previous sum and a 2) totalsum, if tmp < 0 discard and keep on track of MAX totalsum)](maximum_subarray.py)||
|53|Easy|[Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) |Input: nums = [-2,1,-3,4,-1,2,1,-5,4];Output: 6; Explanation: [4,-1,2,1] has the largest sum = 6.| [Python (create 2 vars 1) tmp to record previous sum and a 2) totalsum, if tmp < 0 discard and keep on track of MAX totalsum)](maximum_subarray.py)||
|54|Medium|[Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) |Input:[ [ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ]]Output: [1,2,3,6,9,8,7,4,5]| [Python (deal with 4 directions 0: go right   1: go down  2: go left  3: go up; if up > down or left > right: return res)](spiral_matrix.py)||
|55|Medium|[Jump Game](https://leetcode.com/problems/jump-game/) |Input: nums = [2,3,1,1,4];Output: true;Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.| [Python](jump_game.py)||
|56|Medium|[Merge Intervals](https://leetcode.com/problems/merge-intervals/) |Input: intervals = [[1,4],[4,5]];Output: [[1,5]]; Explanation: Intervals [1,4] and [4,5] are considered overlapping.| [Python](merge_intervals.py)||
|58|Easy|[Length of Last Word](https://leetcode.com/problems/length-of-last-word/) |Input: "Hello World" Output: 5| [Python (2 pointers left and right)](length_of_last_word.py)||
|59|Medium|[Spiral Matrix II](https://leetcode.com/problems/spiral-matrix-ii/) |Input: 3 Output:[ [ 1, 2, 3 ], [ 8, 9, 4 ], [ 7, 6, 5 ]]| [Python ](spiral_matrix_ii.py)||
|61|Medium|[Rotate List](https://leetcode.com/problems/rotate-list/) |Input: 1->2->3->4->5->NULL, k = 2 Output: 4->5->1->2->3->NULL| [Python ](rotate_list.py)||
|62|Medium|[Unique Paths](https://leetcode.com/problems/unique-paths/) |Input: m = 3, n = 2 Output: 3 Explanation:From the top-left corner, there are a total of 3 ways to reach the bottom-right corner: 1. Right -> Down -> Down 2. Down -> Down -> Right 3. Down -> Right -> Down| [Python (permutation formula  n choose m-n ) ](unique_paths.py)||
