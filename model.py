import os
import glob
from posixpath import basename
import sklearn as sk
from sklearn.model_selection import train_test_split
import shutil
import tensorflow as tf

def split_data (path_to_data , path_to_save_train , path_to_save_valid , split_size = 0.1):

    folders = os.listdir(path_to_data)

    for folder in folders:

        full_path = os.path.join(path_to_data , folder)
        images_path = glob.glob(os.path.join(full_path , '*.png')) #importing only .png files(images)

        x_train , x_val = train_test_split(images_path , test_size = split_size)

        for x in x_train:
            ##features = tf.layers.batch_normalization(##)
            path_to_folder = os.path.join(path_to_save_train , folder)

            if not os.path.isdir(path_to_folder):
                os.makedirs(path_to_folder)

            shutil.copy(x , path_to_folder)

        for x in x_val:
            path_to_folder = os.path.join(path_to_save_valid, folder)

            if not os.path.isdir(path_to_folder):
                os.makedirs(path_to_folder)

            shutil.copy(x, path_to_folder)


if __name__ == "__main__":
    path_to_data = "D:\\Traffic_sign_recognition\\archive (1)\\Train"
    path_to_save_train = "D:\\Traffic_sign_recognition\\archive (1)\\training_data\\Train"
    path_to_save_valid = "D:\\Traffic_sign_recognition\\archive (1)\\training_data\\Val"
    split_data(path_to_data = path_to_data , path_to_save_train = path_to_save_train , path_to_save_valid = path_to_save_valid)
   
    



