import os
import zipfile
import argparse
from tqdm import tqdm
from os.path import basename, dirname, join


def zipdir(path, ziph, run_path, ftype, save_stage):

    if save_stage:
        if not os.path.exists(run_path + '/status.txt'):
            with open(run_path + '/status.txt', 'w'): pass

        have_zip = []
        with open(run_path + '/status.txt', "r") as f:
            have_zip = [x.replace('\n', '') for x in f.readlines()]

        now_zip = []
        f = open(run_path + '/status.txt', "a")

        for root, dirs, files in tqdm(os.walk(path)):
            tmp_root = root.replace(path, '')
            if tmp_root not in now_zip and tmp_root not in have_zip:
                now_zip.append(tmp_root)
                if tmp_root != '':
                    f.write(tmp_root + '\n')
                for file in files:
                    if any(file.endswith(f'.{x}') for x in ftype) == True or ftype[0] == 'all':
                        ziph.write(join(root, file), 
                            os.path.relpath(join(root, file), 
                                            join(path, '..')))

        f.close()
    else:
         for root, dirs, files in tqdm(os.walk(path)):
            for file in files:
                if any(file.endswith(f'.{x}') for x in ftype) == True or ftype[0] == 'all':
                    ziph.write(join(root, file), 
                        os.path.relpath(join(root, file), 
                                        join(path, '..')))

def main(dir_path, save_path, file_type, save_stage):
    # run_path = join(save_path, f"{basename(dirname(dir_path))}")
    run_path = join(save_path, "")
    if run_path != '' and not os.path.isdir(run_path):
        os.mkdir(run_path)
    out_path = basename(dirname(dir_path))
    with zipfile.ZipFile(join(f'{run_path}',f'{out_path}.zip'), 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipdir(dir_path, zipf, run_path, file_type, save_stage)

if __name__ == '__main__':
    # Example: python -m zip --dir_path me/media/ --file_type pdf html
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir_path', type=str, required=True, help='Directory path need to zip')
    parser.add_argument('--save_path', type=str, default='', help='Directory path to save zip')
    parser.add_argument('--file_type', nargs='+', default=['all'], type=str, help='Zip only type')
    parser.add_argument('--save_stage', default=False, action='store_true', help='Save stage when crash zip')
    opt = parser.parse_args() 
    main(**vars(opt))
