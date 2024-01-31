import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox

def mandelbrot(complex_number, max_iterations=50):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iterations:
        z = z*z + complex_number
        n += 1
    return n

def plot_mandelbrot(ax, resolution, x_min, x_max, y_min, y_max):
    ax.clear()  # Clear the previous plot
    width, height = resolution
    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y

    image = np.zeros(Z.shape, dtype=float)
    for i in range(width):
        for j in range(height):
            image[j, i] = mandelbrot(Z[j, i])

    ax.imshow(image, extent=(x_min, x_max, y_min, y_max), cmap='hot', interpolation='bilinear')
    ax.set_title('Mandelbrot Set')
    ax.set_xlabel('Real')
    ax.set_ylabel('Imaginary')
    plt.draw()  # Redraw the current figure

def update_plot():
    plot_mandelbrot(ax, resolution, x_min, x_max, y_min, y_max)

def submit_real_min(text):
    global x_min
    try:
        x_min = float(text)
        update_plot()
    except ValueError:
        print("Invalid input for Real Min.")

def submit_real_max(text):
    global x_max
    try:
        x_max = float(text)
        update_plot()
    except ValueError:
        print("Invalid input for Real Max.")

def submit_imag_min(text):
    global y_min
    try:
        y_min = float(text)
        update_plot()
    except ValueError:
        print("Invalid input for Imaginary Min.")

def submit_imag_max(text):
    global y_max
    try:
        y_max = float(text)
        update_plot()
    except ValueError:
        print("Invalid input for Imaginary Max.")

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.4)
resolution = (1000, 1000)
x_min, x_max, y_min, y_max = -2.5, 1.0, -1.0, 1.0

# Plot the initial Mandelbrot set
plot_mandelbrot(ax, resolution, x_min, x_max, y_min, y_max)

# Text boxes for entering the range
axbox_real_min = plt.axes([0.1, 0.25, 0.2, 0.05])
text_box_real_min = TextBox(axbox_real_min, 'Real Min', initial=str(x_min))
text_box_real_min.on_submit(submit_real_min)

axbox_real_max = plt.axes([0.4, 0.25, 0.2, 0.05])
text_box_real_max = TextBox(axbox_real_max, 'Real Max', initial=str(x_max))
text_box_real_max.on_submit(submit_real_max)

axbox_imag_min = plt.axes([0.1, 0.15, 0.2, 0.05])
text_box_imag_min = TextBox(axbox_imag_min, 'Imaginary Min', initial=str(y_min))
text_box_imag_min.on_submit(submit_imag_min)

axbox_imag_max = plt.axes([0.4, 0.15, 0.2, 0.05])
text_box_imag_max = TextBox(axbox_imag_max, 'Imaginary Max', initial=str(y_max))
text_box_imag_max.on_submit(submit_imag_max)

plt.show()
