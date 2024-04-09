# include <iostream>

int main() {
  long A;
  long B;
  int inputCount = 0;
  long differences[1000];


  // scan for input till EOF
  while(scanf("%ld %ld", &A, &B) != EOF) {
    // compure for the absolute diffs per scanned input
    differences[inputCount] = labs(A - B);
    inputCount += 1;
  }

  // print all differences afterwards
  for (int i=0; i<inputCount; i++) {
    printf("%ld\n", differences[i]);
  }
}
