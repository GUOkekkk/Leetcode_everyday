// Created by Ke GUO on 2021/09/14
// Leetcode Everyday: Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
//An input string is valid if:
//Open brackets must be closed by the same type of brackets.
//Open brackets must be closed in the correct order.



#include <iostream>
#include <vector>
using namespace std;

class Solution{
public:
    bool isValid(string s) {
        vector <char> tem{0}; // use vector to store the all kinds of dynamic information. Set a initial value to avoid some error.
        int n = s.size(); // set the size of the input is quiet necessary, but better have a meaningful name
        if (n % 2 == 1)
        {
            return false;
        }

        for (char pare:s) // use this way to extract the char
        {
            if(pare == '(' || pare == '[' || pare == '{')
            {
                tem.push_back(pare); // push_back: put the value into the vector
            }else if(pare == ')' && tem.back() == '(' //back: the last value
                     ||pare == ']' && tem.back() == '['
                     ||pare == '}' && tem.back() == '{')
            {
                tem.pop_back(); // pop_back: delete the last value
            }else
            {
                return false;

            }
        }
        tem.pop_back(); // remove the initial value
        return tem.empty(); // if empty?

    }
};

int main() {
    string s = "[()]";
    Solution S1; // how to use class, first create one
    cout << boolalpha << S1.isValid(s) << endl; // put in the variable and use the function
    return 0;
}
