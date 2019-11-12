import logging

def log_error(message):
    logging.error(message)


def log_file_already_existed(file_name):
    message = 'file with name %s already existed' % file_name
    log_error(message)


def log_info(message):
    logging.info(message)


def log_repo_start_to_clone(repo_name, dest):
    message = 'rep with name %(repo_name)s start clone to dest %(dest)s' \
        % {'repo_name': repo_name, 'dest': dest}
    log_info(message)