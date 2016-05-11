import logging


class Logging(object):
    logging.basicConfig(level=logging.DEBUG, \
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s', \
                        datefmt='%m-%d %H:%M', \
                        filename='myapp.log', filemode='w')

    def create_logger(self, name, folder_path, logger_name):
        logger = logging.getLogger(name)
        log_file_full_name = folder_path + "//" + logger_name

        # writes formatted logging records to disk files
        file_handler = logging.FileHandler(log_file_full_name)
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        file_handler.setFormatter(formatter)

        # write formatted logging records to console
        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)
        console.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console)
        logger.setLevel(logging.WARNING)

        return logger, log_file_full_name