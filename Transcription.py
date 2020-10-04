'''
A simple Gooey example. One required field, one optional.
'''

from gooey import Gooey, GooeyParser

import test


@Gooey()
def main():
    parser = GooeyParser(description='Transcribe/translate audio.')

    parser.add_argument(
        'required_field',
        metavar='Language',
        help='Choose the language for the output text in the drop-down menu.')

    parser.parse_args()
    test.main()
    print('Transcription complete!')


if __name__ == '__main__':
    main()
