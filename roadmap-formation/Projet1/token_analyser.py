import argparse
from pathlib import Path 
import tiktoken 


def count_chars(text):

    return len(text)


def count_words(text):

    return len(text.split())


def count_token(text, tokenizer_name):

    encode = tiktoken.get_encoding(tokenizer_name)
    return len(encode.encode(text))



def main():

    # Création du parser :
    parser = argparse.ArgumentParser(description="Lancer la commande avec --text 'votre text' pour analyser votre texte en argument...")
  
    # Création du groupe parseur :
    group = parser.add_mutually_exclusive_group(required=True)

    # Ajout des argument du groupe, soit file soit text :
    group.add_argument("--text", help="help pour le texte")
    group.add_argument("--file", help="help pour le file")

    # Ajout pour token:

    parser.add_argument(
        "--tokenizer",
        default="cl100k_base",
        choices=["cl100k_base", "o200k_base"],
        help="Tokenizer à utiliser"
    )

    # On parse (on check le contenue de argument)
    args = parser.parse_args()

    # If :

    if args.text:
        contenu = args.text
    else:
        contenu = Path(args.file).read_text(encoding="utf-8")

    print("Nombre de caractéres:", count_chars(contenu))
    print("Mots:", count_words(contenu))
    print(f"Token({args.tokenizer}):", count_token(contenu, args.tokenizer))


if __name__ == "__main__":
    main()


