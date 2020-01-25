import os
import tarfile


def unzip_file(path_to_zip_file, directory_to_extract_to):

    if (path_to_zip_file.endswith("tar.gz")):
        tar = tarfile.open(path_to_zip_file)
        tar.extractall(directory_to_extract_to)
        tar.close()
        return True
    else:
        print("did NOT get a tar.gz file")
        return False


def test_unzip_tar_gz_file():
    zipped_file = "/home/guya/tarGzFolder/npt1800kvmpackage_76067.tar.gz"
    directory_to_extract_to = "/home/guya/tarGzFolder"
    private_dswp_out_file_path = "/home/guya/tarGzFolder/DSWP.out"
    extracted_folder_name = "kvmpackage"
    dst_path_of_private_dswp = os.path.join(directory_to_extract_to, extracted_folder_name)
    dst_path_of_private_dswp = os.path.join(dst_path_of_private_dswp, "image/DSWP.out")
    print("the private DSWP.out file will be copied as dst file name:" + dst_path_of_private_dswp)

    if not unzip_file(zipped_file, directory_to_extract_to):
        print("was unable to extract the tar.gz file")
    else:
        from shutil import copyfile
        copyfile(private_dswp_out_file_path, dst_path_of_private_dswp)


def remove_all_configured_interfaces():
    ip_addr = "172.30.86.12"
    line_with_interface_to_remove = "ge-ts10.2.1 Link encap:Ethernet  HWaddr f8:ec:5f:cd:45:08"
    pattern_to_look_1 = "ge-ts"
    pattern_to_look_2 = "xe-ts"
    if line_with_interface_to_remove.startswith(pattern_to_look_1) or \
        line_with_interface_to_remove.startswith(pattern_to_look_2):
        words_in_line = line_with_interface_to_remove.split(" ")
        interface_to_remove_name = words_in_line[0]
        print("the given line contains an interface to remove with name:" + words_in_line[0])
        cmd_to_remove_interface = "ip link delete " + interface_to_remove_name
        print("the command to use in order to remove the interface is:" + cmd_to_remove_interface)

remove_all_configured_interfaces()