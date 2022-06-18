import torch

criterion = torch.nn.KLDivLoss(reduction='mean')

output = torch.rand(4, 3, 32, 32)
target = torch.rand(4, 3, 32, 32)

loss = criterion(output, target)
print(loss)