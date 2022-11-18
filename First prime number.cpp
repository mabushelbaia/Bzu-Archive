#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
int isPrime(int n) { // self-explanatory
    if (n <= 1) return 0;
    if (n <= 3) return 1;

    for (int j = 2; j < n; j++) {
        if (n % j == 0) return 0;
    }
    return 1;
}
int nextPrime(int n) {
    if (n <= 1) return 2;
    int prime = n;
    while (!isPrime(prime)) {
        prime++;
    }
    return prime;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int n; cin >> n;
    cout << nextPrime(n);
    return 0;
}

