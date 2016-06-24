# -*- coding: utf8 -*-
import shutil
import var

if __name__ == '__main__':
    shutil.make_archive("a", 'zip', var.TEST_SUITE_LOG_PATH)
