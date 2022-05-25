import os
import zipfile
import argparse
from numpy import single
from tqdm import tqdm
from os.path import basename, dirname, join
import datetime
import hashlib
import shutil


def process_file(save_path):
    folder_names = os.listdir(save_path)
    for name in folder_names:
        with open(join(join(save_path,name), 'train.txt' ), 'r') as f:
            filename = [basename(x).replace('.PNG\n','') for x in f.readlines()]
        for file in filename:
            src_img =  join(join(save_path,name), f'obj_train_data/{file}.PNG')
            src_txt =  join(join(save_path,name), f'obj_train_data/{file}.txt')
            dst_img = join(save_path, 'all')
            x = datetime.datetime.now()
            dati = str(x.date())+ '_' + str(x.time())
            hash_name = hashlib.md5(f'{name}_{dati}'.encode("utf-8")).hexdigest()
            if not os.path.isdir(join(save_path, 'all')):
                os.mkdir(join(save_path, 'all'))
            dst_img = join(save_path, f'all/{hash_name}.PNG')
            dst_txt = join(save_path, f'all/{hash_name}.txt')
            shutil.copy2(src_img, dst_img)
            shutil.copy2(src_txt, dst_txt)
    

def unzipdir(zip_path, save_path, is_file, is_folder, combine):
    if is_folder == 1:
        zip_files = os.listdir(zip_path[0])
        for file in tqdm(zip_files):
            if file.endswith('.zip'):
                fzip_path = join(zip_path[0], file)
                with zipfile.ZipFile(fzip_path, 'r') as zip_ref:
                    zip_ref.extractall(join(save_path, file.replace('.zip','')))
    elif is_file == 1:
        for x in zip_path:
            with zipfile.ZipFile(x, 'r') as zip_ref:
                zip_ref.extractall(join(save_path, basename(x).replace('.zip','')))
    if combine == 1:
        process_file(save_path)

def main(zip_path, save_path, is_file=1, is_folder=0, combine=0):
    unzipdir(zip_path, save_path, is_file, is_folder,combine)
    

if __name__ == '__main__':
    # python -m unzip --zip_path run/media/media.zip --save_path run/test/
    parser = argparse.ArgumentParser()
    parser.add_argument('--zip_path', nargs='+', type=str, required=True, help='Directory path need to be unzip')
    parser.add_argument('--save_path', type=str, default='', help='Directory path need to store zip')
    parser.add_argument('--is_file', default=1, type=int, help='is zip file')
    parser.add_argument('--is_folder', default=0, type=int, help='Folder include zip file')
    # Not recommend for normal user (CVAT YOLO 1.1)
    parser.add_argument('--combine', default=0, type=int, help='Combine all image to one folder')
    opt = parser.parse_args()
    main(**vars(opt))