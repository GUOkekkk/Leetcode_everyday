//
// Created by guo on 2021/9/15.
//
//A peak element is an element that is strictly greater than its neighbors.
//Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks. // therefore can only find the max
//You may imagine that nums[-1] = nums[n] = -∞.
//You must write an algorithm that runs in O(log n) time.

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int n = nums.size();
        // deal with the i=-1 and i=n
        auto get = [&](int i) -> pair<int, int> { // define a get function  // why not directly use nums[mid] // A: easy to deal with i==-1 and i==n
            if (i == -1 || i == n) {
                return {0, 0}; //You may imagine that nums[-1] = nums[n] = -∞. // When compare the pair, first compare the first one, if the same then the second
            }
            return {1, nums[i]};
        };

        int left = 0, right = n - 1, ans = -1;
        while (left <= right) {
            int mid = (left + right) / 2; // casue the time complexity is required as logn, binary search might be better.
            if (get(mid - 1) < get(mid) && get(mid) > get(mid + 1)) {
                ans = mid;
                break;
            }
            if (get(mid) < get(mid + 1)) {
                left = mid + 1;
            }
            else {
                right = mid - 1;
            }
        }
        return ans;
    }
};

int main()
{
    vector<int> nums = {1,5,9};
    Solution S1;
    cout << S1.findPeakElement(nums) << endl;
}
