################################
# collate batch and return a batch in the shape of (B, C, H, W)
################################
import numpy as np


class Dataset():
    def __init__(self):
        self.batch_size = 2
        self.img_ids = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg']

    def load_img(self, img_id):
        # print(img_id)
        width = np.random.randint(64) + 1
        img = np.random.rand(3, 64, width)
        return img

    def generate_batch(self):
        '''
        :param batch_size: int>0
        :return: a list of images in the shape of (C, H, W)
        '''
        batch = []
        imgs = self.img_ids[:self.batch_size]
        for img_id in imgs:
            img = self.load_img(img_id)
            batch.append(img)
        return batch

    def __call__(self, *args, **kwargs):
        batch = self.generate_batch()
        # collate batch and return a batch in the shape of (B, C, H, W)
        print(len(batch))
        return self.collate_batch(batch)

    def collate_batch(self, batch):
        B, C, H = len(batch), batch[0].shape[0], batch[0].shape[1]

        max_width = 0
        width = []

        for b in range(B):
            w = batch[b].shape[2]
            width.append(w)

        max_width = np.max(width)

        collated = []
        for img in batch:
            C, H, W = img.shape
            final_dim = np.zeros((C, H, max_width))

            final_dim[:, :, :W] = img[:, :, :]

            img = final_dim

            collated.append(img)

        return collated


data = Dataset()

batch = data.generate_batch()

print(len(batch), batch[0].shape, batch[1].shape)

collated = data.__call__()

print(collated[0].shape, collated[1].shape)










