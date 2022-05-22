#include <iostream>
#include <math.h>

using namespace std;

int main()
{

    int m;
    int n;
    int sum = 0;
    int min = -1;

    cin >> m >> n;

    for (int i = m; i <= n; i++)
    {
        if (sqrt(i) == int(sqrt(i)))
        {
            sum += i;

            if (min == -1)
            {
                min = i;
            }
        }
    }

    if (sum > 0)
    {
        cout << sum << "\n";
        cout << min << "\n";
    }
    else
    {
        cout << min << "\n";
    }

    return 0;
}