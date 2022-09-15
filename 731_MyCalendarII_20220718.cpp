/*
//
// Created by gkbb on 2022/7/18.
//You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a triple booking.
//
//A triple booking happens when three events have some non-empty intersection (i.e., some moment is common to all the three events.).
//
//The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.
//
//Implement the MyCalendarTwo class:
//
//MyCalendarTwo() Initializes the calendar object.
//boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a triple booking. Otherwise, return false and do not add the event to the calendar.
//

//inserts a new element at the end of the vector, right after its current last element. This new element is constructed in place using args as the arguments for its constructor.
//
//This effectively increases the container size by one, which causes an automatic reallocation of the allocated storage space if -and only if- the new vector size surpasses the current vector capacity.
//
//The element is constructed in-place by calling allocator_traits::construct with args forwarded.
//
//A similar member function exists, push_back, which either copies or moves an existing object into the container.
// So generally speaking, emplace_back is better than the push_back
// It is easy to solve this question by using the traversal algorithm directly although using difference array can make code
// easier but the time complexity and space complexity is the same, therefore the segment tree is a better solution.

//*
// Difference array
*/
/*#include <iostream>
#include <vector>
#include <map>
using namespace std;

class MyCalendarTwo {
public:
    MyCalendarTwo() {

    }

    bool book(int start, int end) {
        int ans = 0;
        int maxBook = 0;
        cnt[start]++;
        cnt[end]--;
        for (auto &[_, freq] : cnt) {
            maxBook += freq;
            ans = max(maxBook, ans);
            if (maxBook > 2) {
                cnt[start]--;
                cnt[end]++;
                return false;
            }
        }
        return true;
    }
private:
    map<int, int> cnt;
};*//*




// NOT finished
#include <iostream>
#include <vector>
#include <bits/unordered_map.h>

using namespace std;


class MyCalendarTwo {
public:
    MyCalendarTwo() {
    }

    void update(int start, int end, int val, int left, int right, int index){
        if(right < start || left > end){
            return;
        }
        if(start <= left && end >= right){
            segment_tree[index].first += val;
            segment_tree[index].second += val;
        } else{
            int mid = (left + right) >> 1;
            update(start, end, val, left, mid, 2*index);
            update(start, end, val, mid+1, right, 2*index+1);
            segment_tree[index].first = segment_tree[index].second + max(segment_tree[2*index].first, segment_tree[2*index+1].first);
        }
    }

    bool book(int start, int end) {
        update(start, end-1, 1, 0, 1e9, 1);
        if(segment_tree[1].first > 2){
            update(start, end-1, -1, 0, 1e9,1);
            return false;
        }
        return true;

    }

private:
    unordered_map<int, pair<int, int>> segment_tree;
};

// * Your MyCalendarTwo object will be instantiated and called as such:
// * MyCalendarTwo* obj = new MyCalendarTwo();
// * bool param_1 = obj->book(start,end);




int main() {
    MyCalendarTwo myCalendarTwo;
    cout << boolalpha << myCalendarTwo.book(10, 20) << endl;
    cout << myCalendarTwo.book(50, 60) << endl;
    cout << myCalendarTwo.book(10, 40) << endl;
    cout << myCalendarTwo.book(5, 15) << endl;
    return 0;
}
*/
