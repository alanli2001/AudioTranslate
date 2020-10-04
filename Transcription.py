from gooey import Gooey, GooeyParser
import test


@Gooey()
def main():
    parser = GooeyParser(description='Transcribe/translate audio.')

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-en", "--English", action="store_true")
    group.add_argument("-hi", "--Hindi", action="store_true")
    group.add_argument("-es", "--Spanish", action="store_true")
    group.add_argument("-fr", "--French", action="store_true")
    group.add_argument("-ar", "--Arabic", action="store_true")
    group.add_argument("-bn", "--Bengali", action="store_true")
    group.add_argument("-ru", "--Russian", action="store_true")
    group.add_argument("-pt", "--Portuguese", action="store_true")
    group.add_argument("-id", "--Indonesian", action="store_true")
    args = parser.parse_args()

    def run():
        if args.English:
            test.main("en")
        elif args.Hindi:
            test.main("hi")
        elif args.Spanish:
            test.main("es")
        elif args.French:
            test.main("fr")
        elif args.Arabic:
            test.main("ar")
        elif args.Bengali:
            test.main("bn")
        elif args.Russian:
            test.main("ru")
        elif args.Portuguese:
            test.main("pt")
        elif args.Indonesian:
            test.main("id")
        else:
            test.main("en")
    run()
    print('Transcription complete!')


if __name__ == '__main__':
    main()
