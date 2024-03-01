/*
 * @lc app=leetcode id=347 lang=java
 *
 * [347] Top K Frequent Elements
 */

import java.util.*;
 
class Run{
     public static void main(String[] args){
         Solution solution = new Solution();
         System.out.println("Program running.");
         int result[] = solution.topKFrequent(new int[]{3,3,4,2,2,2},2);
         System.out.println(Arrays.toString(result));
         
     }
 }

// @lc code=start


class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> count = new HashMap<>(); // count={}
        //creating bucket
        List<Integer>[] sortedFrequency = new List[nums.length + 1]; // sortedFrequency=[[] for x in range(len(nums)+1)]
        // creating bucket part 2
        for (int i = 0; i < sortedFrequency.length; i++) { 
            sortedFrequency[i] = new ArrayList<>();
        }
        // inserting into dictionary/hashmap
        for (int num : nums) { // for num in nums:
            count.put(num, count.getOrDefault(num, 0) + 1); // count[num]=count.get(num, 0)+1
        }
        
        for (Map.Entry<Integer, Integer> entry : count.entrySet()) {
            int number = entry.getKey();
            int countValue = entry.getValue();
            sortedFrequency[countValue].add(number);
        }
        
        List<Integer> res = new ArrayList<>();
        for (int i = sortedFrequency.length - 1; i >= 0; i--) {
            List<Integer> arry = sortedFrequency[i];
            for (int num : arry) {
                res.add(num);
                if (res.size() == k) {
                    int[] result = new int[res.size()];
                    for (int j = 0; j < res.size(); j++) {
                        result[j] = res.get(j);
                    }
                    return result;
                }
            }
        }
        
        return null; // Or handle appropriately if k is larger than the number of unique elements
    }
}


// @lc code=end

