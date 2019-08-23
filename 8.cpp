class Solution {
public:
    int myAtoi(string str) {
        int i = 0;
        bool negative = false;
        int firstChar = 0;
        while (!isdigit(str[i]) && i < str.length()) {
            i++;
        }
        
        
        while (str[firstChar] == ' ') firstChar++;
        if (i - firstChar > 1) {
            cout << i << endl;
            cout << firstChar << endl;
            return 0;
        }
        if (str[firstChar] != '-' && str[firstChar] != '+' && !isdigit(str[firstChar])) {
            return 0;
        }
        
        if (i != 0 && str[i-1] == '-') {
            negative = true;
        }
        
        if (i > 1 && str[i-2] == '-' && str[i-1] == '+') {
            return 0;
        }
        long long number = 0;
        while (isdigit(str[i]) && i < str.length()) {
            if (str[i] < '0' || str[i] > '9') break;
            number = number * 10;
            number = number + (str[i] - '0');
            //cout << number << endl;
            if (number > INT_MAX) {
                break;
            }
            i++;
            
        }
        
        if (number > INT_MAX) {
            if (negative) {
                return INT_MIN;
            } else {
                return INT_MAX;
            }
        }
        
        if (negative) {
            return number*(-1);
        } else {
            return number;
        }
        
        
    }
};
