import os, sys, tarfile, glob


def extract(tar_path, extract_path="."):
    print("Extract " + tar_path + " to " + extract_path)
    tar = tarfile.open(tar_path, 'r')
    tar.extractall(path=extract_path)
    tar.close()


def for_extract(tar_files1, extract_path1):
    for tar_file1 in tar_files1:
        print("\t" + tar_file1)
        extract(tar_file1, extract_path1)


try:
    print("Welcome to Jetbrains Installer!")
    print("By siyu1915, https://www.github.com/siyu1915/")

    tar_files = glob.glob("./*.tar.gz")
    print("Input your extract path, enter . to extract current dir:")
    extract_path = input()
    file_count = len(tar_files)
    extracting_count = 1
    print("Found " + str(file_count) + " files(.tar.gz) in your directory:")

    if file_count == 0:
        quit()

    for tar_file in tar_files:
        print("\t" + tar_file)

    while True:
        print("Are you sure you want to extract these files?[Y/n]")
        i = input()
        if i == "Y" or "y":
            for_extract(tar_files, extract_path)
            print("------------------------------")
            print("Extracted " + str(file_count) + " file(s) to " + extract_path)
            break
        elif i == "N" or "n":
            print("Exited.")
            break
        else:
            continue



except tarfile.TarError:
    print("Cannot extract files!")
