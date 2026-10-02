#include <iostream>
using namespace std;

int main()
{
    int i = 1;
    // 外层while：控制行数
    while (i <= 9)
    {
        int j = 1;
        // 内层while：控制每行的式子
        while (j <= i)
        {
            cout << j << "*" << i << "=" << i*j << "\t";
            j++; // j自增
        }
        cout << endl; // 一行结束换行
        i++; // i自增
    }
    return 0;
}