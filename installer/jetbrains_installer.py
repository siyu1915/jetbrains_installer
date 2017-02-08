import os, sys, tarfile, glob


def extract(tar_path, extract_path="."):
    print("Extract " + tar_path + " to " + extract_path)
    tar = tarfile.open(tar_path, 'r')
    tar.extractall(path=extract_path)
    tar.close()


try:
    print("Welcome to Jetbrains Installer!")
    print("By siyu1915, https://www.github.com/siyu1915/")
    tar_files = glob.glob("./*.tar.gz")
    print("Input your extract path, enter . to extract current dir:")
    extract_path = input()
    print("Extract path: " + extract_path)
    print("Found these files(.tar.gz) in your directory:")
    for tar_file in tar_files:
        print("\t" + tar_file)
        extract(tar_file, extract_path)
except tarfile.TarError:
    print()
