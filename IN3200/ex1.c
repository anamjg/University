#include <stdio.h>
#include <math.h>

double numerical_integration (double x_min, double x_max, int slices)
{
    double delta_x = (x_max - x_min) / slices;
    double x, sum = 0.0;
    for (int i = 0; i < slices; i++) {
        x = x_min + i * delta_x;
        sum = sum + 4.0/(1.0 + x*x);
    }
    return sum * delta_x;
}


int main(int argc, char const *argv[])
{
    double x_min = 0.0;
    double x_max = 1.0;
    int slices = 1000000; // number of slices for numerical integration
    double result = numerical_integration(x_min, x_max, slices);
    double expected = M_PI; // expected value of pi
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
    printf("Calculated value of pi: %.10f\n", result);
    return 0;
}