from torch import nn


class ShuffleNet(nn.Module):
    def __init__(self, g):
        super(ShuffleNet, self)
        self.num_groups = g

    def forward(self, x):
        B, C, H, W = x.shape

        x = x.reshape(B, g, -1, H, W)

        x = x.permute(0, 2, 1, 3, 4)

        x = x.reshape(B, C, H, W)

        return x