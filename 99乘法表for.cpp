#include <iostream>
using namespace std;//写这个容易忘分号

int main()
{
    for (int i = 1; i <= 9; i++)//2层for循环,i从1刷到9
    {
        for (int j = 1; j <= i; j++)//j从1刷到i
        {
            cout << j << "*" << i << "=" << i*j << "\t";//cout(charactor out)比C的printf()性能好
        }
        cout << endl;//换行
    }
    return 0;
}