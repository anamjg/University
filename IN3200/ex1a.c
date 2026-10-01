// code that verifies 1-1/2**2+1/2**4-1/2**6+ ... is 4/5

#include <stdio.h>

double calculate(int n)
{
    double sum = 0.0;
    for (int i = 0; i < n; i++) {
        sum += pow(-1, i) / pow(2, 2 * i);
    }

    return sum;

}

int main(int argc, char const *argv[])
{
    int n = 1000; // number of terms to calculate
    double result = calculate(n);
    double expected = 4.0 / 5.0;
    double epsilon = 1e-10; // tolerance for floating-point comparison
    double difference = result - expected;
    if (difference < 0) {
        difference = -difference; // take absolute value
    }
    if (difference < epsilon) {
        printf("The calculated value is close enough to the expected value.\n");
    } else {
        printf("The calculated value is NOT close enough to the expected value.\n");
    }
    printf("Calculated value: %.10f\n", result);
    printf("Expected value: %.10f\n", expected);
    printf("The difference is: %.10f\n", difference);

    return 0;
}
