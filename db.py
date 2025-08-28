from utils.random import random

import os
import time
import pickle
import shutil
import fnmatch


class Manager:
    def __init__(self, index, generate_only, output_dir=None, file_extension=".html"):
        self.generate_only = generate_only
        self.index = index
        self.file_extension = file_extension
        self.file_counter = 0

        if generate_only:
            if os.path.exists(output_dir):
                shutil.rmtree(output_dir)
            os.mkdir(output_dir)
            self.output_dir = output_dir
        else:
            pass

    def fn(self):
        self.file_counter += 1
        return "{}-{}-{}".format(self.index, int(time.time() * 100), self.file_counter)

    def save_testcase(self, document, cov=None):
        if self.generate_only:
            path = os.path.join(self.output_dir, "{}{}".format(self.fn(), self.file_extension))
            with open(path, "w") as f:
                f.write(str(document))
        else:
            pass
