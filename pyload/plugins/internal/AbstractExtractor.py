# -*- coding: utf-8 -*-


from __future__ import unicode_literals
class ArchiveError(Exception):
    pass


class CRCError(Exception):
    pass


class WrongPassword(Exception):
    pass


class AbtractExtractor:

    __version__ = "0.1"

    @staticmethod
    def checkDeps():
        """ Check if system satisfies dependencies
        :return: boolean
        """
        return True

    @staticmethod
    def getTargets(files_ids):
        """ Filter suited targets from list of filename id tuple list
        :param files_ids: List of file paths
        :return: List of targets, id tuple list
        """
        raise NotImplementedError

    def __init__(self, m, file, out, fullpath, overwrite, excludefiles, renice):
        """Initialize extractor for specific file

        :param m: ExtractArchive addon plugin
        :param file: Absolute file path
        :param out: Absolute path to destination directory
        :param fullpath: Extract to fullpath
        :param overwrite: Overwrite existing archives
        :param renice: Renice value
        """
        self.m = m
        self.file = file
        self.out = out
        self.fullpath = fullpath
        self.overwrite = overwrite
        self.excludefiles = excludefiles
        self.renice = renice
        self.files = []  #: Store extracted files here

    def init(self):
        """ Initialize additional data structures """
        pass

    def checkArchive(self):
        """Check if password is needed. Raise ArchiveError if integrity is
        questionable.

        :return: boolean
        :raises ArchiveError
        """
        return False

    def checkPassword(self, password):
        """ Check if the given password is/might be correct.
        If it can not be decided at this point return true.

        :param password:
        :return: boolean
        """
        return True

    def extract(self, progress, password=None):
        """Extract the archive. Raise specific errors in case of failure.

        :param progress: Progress function, call this to update status
        :param password password to use
        :raises WrongPassword
        :raises CRCError
        :raises ArchiveError
        :return:
        """
        raise NotImplementedError

    def getDeleteFiles(self):
        """Return list of files to delete, do *not* delete them here.

        :return: List with paths of files to delete
        """
        raise NotImplementedError

    def getExtractedFiles(self):
        """Populate self.files at some point while extracting"""
        return self.files
