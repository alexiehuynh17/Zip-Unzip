# Zip-Unzip
## How to use zip and unzip python code


### **Zip code**
Example command: `python -m zip --dir_path me/media/ --save_path run/ --file_type pdf html`

Attributes:

* `--dir_path`: Directory path need to zip (required).
* `--save_path`: Directory path to save zip.
* `--file_type`: Zip only type of files (default: all file).
* `--save_stage`: Save stage when crash zip happened (default: not save).


### **Unzip code**
Example command: `python -m unzip --zip_path run/media/media.zip --save_path run/test/`

Attributes:

* `--zip_path`: Directory path need to be unzipp (required).
* `--save_path`: Directory path need to store zip.
* `--is_file`: Is zip file {0,1} (default: 1).
* `--is_folder`: Folder include zip file {0,1} (default: 0).
* `--combine`: combine all zip file {0,1} (default: 0) (**_Not recommend for normal user_ CVAT YOLO 1.1 only**).
