from tsotmkvlib import cavlog, cavsys


def main():
    """
    Main Program loop
    :return:
    """

    log = cavlog.build_cavlog('DEBUG')
    cavsys.check_py_version()


if __name__ == '__main__':
    main()
else:
    exit(1)
