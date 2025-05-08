import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from sympy import symbols, sympify, lambdify
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Arc
import math

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
if math.isnan(func(x0,y0)):
    xboo = False
    yboo = False
D_x1 = round((func(x0 + ndelta,y0) - func(x0,y0))/ndelta,2)
D_x2 = round((func(x0 + pdelta,y0) - func(x0,y0))/pdelta,2)
if math.isnan(D_x2) or math.isnan(D_x1):
    D_x2 = "Không tồn tại đạo hàm riêng theo biến x tại M0"
    xboo = False
elif round(D_x1 - D_x2) != 0:
    D_x2 = "Không tồn tại đạo hàm riêng theo biến x tại M0"
    xboo = False

#Cal Y - Partial Derivative
D_y1 = round((func(x0,y0 + ndelta) - func(x0,y0))/ndelta,2)
D_y2 = round((func(x0,y0 + pdelta) - func(x0,y0))/pdelta,2)
if math.isnan(D_y2) or math.isnan(D_y1):
    D_y2 = "Không tồn tại đạo hàm riêng theo biến y tại M0"
    xboo = False
elif round(D_y1 - D_y2) !=0:
    D_y2 = "Không tồn tại đạo hàm riêng theo biến y tại M0"
    yboo = False

#Draw X-fig

#Tạo figure 1
fig1 = plt.figure(figsize=(10, 5))
#Tạo subplot 2D ở vị trí 1 (trong lưới 1 hàng, 2 cột)
ax1 = fig1.add_subplot(1, 2, 1)
x = np.linspace(x0 - 1, x0 + 1, 100)
z = func(x,y0)

#Vẽ 2D - x
ax1.plot(x, z, color='blue', label ="Đường cong Cx")
ax1.scatter(x0, func(x0,y0), color='orange', s=50)
ax1.text(x0,func(x0,y0),"M0")
if xboo:
    ax1.plot(x,D_x2*(x-x0)+func(x0,y0), color ="cyan",label ="d1 - Tiếp tuyến tại M0 của đường cong Cx")
    ax1.axhline(y = func(x0,y0),color ="black", linestyle='--', linewidth=2)
    # Vẽ cung góc (bán kính nhỏ)
    angle = np.arctan(D_x2)
    angle_deg = np.degrees(angle)
    if angle_deg < 0:
        angle_deg = angle_deg + 180
    arc = Arc((x0,func(x0,y0)), 1, 1, theta1=0, theta2=angle_deg,edgecolor='black')
    ax1.add_patch(arc)
    # Đặt nhãn alpha ở giữa cung
    mid_ang = angle/2
    ax1.text(x0 + 0.75*np.cos(mid_ang), func(x0,y0) + 0.75*np.sin(mid_ang),r'$\alpha$', fontsize=14)

ax1.set_title(f'Mặt cắt 2D theo mặt y0 = {y0}\n' + r"tan($\alpha$)" + f"= f\'x(M0): {D_x2}")
ax1.set_xlabel('x')
ax1.set_ylabel('z')
ax1.axis('equal')

# Tạo subplot 3D ở vị trí 2 (trong lưới 1 hàng, 2 cột)
ax2 = fig1.add_subplot(1, 2, 2, projection='3d')
X = np.linspace(x0 - 1, x0 + 1, 100)
Y = np.linspace(y0 - 1, y0 + 1, 100)
X, Y = np.meshgrid(X, Y)
Z = func(X,Y)
x_line = np.linspace(x0 - 1, x0 + 1, 200)
y_line = np.full_like(x0, y0)      
z_line = func(x_line, y_line)

#Vẽ 3D - x
if xboo:
    t = np.linspace(-5, 5, 100)
    Xt = x0 + t
    Yt = np.full_like(t, y0)
    Zt = func(x0,y0) + D_x2 * t
    ax2.plot(Xt, Yt, Zt, color='cyan')

ax2.plot_surface(X, Y, Z, cmap='Pastel1')
ax2.scatter(x0, y0, func(x0,y0), color='orange', s=50)
ax2.text(x0,y0,func(x0,y0),f"M0({x0},{y0})")
ax2.plot(x_line,y_line,z_line, color = "Blue")

ax2.set_title(f'Đồ thị 3D: z = {expr}')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('z')

plt.tight_layout()
fig1.legend()

#Draw Y-fig

# Tạo figure 2
fig2 = plt.figure(figsize=(10, 5))

# Tạo subplot 2D ở vị trí 1 (trong lưới 1 hàng, 2 cột)
ax1 = fig2.add_subplot(1, 2, 1)
y = np.linspace(y0 - 1, y0 + 1, 100)
z = func(x0,y)

#Vẽ 2D - y
ax1.plot(y, z, color='blue',label = "Đường cong Cy")
ax1.scatter(y0, func(x0,y0), color='orange', s=50)
ax1.text(y0,func(x0,y0),"M0")
if yboo:
    ax1.plot(y,D_y2*(y-y0)+func(x0,y0), color ="cyan", label ="d2 - Tiếp tuyến tại M0 của đường cong Cy")
    ax1.axhline(y = func(x0,y0),color ="black", linestyle='--', linewidth=2)
    # Vẽ cung góc (bán kính nhỏ)
    angle = np.arctan(D_y2)
    angle_deg = np.degrees(angle)
    if angle_deg < 0:
        angle_deg = angle_deg + 180
    arc = Arc((y0,func(x0,y0)), 1, 1, theta1=0, theta2=angle_deg,edgecolor='black')
    ax1.add_patch(arc)
    # Đặt nhãn alpha ở giữa cung
    mid_ang = angle/2
    ax1.text(y0 + 0.75*np.cos(mid_ang), func(x0,y0) + 0.75*np.sin(mid_ang),r'$\beta$', fontsize=14)

ax1.set_title(f'Mặt cắt 2D theo mặt x = {x0}\n' + r"tan($\beta$)" + f"= f\'y(M0): {D_y2}")
ax1.set_xlabel('y')
ax1.set_ylabel('z')
ax1.axis('equal')

# Tạo subplot 3D ở vị trí 2 (trong lưới 1 hàng, 2 cột)
ax2 = fig2.add_subplot(1, 2, 2, projection='3d')
X = np.linspace(x0 - 1, x0 + 1, 100)
Y = np.linspace(y0 - 1, y0 + 1, 100)
X, Y = np.meshgrid(X, Y)
Z = func(X,Y)
y_line = np.linspace(y0 - 1, y0 + 1, 200)   
x_line = np.full_like(y0,x0)  
z_line = func(x_line, y_line)

#Vẽ 3D - y
if yboo:
    t = np.linspace(-5, 5, 100)
    Xt = np.full_like(t, x0)
    Yt = y0 + t
    Zt = func(x0,y0) + D_y2 * t
    ax2.plot(Xt, Yt, Zt, color='cyan')

ax2.plot_surface(X, Y, Z, cmap='binary')
ax2.scatter(x0, y0, func(x0,y0), color='black', s=50)
ax2.text(x0,y0,func(x0,y0),f"M0({x0},{y0})")
ax2.plot(x_line,y_line,z_line, color ="Blue")

ax2.set_title(f'Đồ thị 3D: z = {expr}')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('z')

plt.tight_layout()
fig2.legend()
plt.show()