import logging


def log(file_name='log',
        module_name='logger',
        info_type='info',
        *args, **kwargs):
    logger = logging.getLogger(module_name)
    if info_type == 'info':
        logger.info('module is :%s' % module_name + str(args))
    if info_type == 'debug':
        logger.debug('module is :%s' % module_name + str(args))
    if info_type == 'error':
        logger.error('module is :%s' % module_name + str(args))
    with open(file_name, 'a+') as f:
        f.writelines('module is :%s' % module_name, args)
    