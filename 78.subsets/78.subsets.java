import java.util.*;
/*
 * @lc app=leetcode id=78 lang=java
 *
 * [78] Subsets
 */
class Run{
  public static void main(String[] args){
      Solution solution = new Solution();
      System.out.println("Program running.");
      int[] test = {3,4,4,2,2,2}
      int result[] = solution.subsets(new int[]{3,4,4,2,2,2},2);
      System.out.println(Arrays.toString(result));
      
  }
}
// @lc code=start
class Solution {
  public List<List<Integer>> subsets(int[] nums) {
    var list = new ArrayList<List<Integer>>();

    solve(nums, 0, new ArrayList<Integer>(), list);

    return list;
  }

  void solve(final int[] nums, final int i, final List<Integer> list, List<List<Integer>> finalList) {
    if (i == nums.length) {
      finalList.add(list);
      return;
    }

    // without
    solve(nums, i + 1, list, finalList);

    var with = new ArrayList<Integer>(list);
    with.add(nums[i]);
    solve(nums, i + 1, with, finalList);
  }
}
// @lc code=end

