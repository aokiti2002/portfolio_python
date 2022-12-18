import random
from matplotlib import pyplot as plt
import numpy as np
import torch
import joblib
import pickle
from importlib import machinery

def load_model(filename):
    
    with open(filename, 'rb') as f:
        state = pickle.load(f)

    module = machinery.SourceFileLoader(state['module_path'], state['module_path']).load_module()
    args, kwargs = state['args'], state['kwargs']
    model = getattr(module, state['class_name'])(*args, **kwargs)
    model.load_state_dict(state['state_dict'])

    return model

a = -2.0
b = 3.0

x = []
y = []

x = [i/10 for i in range(300)]

for i in x:
    y += [a*i+b+random.uniform(-0.5,0.5)]


true_net = load_model('senkei.pkl')

true_net.eval()

x_test = np.linspace(0, 30, 200)
x_test_tensor = torch.from_numpy(x_test.reshape(-1,1)).float()

with torch.no_grad():
    y_pred_tensor = true_net(x_test_tensor)

y_pred = y_pred_tensor.data.numpy()

plt.scatter(x,y)
plt.plot(x_test, y_pred, c='orange')
plt.show()



