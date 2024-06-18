import torch
from matplotlib import pyplot as plt

pose_path = '/home/yugrp01/CF-3DGS/output/progressive/data_museum/pose/ep00_init.pth'

data = torch.load(pose_path)
print(data.keys())
print(len(data['poses_pred'].tolist()))
x = []
y = []
z = []
for pose in data['poses_pred'].tolist():
    x.append(pose[0][3])
    y.append(pose[1][3])
    z.append(pose[2][3])

# 可视化xyz
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z)
plt.show()