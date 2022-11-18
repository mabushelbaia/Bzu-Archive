#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <unordered_set>
using namespace std;
int countOccurrences(int arr[], int n, int x)
{
    int res = 0;
    for (int i=0; i<n; i++)
        if (x == arr[i])
          res++;
    return res;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int n1, n2;cin >> n1 >> n2;
    int array1[n1], array2[n2];
    for(int i = 0; i < n1; i++)
        cin >> array1[i];
    for(int i = 0; i < n2; i++)
        cin >> array2[i];
    unordered_set<int> s(array1, array1 + n1);
    int counter = 0;
    for(int x: s)
        counter += countOccurrences(array2, n2, x);
    cout << counter;
    return 0;
}
