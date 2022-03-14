import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import glob
import shutil
from sklearn.model_selection import train_test_split
import csv

def image_display(examples, labels):

    plt.figure(figsize=(10, 10))

    for i in range(25):

        index = np.random.randint(0, examples.shape[0] - 1)
        label = labels[index]
        img = examples[index]
        plt.subplot(5, 5, i + 1)
        plt.title(str(label))
        plt.tight_layout()
        plt.imshow(img, cmap='gray')

    plt.show()


def split_data(path_to_data, path_to_save_train, path_to_save_valid, split_size=0.1):

    folders = os.listdir(path_to_data)

    for folder in folders:

        full_path = os.path.join(path_to_data, folder)
        # importing only .png files(images)
        images_path = glob.glob(os.path.join(full_path, '*.png'))

        x_train, x_val = train_test_split(images_path, test_size=split_size)

        for x in x_train:
            ##features = tf.layers.batch_normalization(##)
            path_to_folder = os.path.join(path_to_save_train, folder)

            if not os.path.isdir(path_to_folder):
                os.makedirs(path_to_folder)

            shutil.copy(x, path_to_folder)

        for x in x_val:
            path_to_folder = os.path.join(path_to_save_valid, folder)

            if not os.path.isdir(path_to_folder):
                os.makedirs(path_to_folder)

            shutil.copy(x, path_to_folder)


def test_set(path_to_test , path_to_csv):

    testset = {}

    try:
        with open(path_to_csv , 'r') as csvfiles:
            
            
