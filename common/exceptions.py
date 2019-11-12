import six
import logging


class BaseExcep(Exception):
    msg_fmt = 'An unknown exception occured.'


    def __init__(self, message=None, **kwargs):
        self.kwargs = kwargs

        try:
            if not message:
                message = self.msg_fmt % kwargs
            else:
                message = six.text_type(message)
        except KeyError:
            logging.error('failed to render message: %s with keywords: %s'
                          % (self.msg_fmt, str(kwargs)))


class FileNotExists(BaseExcep):
    msg_fmt = 'file with name: %(file_name)s not exists.'


class FileNameMustBeString(BaseExcep):
    def __init__(self):
        message = 'file name must be string'
        super(BaseExcep, self).__init__(message=message)

class DirectoryExists(BaseExcep):
    msg_fmt = 'directory with name: %(directory_name)s already exists.'