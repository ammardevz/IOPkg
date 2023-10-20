import os
import struct
from datetime import datetime

import base


class Packager:
    def __init__(self):
        self._pkg_data = []
        self.version = '1.0'

    def add(self, path):
        if not os.path.exists(path):
            return
        if os.path.isfile(path):
            self.__add_file__(path)
        elif os.path.isdir(path):
            self.__add_dir__(path)
        else:
            raise ValueError(f"The path '{path}' could not be found or is not a valid file or directory.")

    def __add_file__(self, path):
        file_info = base.File()
        with open(path, "rb") as file:
            content = file.read()

        file_info.content = content
        file_info.size = os.path.getsize(path)
        file_info.filename = os.path.basename(path)

        self._pkg_data.append(file_info)

    def __add_dir__(self, path):
        for root, dirs, files in os.walk(path):
            for filename in files:
                file_path = os.path.join(root, filename)
                relative_path = os.path.relpath(file_path, path)
                pkg_filename = os.path.join(relative_path.replace(os.sep, "/"))

                file_info = base.File()
                with open(file_path, "rb") as file:
                    content = file.read()

                file_info.content = content
                file_info.size = os.path.getsize(file_path)
                file_info.filename = pkg_filename

                self._pkg_data.append(file_info)

    def exportPkg(self, out, author=None):
        files_count = len(self._pkg_data)
        now = datetime.today()
        formatted_date = now.strftime("%Y-%m-%d %H:%M")
        if author is None:
            author = os.getlogin()
        with open(out, "wb") as file:
            file.write(struct.pack("<I", files_count))

            file.write(struct.pack("<I", len(self.version)))
            file.write(self.version.encode("utf-8"))

            file.write(struct.pack("<I", len(formatted_date)))
            file.write(formatted_date.encode("utf-8"))

            file.write(struct.pack("<I", len(author)))
            file.write(author.encode("utf-8"))

            for file_info in self._pkg_data:
                file.write(struct.pack("<I", len(file_info.filename)))
                file.write(file_info.filename.encode("utf-8"))

                file.write(struct.pack("<I", file_info.size))

                file.write(struct.pack("<Q", len(file_info.content)))
                file.write(file_info.content)

    @staticmethod
    def extractPkgInfo(_input):
        with open(_input, 'rb') as file:
            files_count = struct.unpack("<I", file.read(4))[0]

            packager_version_version = struct.unpack("<I", file.read(4))[0]
            packager_version = file.read(packager_version_version).decode('utf-8')

            creation_date_length = struct.unpack("<I", file.read(4))[0]
            creation_date = file.read(creation_date_length).decode('utf-8')

            author_length = struct.unpack("<I", file.read(4))[0]
            author = file.read(author_length).decode('utf-8')

            file_infos = []
            for _ in range(files_count):
                file_info = base.File()

                filename_length = struct.unpack("<I", file.read(4))[0]
                file_info.filename = file.read(filename_length).decode("utf-8")

                file_info.size = struct.unpack("<I", file.read(4))[0]
                content_length = struct.unpack("<Q", file.read(8))[0]
                file_info.content = file.read(content_length)

                file_infos.append(file_info)

            return author, file_infos, {"date": creation_date, "version": packager_version}
