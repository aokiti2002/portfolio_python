import random
from matplotlib import pyplot as plt
import numpy as np
import torch
import torch.nn as nn
import inspect
import pickle
from copy import deepcopy

class Net(torch.nn.Module):

    def __init__(self, seed=123):
    
        super(Net, self).__init__()

        torch.manual_seed(seed)

        self.full = nn.Sequential(
            nn.Linear(1,32),
            nn.ReLU(),
            nn.Linear(32,16),
            nn.ReLU(),
            nn.Linear(16,1)
        )

    def forward(self, x):
        
        x = self.full(x)

        return x

def save_model(model, filename, args=[], kwargs={}):

    model_cpu = deepcopy(model).cpu()
    
    state = {'module_path': inspect.getmodule(model, _filename=True).__file__,
             'class_name': model.__class__.__name__,
             'state_dict': model_cpu.state_dict(),
             'args': args,
             'kwargs': kwargs}

    with open(filename, 'wb') as f:
        pickle.dump(state, f)

check_net = Net()
true_net = Net(seed=10)

a = -2.0
b = 3.0

x = []
y = []

x = [i/10 for i in range(300)]

for i in x:
    y += [a*i+b]

data_x = np.array(x)
data_y = np.array(y)

num_epochs = 10000

x_tensor = torch.from_numpy(data_x.reshape(-1, 1)).float()
y_tensor = torch.from_numpy(data_y.reshape(-1, 1)).float()

true_net.train()

criterion = torch.nn.MSELoss()

optimizer = torch.optim.SGD(true_net.parameters(),lr = 0.001)

epoch_loss = []

for epoch in range(num_epochs):
    outputs = true_net(x_tensor)

    loss = criterion(outputs, y_tensor)

    optimizer.zero_grad()

    loss.backward()

    optimizer.step()

    epoch_loss.append(loss.data.numpy().tolist())

    if epoch % 100 == 0:
        print(f'epoch : {epoch}  loss : {epoch_loss[len(epoch_loss)-1]}')

epoch_loss = []

save_model(true_net, 'senkei.pkl')