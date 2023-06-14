import sys
import os
from dcws.config import settings
from dcws.secrets_loader import enc, new_key, enc_with_key


def _bootstrap():
    key = new_key()
    print(key)
    print(enc_with_key(key, 'test value'))


def main():
    """
    Main application driver.
    """

    if len(sys.argv) == 2 and sys.argv[1] == '-b':
        # If the command line parameter is -b, then bootstrap the application.
        _bootstrap()
    else:
        # Otherwise, read the decrypt key from standard input and print out the properties.
        key = input()
        os.environ['DYNACONF_DECRYPT_KEY'] = key
        print(settings.app.property)
        print(settings.secret)


if __name__ == '__main__':
    main()
