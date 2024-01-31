#include <stdio.h>

int main(){
    int A = 0; // length of each array
    int B = 0; // number of arrays
    scanf("%d", &A);
    scanf("%d", &B);
    // Create B arrays of char values of length A
    char arr[B][A];
    double count_hashtags = 0;
    double count_dots = 0;
    // Consume newline character after reading in B
    scanf(" %d", &B);

    for(int i = 0; i < B; i++){
        for(int j = 0; j < A; j++){
            scanf(" %c", &arr[i][j]);
            if(arr[i][j] == '#'){
                count_hashtags++;
            }
            else if(arr[i][j] == '.'){
                count_dots++;
            }
        }
    }

    double quotient = count_dots/count_hashtags;
    printf("%f", quotient);

    return 0;
}