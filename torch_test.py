import torch
print(f"{torch.cuda.is_available()}")
print(F"{torch.cuda.current_device()}")
print(torch.cuda.device_count())