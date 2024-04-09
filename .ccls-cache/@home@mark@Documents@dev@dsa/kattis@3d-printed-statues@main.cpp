#include <iostream>

int printDays(int days) {
  printf("%d", days);
  return 0;
}

int main() {
  int N;
  int printers = 1;
  int days = 1;

  scanf("%d", &N); // input target value

  if (N < 1) printDays(days);

  while(printers < N) {
    days += 1;
    printers += printers;
  }

  printDays(days);;
}

/**
* print a printer each day
*
* 2: I + I
* 4: II + II
* 8: IIII + IIII
* 16: IIIIIIIIIIIIIIII + IIIIIIIIIIIIIIII
*/
