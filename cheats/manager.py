""" Cheats manager module """

import os
import errno
import glob2


class CheatsManager(object):
    """ Class that manages the cheat sheets """

    def __init__(self, cheats_dir):
        """ Constructor method"""
        self.cheats_dir = cheats_dir
        self.create_default_cheats_dir()

    def find(self, query=None):
        """ Llooks for a cheat sheet, optionally filtered by the query argument """

        files = glob2.glob('%s/**/*' % self.cheats_dir)
        result = []
        for file_path in files:
            filename = os.path.basename(file_path)
            filename_without_ext = os.path.splitext(
                filename)[0].replace('-', ' ').title()

            if not os.path.isfile(file_path):
                continue
            if query and query.lower() not in filename.lower():
                continue

            result.append({
                'path': file_path,
                'name': filename,
                'normalized_name': filename_without_ext
            })

        return result

    def create_default_cheats_dir(self):
        """ creates the cheats dir if it does not exist """
        try:
            os.makedirs(self.cheats_dir)
        except OSError as exc:
            if exc.errno == errno.EEXIST and os.path.isdir(self.cheats_dir):
                pass
            else:
                raise

    def set_cheats_dir(self, path):
        """ Sets the cheats dir, overriding the default one """
        self.cheats_dir = path