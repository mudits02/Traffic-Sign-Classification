import os
import glob
from posixpath import basename
import sklearn as sk
from sklearn.model_selection import train_test_split
import shutil
import tensorflow as tf
from my_utils import split_data


if __name__ == "__main__":
    path_to_data = "D:\\Traffic_sign_recognition\\archive (1)\\Train"
    path_to_save_train = "D:\\Traffic_sign_recognition\\archive (1)\\training_data\\Train"
    path_to_save_valid = "D:\\Traffic_sign_recognition\\archive (1)\\training_data\\Val"
    split_data(path_to_data = path_to_data , path_to_save_train = path_to_save_train , path_to_save_valid = path_to_save_valid)
   
    



