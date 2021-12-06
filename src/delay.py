from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt 
import torch 
import copy 


def lorenz_attractor(x_0,y_0,z_0,sigma=10,beta=8/3,rho=28,steps=10000,end= 10):
    x = [x_0]
    y = [y_0]
    z = [z_0]

    for _ in range(steps):
        x.append(x[-1] + (sigma * (y[-1] - x[-1])) * end/steps)
        y.append(y[-1] + (x[-1] * (rho - z[-1]) - y[-1]) * end/steps)
        z.append(z[-1] + (x[-1] * y[-1] - beta * z[-1]) * end/steps)

    return (x,y,z)


def lorenz_attractor_endpoint(x_0,y_0,z_0,sigma=10,beta=8/3,rho=28,steps=10000,end= 10):
    x = copy.deepcopy(x_0)
    y = copy.deepcopy(y_0)
    z = copy.deepcopy(z_0)
    for _ in range(steps):
        x = x + sigma * (y - x) * end/steps
        y = y + (x * (rho - z) - y) * end/steps
        z = z + (x * y - beta * z) * end/steps
    
    return (x,y,z)


if __name__ == "__main__":
    fig = plt.figure()
    ax = fig.add_subplot(111,projection="3d")

    x0 = 5.0
    y0 = 5.0
    z0 = 5.0

    x,y,z = lorenz_attractor(x0,y0,z0)
    ax.plot(x,y,z)
    
    x_end,y_end,z_end = lorenz_attractor_endpoint(torch.tensor([x0,x0+1]),torch.tensor([y0,y0]),torch.tensor([z0,z0]))
    ax.scatter([x0,x0+1],[y0,y0],[z0,z0],color="green") #begin point
    ax.scatter(x_end,y_end,z_end,color="red") #end point
    plt.show()