from tsotmkvlib import cavlog


def main():
    """
    Main Program loop
    :return:
    """

    log = cavlog.build_cavlog('DEBUG')
    log.info("Log file initialized")
    # TODO check version of Python


if __name__ == '__main__':
    main()
else:
    exit(1)
