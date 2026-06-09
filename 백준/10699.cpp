#include <bits/stdc++.h>

using namespace std;

int main() {
    time_t t = time(NULL);
    tm* now = localtime(&t);
    cout << (now->tm_year + 1900) << '-' << (now->tm_mon + 1 < 10 ? "0" : "") << (now->tm_mon + 1) << '-' << (now->tm_mday < 10 ? "0" : "") << now->tm_mday << endl;
    return 0;
}
