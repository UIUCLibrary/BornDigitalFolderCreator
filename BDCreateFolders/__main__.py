import sys
import argparse
import os
import shutil


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("csvfile", help="csv file exported from Medusa")
    parser.add_argument("-d", "--destination", default=os.getcwd(), help="Destination for the folders to be generated. Default: current directory")

    return parser.parse_args()


def get_arg_errors(args):
    if not os.path.exists(args.csvfile):
        yield "Unable to find \"{}\"".format(args.csvfile)

    if not os.path.exists(args.destination):
        yield "Invalid destination \"{}\"".format(args.destination)
    raise StopIteration


def confirm(msg):
    while True:
        answer = input("{} [y/n]: ".format(msg)).lower()
        if answer == "yes" or answer == "y":
            return True
        elif answer == "no" or answer == "n":
            return False
        else:
            print("Invalid answer", file=sys.stderr)


def banner():
    print("Folder Creator")
    pass


def main():
    banner()
    args = get_args()
    errors = list(get_arg_errors(args))
    if errors:
        for error in errors:
            print(error)
        exit(1)

    data = csv_parser.bdCSV(args.csvfile)
    if data.errors:
        for error in data.errors:
            print(error, file=sys.stderr)
        exit(1)

    num_folders_created = 0
    for item in data:
        barcode = item.barcode
        num_disks = item.num_disks
        print("Generating folders for {} with {} disks.".format(barcode, num_disks))
        try:
            for new_dir in folder_makers.gen_package_folder_names(root=args.destination, barcode=barcode, num_disks=num_disks):
            # for new_dir in folder_makers.gen_package_folder_names(root=args.destination, barcode=barcode, num_disks=num_disks):
                if os.path.exists(new_dir):
                    if confirm("\"{}\" already exists. Do you wish overwrite it? Note: Overwriting will delete any files "
                               "currently in the folder".format(new_dir)):
                        shutil.rmtree(new_dir)
                    else:
                        continue
                print("Creating: {} ".format(new_dir))
                os.makedirs(new_dir)
                num_folders_created += 1
            print("")
        except KeyboardInterrupt:
            print("\nExiting")
            break
    print("Created {} folders".format(num_folders_created))



if __name__ == '__main__':
    import folder_makers
    import csv_parser
    main()
else:
    from . import folder_makers
    from . import csv_parser




