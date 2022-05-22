#include <iostream>
#include <math.h>

using namespace std;

int main()
{
    int n;

    cin >> n;

    for (int i = 0; i < n; i++)
    {
        int currentMax = 0;
        string currentPlayer;
        int p;

        cin >> p;


        for (int j = 0; j < p; j++)
        {
            int c;
            string name;
            cin >> c >> name;

            if (c > currentMax) {
                currentMax = c;
                currentPlayer = name;
            }
        }
        cout << currentPlayer << "\n";
    }

    return 0;
}