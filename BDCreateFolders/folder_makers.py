import platform
import os


def get_disk_paths(new_dir_name):
    yield os.path.join(new_dir_name, "ImageCapturedFromDisk")
    objectDocDir = os.path.join(new_dir_name, "ObjectDocumentation")
    yield objectDocDir
    yield os.path.join(objectDocDir, "ObjectJPG")
    yield os.path.join(new_dir_name, "OriginalFiles")


def gen_package_folder_names(root, barcode:int, num_disks:int):
    new_dir_name = os.path.join(root, str(barcode))
    yield new_dir_name
    for disk_number in range(num_disks):
        disk_dir = os.path.join(new_dir_name, str(disk_number + 1).zfill(3))
        yield disk_dir

        for new_path in get_disk_paths(disk_dir):
            yield new_path

    pass


# TODO DELETE THIS
def show_dir(root):
    for root, dirs, files in os.walk(root):
        for _file in files + dirs:
            print(os.path.join(root, _file))



