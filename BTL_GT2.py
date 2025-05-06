import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from sympy import symbols, sympify, lambdify
from mpl_toolkits.mplot3d import Axes3D


#INP
x, y = symbols('x y')
expr = sympify(input("Nhap ham f(x,y): "))
x0 = float(input("Nhap x0: "))
y0 = float(input("Nhap y0: "))
#FixData
func = lambdify((x, y), expr, 'numpy')
xboo= True
yboo = True

#Cal X - Partial Derivative
pdelta = 10**(-9)
ndelta = -10**(-9)
D_x1 = round((func(x0 + ndelta,y0) - func(x0,y0))/ndelta,2)
D_x2 = round((func(x0 + pdelta,y0) - func(x0,y0))/pdelta,2)

#Cal Y - Partial Derivative
D_y1 = round((func(x0,y0 + ndelta) - func(x0,y0))/ndelta,2)
D_y2 = round((func(x0,y0 + pdelta) - func(x0,y0))/pdelta,2)
if round(D_x1 - D_x2) != 0:
    D_x2 = "Không tồn tại đạo hàm riêng theo biến x"
    xboo = False
if round(D_y1 - D_y2) !=0:
    D_y2 = "Không tồn tại đạo hàm riêng theo biến y"
    yboo = False

#Draw with X-fig
# Tạo figure 1
fig1 = plt.figure(figsize=(10, 5))

# Tạo subplot 2D ở vị trí 1 (trong lưới 1 hàng, 2 cột)
ax1 = fig1.add_subplot(1, 2, 1)
x = np.linspace(x0 - 5, x0 + 5, 100)
y = func(x,y0)

ax1.plot(x, y, color='blue')
ax1.scatter(x0, func(x0,y0), color='orange', s=50)
ax1.text(x0,func(x0,y0),"M0")
if xboo:
    ax1.plot(x,D_x2*(x-x0)+func(x0,y0), color ="cyan")
    # ax1.plot([x0,func(x0,y0)], [x0, func(x0,y0)],color ="black", linestyle='-.', linewidth=2)

ax1.set_title(f'Mặt cắt 2D tại y0 = {y0}\nD\'x: {D_x2}')
ax1.set_xlabel('x')
ax1.set_ylabel('z')

# Tạo subplot 3D ở vị trí 2 (trong lưới 1 hàng, 2 cột)
ax2 = fig1.add_subplot(1, 2, 2, projection='3d')
X = np.linspace(x0 - 5, x0 + 5, 100)
Y = np.linspace(y0 - 5, y0 + 5, 100)
X, Y = np.meshgrid(X, Y)
Z = func(X,Y)

ax2.plot_surface(X, Y, Z, cmap='Blues')
ax2.scatter(x0, y0, func(x0,y0), color='orange', s=50)
ax2.text(x0,y0,func(x0,y0),f"M0({x0},{y0})")

ax2.set_title(f'Đồ thị 3D: z = {expr}')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('z')

plt.tight_layout()

#Draw with Y-fig
# Tạo figure 2
fig2 = plt.figure(figsize=(10, 5))

# Tạo subplot 2D ở vị trí 1 (trong lưới 1 hàng, 2 cột)
ax1 = fig2.add_subplot(1, 2, 1)
y = np.linspace(x0 - 5, x0 + 5, 100)
z = func(x0,y)

ax1.plot(y, z, color='blue')
ax1.scatter(y0, func(x0,y0), color='orange', s=50)
ax1.text(y0,func(x0,y0),"M0")
if yboo:
    ax1.plot(y,D_y2*(y-y0)+func(x0,y0), color ="cyan")
    # ax1.plot(func(x0,y0),color ="black")

ax1.set_title(f'Mặt cắt 2D tại x0 = {x0}\nD\'y: {D_y2}')
ax1.set_xlabel('y')
ax1.set_ylabel('z')

# Tạo subplot 3D ở vị trí 2 (trong lưới 1 hàng, 2 cột)
ax2 = fig2.add_subplot(1, 2, 2, projection='3d')
X = np.linspace(x0 - 5, x0 + 5, 100)
Y = np.linspace(y0 - 5, y0 + 5, 100)
X, Y = np.meshgrid(X, Y)
Z = func(X,Y)

ax2.plot_surface(X, Y, Z, cmap='Blues')
ax2.scatter(x0, y0, func(x0,y0), color='black', s=50)
ax2.text(x0,y0,func(x0,y0),f"M0({x0},{y0})")

ax2.set_title(f'Đồ thị 3D: z = {expr}')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('z')

plt.tight_layout()
plt.show()