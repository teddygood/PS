#include <bits/stdc++.h>
using namespace std;

int main()
{
	int arr[100];
	int n = 0, max = 0;


	for (int i = 1; i <= 9; i++)
	{
		cin >> arr[i];

		if (max < arr[i])
		{
			max = arr[i];
			n = i;
		}
	}

	cout << max << " " << n << endl;
}