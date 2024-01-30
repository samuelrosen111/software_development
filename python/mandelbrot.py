import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(complex_number, max_iterations=50):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iterations:
        z = z*z + complex_number
        n += 1
    return n

def plot_mandelbrot(resolution, x_min, x_max, y_min, y_max):
    width, height = resolution
    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y

    image = np.zeros(Z.shape, dtype=float)
    for i in range(width):
        for j in range(height):
            image[j, i] = mandelbrot(Z[j, i])

    plt.figure(figsize=(10, 10))
    plt.imshow(image, extent=(x_min, x_max, y_min, y_max), cmap='hot', interpolation='bilinear')
    plt.colorbar()
    plt.title('Mandelbrot Set')
    plt.xlabel('Re')
    plt.ylabel('Im')
    plt.show()

def zoom_quadrant(x_min, x_max, y_min, y_max, quadrant):
    x_mid = (x_min + x_max) / 2
    y_mid = (y_min + y_max) / 2

    # NOTE: Quadrant numbering is as follows (y axis should be inverted as seen to get correct quadrant):
    if quadrant == 1:  # Top-left
        return x_min, x_mid, y_min, y_mid
    elif quadrant == 2:  # Top-right
        return x_mid, x_max, y_min, y_mid
    elif quadrant == 3:  # Bottom-left
        return x_min, x_mid, y_mid, y_max
    elif quadrant == 4:  # Bottom-right
        return x_mid, x_max, y_mid, y_max

def main():
    x_min, x_max = -2.5, 1.0
    y_min, y_max = -1.0, 1.0
    resolution = (1000, 1000)

    while True:
        plot_mandelbrot(resolution, x_min, x_max, y_min, y_max)
        print("\nQuadrants: 1.Top-left  2.Top-right  3.Bottom-left  4.Bottom-right")
        choice = input("Enter the quadrant to zoom into (or 'exit' to quit): ").strip().lower()

        if choice == 'exit':
            break

        if choice in ['1', '2', '3', '4']:
            quadrant = int(choice)
            x_min, x_max, y_min, y_max = zoom_quadrant(x_min, x_max, y_min, y_max, quadrant)
        else:
            print("Invalid input. Please enter a number between 1 and 4, or 'exit' to quit.")

if __name__ == '__main__':
    main()
