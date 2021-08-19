import torch 
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt 

def lorenz_attractor(x_0,y_0,z_0,sigma=10,beta=8/3,rho=28,step_size=1/100):
    x = x_0
    y = y_0
    z = z_0
    while(True):
        x += (sigma * (y - x)) * step_size
        y += (x * (rho - z) - y) *step_size
        z += (x * y - beta * z) * step_size
        
        yield x,y,z


x_0 = torch.tensor([1.0])
y_0 = torch.tensor([1.0])
z_0 = torch.tensor([1.0])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.ion()

x_plot = torch.Tensor([])
y_plot = torch.Tensor([])
z_plot = torch.Tensor([])

x_plot_1 = torch.Tensor([])
y_plot_1 = torch.Tensor([])
z_plot_1 = torch.Tensor([])

f_1 = lorenz_attractor(x_0,y_0,z_0)
f_2 = lorenz_attractor(x_0+0.1,y_0+0.1,z_0+0.1)

while(True):
    x,y,z = next(f_1)
    x_1,y_1,z_1 = next(f_2)
    ax.cla()
    x_plot = torch.cat((x_plot,x))
    y_plot = torch.cat((y_plot,y))
    z_plot = torch.cat((z_plot,z))

    x_plot_1 = torch.cat((x_plot_1,x_1))
    y_plot_1 = torch.cat((y_plot_1,y_1))
    z_plot_1 = torch.cat((z_plot_1,z_1))

    ax.plot(x_plot.numpy(),y_plot.numpy(),z_plot.numpy(),color="blue")
    ax.plot(x_plot_1.numpy(),y_plot_1.numpy(),z_plot_1.numpy(),color="red")
    plt.pause(0.001)
plt.show()
