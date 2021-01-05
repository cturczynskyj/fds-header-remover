import os
import shutil

rom_folder = 'fds_roms'
headerless_folder = 'headerless_roms'

"""
parse params for fds roms foler
"""

for subdir, dirs, files in os.walk(rom_folder):
    for file_name in files:

        # don't process any non-fds files
        if not file_name.endswith(".fds"):
            continue

        # path for unmodified files
        file_path = os.path.join(subdir, file_name)

        truncated_data = None
        with open(file_path, mode='rb') as file:
            # read first 16 bytes (the header)
            data = file.read(16)
            string_content = "".join(map(str, data))

            if string_content.startswith('FDS'):
                # if the first 16 bytes starts with FDS then there is a header
                # so let's populate the truncated_data with the rest of the file
                truncated_data = file.read()

        # get path to write to
        path = subdir.split(os.sep)
        headerless_path = os.path.join(headerless_folder, file_name)
        if len(path) != 0:
            headerless_path = os.path.join(headerless_folder, os.sep.join(path[1:]), file_name)

        # create directories for file
        directory_to_write_to = os.path.dirname(headerless_path)
        if not os.path.exists(directory_to_write_to):
            try:
                os.makedirs(directory_to_write_to)
            except OSError as exc:
                if exc.errno != errno.EEXIST:
                    raise

        if truncated_data is not None:
            print("Writing with removed header: " + headerless_path)

            # write the file with first 16 bytes removed
            with open(headerless_path, mode='wb') as writer:
                writer.write(truncated_data)
        else:
            print("No header found, copying: " + headerless_path)

            # just copy the file to the headerless folder
            shutil.copyfile(file_path, headerless_path)
