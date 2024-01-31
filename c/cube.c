#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <unistd.h>

#define PI 3.14159265358979323846

// Function to clear the terminal screen
void clearScreen() {
    printf("\033[2J");
    printf("\033[H");
}

// Function to rotate point around the Z axis
void rotateZ(float angle, float *x, float *y) {
    float newX = *x * cos(angle) - *y * sin(angle);
    float newY = *x * sin(angle) + *y * cos(angle);
    *x = newX;
    *y = newY;
}

// Function to rotate point around the Y axis
void rotateY(float angle, float *x, float *z) {
    float newX = *x * cos(angle) + *z * sin(angle);
    float newZ = -(*x) * sin(angle) + *z * cos(angle);
    *x = newX;
    *z = newZ;
}

int main() {
    float points[8][3] = {
        {-1, -1, -1}, {1, -1, -1}, {1, 1, -1}, {-1, 1, -1},
        {-1, -1, 1}, {1, -1, 1}, {1, 1, 1}, {-1, 1, 1}
    };

    int edges[12][2] = {
        {0, 1}, {1, 2}, {2, 3}, {3, 0},
        {4, 5}, {5, 6}, {6, 7}, {7, 4},
        {0, 4}, {1, 5}, {2, 6}, {3, 7}
    };

    float angleZ = 0.01;
    float angleY = 0.01;

    while (1) {
        clearScreen();

        // Rotate and project points
        for (int i = 0; i < 8; i++) {
            float x = points[i][0];
            float y = points[i][1];
            float z = points[i][2];

            rotateZ(angleZ, &x, &y);
            rotateY(angleY, &x, &z);

            // Project to 2D
            int u = (int)((x + 2) * 10);
            int v = (int)((y + 2) * 5);

            // Draw point
            printf("\033[%d;%dH*", v, u);
        }

        // Draw edges
        for (int i = 0; i < 12; i++) {
            float x0 = points[edges[i][0]][0];
            float y0 = points[edges[i][0]][1];
            float z0 = points[edges[i][0]][2];

            float x1 = points[edges[i][1]][0];
            float y1 = points[edges[i][1]][1];
            float z1 = points[edges[i][1]][2];

            rotateZ(angleZ, &x0, &y0);
            rotateY(angleY, &x0, &z0);
            rotateZ(angleZ, &x1, &y1);
            rotateY(angleY, &x1, &z1);

            int u0 = (int)((x0 + 2) * 10);
            int v0 = (int)((y0 + 2) * 5);
            int u1 = (int)((x1 + 2) * 10);
            int v1 = (int)((y1 + 2) * 5);

            printf("\033[%d;%dH*", (v0 + v1) / 2, (u0 + u1) / 2);
        }

        fflush(stdout);
        usleep(50000);

        // Increment angles
        // Increment angles for rotation
        angleZ += 0.05;
        angleY += 0.03;
    }

    return 0;
}