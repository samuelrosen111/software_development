#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

void SieveOfEratosthenes(long long n, int show_progress) {
    long long segment_size = sqrt(n) + 1;
    char *is_prime = malloc(segment_size);
    memset(is_prime, 1, segment_size);

    for (long long i = 2; i * i <= n; i++) {
        if (is_prime[i]) {
            for (long long j = i * i; j * j <= n; j += i)
                is_prime[j] = 0;
        }
    }

    char *segment = malloc(segment_size);
    for (long long low = 0; low <= n; low += segment_size) {
        memset(segment, 1, segment_size);
        long long high = low + segment_size < n ? low + segment_size : n;

        for (long long i = 2; i * i <= n; i++) {
            if (is_prime[i]) {
                long long min_mult = (low + i - 1) / i * i;
                if (min_mult < i * i) min_mult += i;
                for (long long j = min_mult; j < high; j += i)
                    segment[j - low] = 0;
            }
        }

        for (long long i = low; i < high; i++)
            if (segment[i - low]) printf("%lld ", i);

        if (show_progress) {
            printf("\rProgress: %lld%%", 100 * low / n);
            fflush(stdout);
        }
    }

    free(is_prime);
    free(segment);
}

int main() {
    long long n;
    printf("Enter the number up to which you want to find prime numbers: ");
    scanf("%lld", &n);

    SieveOfEratosthenes(n, 1);

    return 0;
}
