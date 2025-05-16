import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from sympy import symbols, sympify, lambdify
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Arc
import math

def d(func,var,x0,y0):
    pdelta = 10**(-9)
    ndelta = -10**(-9)
    if var == "x":
        D_x1 = round((func(x0 + ndelta,y0) - func(x0,y0))/ndelta,2)
        D_x2 = round((func(x0 + pdelta,y0) - func(x0,y0))/pdelta,2)
        if math.isnan(D_x2) or math.isnan(D_x1):
            return "Không tồn tại đạo hàm riêng theo biến x tại M0",False
        elif round(D_x1 - D_x2) != 0:
            return "Không tồn tại đạo hàm riêng theo biến x tại M0",False
        return D_x2,True

    elif var == "y":
        D_y1 = round((func(x0,y0 + ndelta) - func(x0,y0))/ndelta,2)
        D_y2 = round((func(x0,y0 + pdelta) - func(x0,y0))/pdelta,2)
        if math.isnan(D_y2) or math.isnan(D_y1):
            D_y2 = "Không tồn tại đạo hàm riêng theo biến y tại M0",False
        elif round(D_y1 - D_y2) != 0:
            return "Không tồn tại đạo hàm riêng theo biến y tại M0",False
        return D_y2,True

def main():
    #INP
    x, y = symbols('x y')
    expr = sympify(input("Nhap ham f(x,y): "))
    x0 = float(input("Nhap x0: "))
    y0 = float(input("Nhap y0: "))
    #Data
    func = lambdify((x, y), expr, 'numpy')
    try:
        func(x0,y0)
    except:
        print("Không tồn tại f(x0,y0). Hãy thử lại!")
        main()
    else:
        #Cal X - Partial Derivative
        D_x, xboo = d(func,"x",x0,y0)
        #Cal Y - Partial Derivative
        D_y, yboo = d(func,"y",x0,y0)
    print(f"F'x = {D_x}\nF'y = {D_y}")

    #Draw X-fig
    #Tạo figure 1
    fig1 = plt.figure(figsize=(10, 5))
    #Tạo subplot 2D ở vị trí 1 (trong lưới 1 hàng, 2 cột)
    ax1 = fig1.add_subplot(1, 2, 1)
    x = np.linspace(x0 - 0.3, x0 + 0.3, 100)
    z = func(x,y0)

    #Vẽ 2D - x
    ax1.plot(x, z, color='blue', label ="Đường cong Cx")
    ax1.scatter(x0, func(x0,y0), color='orange', s=50)
    ax1.text(x0,func(x0,y0),"M0")

    if xboo: #Có D_x mới vẽ được
        ax1.plot(x,D_x*(x-x0)+func(x0,y0), color ="cyan",label ="d1 - Tiếp tuyến tại M0 của đường cong Cx")
        ax1.axhline(y = func(x0,y0),color ="black", linestyle='--', linewidth=2)
        # Vẽ cung góc (bán kính nhỏ)
        angle = np.arctan(D_x)
        angle_deg = np.degrees(angle)
        if angle_deg < 0:
            angle_deg = angle_deg + 180
        arc = Arc((x0,func(x0,y0)), 0.2, 0.2, theta1=0, theta2=angle_deg,edgecolor='black')
        ax1.add_patch(arc)
        # Đặt nhãn alpha ở giữa cung
        mid_ang = angle/2
        ax1.text(x0 + 0.15*np.cos(mid_ang), func(x0,y0) + 0.15*np.sin(mid_ang),r'$\alpha$', fontsize=14)

    ax1.set_title(f'Mặt cắt 2D theo mặt y0 = {y0}\n' + r"tan($\alpha$)" + f"= f\'x(M0): {D_x}")
    ax1.set_xlabel('x')
    ax1.set_ylabel('z')
    ax1.axis('equal')

    # Tạo subplot 3D ở vị trí 2 (trong lưới 1 hàng, 2 cột)
    ax2 = fig1.add_subplot(1, 2, 2, projection='3d')
    X = np.linspace(x0 - 0.3, x0 + 0.3, 100)
    Y = np.linspace(y0 - 0.3, y0 + 0.3, 100)
    X, Y = np.meshgrid(X, Y)
    Z = func(X,Y)
    x_line = np.linspace(x0 - 0.3, x0 + 0.3, 200)
    y_line = np.full_like(x0, y0)      
    z_line = func(x_line, y_line)

    #Vẽ 3D - x
    if xboo: #Có D_x mới vẽ đường tiếp tuyến được
        t = np.linspace(-0.3, 0.3, 100)
        Xt = x0 + t
        Yt = np.full_like(t, y0)
        Zt = func(x0,y0) + D_x * t
        ax2.plot(Xt, Yt, Zt, color='cyan')
        ax2.scatter(x0, y0, func(x0,y0), color='orange', s=50)
        ax2.text(x0,y0,func(x0,y0),f"M0({x0},{y0})")

    ax2.plot_surface(X, Y, Z, cmap='binary')
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
    y = np.linspace(y0 - 0.3, y0 + 0.3, 100)
    z = func(x0,y)

    #Vẽ 2D - y
    ax1.plot(y, z, color='blue',label = "Đường cong Cy")

    if yboo: #Có D_y mới vẽ được
        ax1.scatter(y0, func(x0,y0), color='orange', s=50)
        ax1.text(y0,func(x0,y0),"M0")
        ax1.plot(y,D_y*(y-y0)+func(x0,y0), color ="cyan", label ="d2 - Tiếp tuyến tại M0 của đường cong Cy")
        ax1.axhline(y = func(x0,y0),color ="black", linestyle='--', linewidth=2)
        # Vẽ cung góc (bán kính nhỏ)
        angle = np.arctan(D_y)
        angle_deg = np.degrees(angle)
        if angle_deg < 0:
            angle_deg = angle_deg + 180
        arc = Arc((y0,func(x0,y0)), 0.2, 0.2, theta1=0, theta2=angle_deg,edgecolor='black')
        ax1.add_patch(arc)
        # Đặt nhãn alpha ở giữa cung
        mid_ang = angle/2
        ax1.text(y0 + 0.15*np.cos(mid_ang), func(x0,y0) + 0.15*np.sin(mid_ang),r'$\beta$', fontsize=14)

    ax1.set_title(f'Mặt cắt 2D theo mặt x = {x0}\n' + r"tan($\beta$)" + f"= f\'y(M0): {D_y}")
    ax1.set_xlabel('y')
    ax1.set_ylabel('z')
    ax1.axis('equal')

    # Tạo subplot 3D ở vị trí 2 (trong lưới 1 hàng, 2 cột)
    ax2 = fig2.add_subplot(1, 2, 2, projection='3d')
    X = np.linspace(x0 - 0.3, x0 + 0.3, 100)
    Y = np.linspace(y0 - 0.3, y0 + 0.3, 100)
    X, Y = np.meshgrid(X, Y)
    Z = func(X,Y)
    y_line = np.linspace(y0 - 0.3, y0 + 0.3, 200)   
    x_line = np.full_like(y0,x0)  
    z_line = func(x_line, y_line)

    #Vẽ 3D - y
    if yboo: #Có D_y mới vẽ tiếp tuyến 3D được
        t = np.linspace(-0.3, 0.3, 100)
        Xt = np.full_like(t, x0)
        Yt = y0 + t
        Zt = func(x0,y0) + D_y * t
        ax2.plot(Xt, Yt, Zt, color='cyan')
        ax2.scatter(x0, y0, func(x0,y0), color='black', s=50)
        ax2.text(x0,y0,func(x0,y0),f"M0({x0},{y0})")

    ax2.plot_surface(X, Y, Z, cmap='binary')
    ax2.plot(x_line,y_line,z_line, color ="Blue")

    ax2.set_title(f'Đồ thị 3D: z = {expr}')
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    ax2.set_zlabel('z')

    fig2.legend()
    #Draw fig3 - Grad + Surface
    fig3 = plt.figure(figsize = (10,5))
    ax = fig3.add_subplot(111, projection='3d')

    #Vẽ đồ thị 3D
    X = np.linspace(x0 - 0.3, x0 + 0.3, 50)
    Y = np.linspace(y0 - 0.3, y0 + 0.3, 50)
    X, Y = np.meshgrid(X, Y)
    Z = func(X,Y)

    ax.plot_surface(X, Y, Z, alpha=0.7, rstride=1, cstride=1)
    ax.scatter(x0, y0, func(x0,y0), color='black', s=50)
    ax.text(x0,y0,func(x0,y0),f"M0({x0},{y0})")
    #Vẽ MPTT
    if xboo and yboo: #Có D_x và D_y mới vẽ được MPTT
        T = func(x0,y0) + D_x * (X - x0) + D_y * (Y - y0)
        ax.plot_surface(X, Y, T,alpha=0.5, rstride=1, cstride=1, label ="Mặt phẳng tiếp tuyến của f tại M0")
    #Vẽ tiếp tuyến - x
    if xboo:
        t = np.linspace(-0.3, 0.3, 100)
        Xt = x0 + t
        Yt = np.full_like(t, y0)
        Zt = func(x0,y0) + D_x * t
        ax.plot(Xt, Yt, Zt, color='red',label='∂f/∂x tại M0')
    #Vẽ tiếp tuyến - y
    if yboo:
        t = np.linspace(-0.3, 0.3, 100)
        xt = np.full_like(t, x0)
        yt = y0 + t
        zt = func(x0,y0) + D_y * t
        ax.plot(xt, yt, zt, color='green', label='∂f/∂y tại M0')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('f(x, y)')
    fig3.legend()
    plt.title(f"Đồ thị hàm và tiếp tuyến tại M0({x0}, {y0})")

    #Vẽ grad-Vec + Bieu đò đường đồng mức
    fig4 = plt.figure(figsize=(10, 5))    
    ax = plt.gca() # lấy đối tượng Axes hiện tại

    # Bước 3: Tạo lưới điểm và tính Z
    x = np.linspace(-3, 3, 200)
    y = np.linspace(-3, 3, 200)
    X, Y = np.meshgrid(x, y)
    Z = func(X, Y)

    # Bước 4: Vẽ contour
    levels = 15 # số đường đồng mức
    cs = ax.contour(X, Y, Z, levels=levels, linewidths=1)

    # Tô màu giữa các vùng contour
    cf = ax.contourf(X, Y, Z, levels=levels, alpha=0.7)

    ax.set_title('Biểu đồ đường đồng mức của f(x, y)')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    if xboo and yboo:    
        ax.quiver(x0, y0, D_x/(5*np.sqrt(D_x**2 + D_y**2)), D_y/(5*np.sqrt(D_x**2 + D_y**2)), label = "Vector gradiant", color='black')
    fig4.legend()

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()