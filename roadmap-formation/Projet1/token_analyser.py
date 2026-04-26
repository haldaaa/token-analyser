import argparse
from pathlib import Path 


def count_chars(text):

    return len(text)


def count_words(text):

    return len(text.split())


def main():

    # Création du parser :
    parser = argparse.ArgumentParser(description="Lancer la commande avec --text 'votre text' pour analyser votre texte en argument...")
  
    # Création du groupe parseur :
    group = parser.add_mutually_exclusive_group(required=True)

    # Ajout des argument du groupe, soit file soit text :
    group.add_argument("--text", help="help pour le texte")
    group.add_argument("--file", help="help pour le file")

    # On parse (on check le contenue de argument)
    args = parser.parse_args()

    # If :

    if args.text:
        contenu = args.text
    else:
        contenu = Path(args.file).read_text(encoding="utf-8")

    print("Nombre de caractéres:", count_chars(contenu))
    print("Mots:", count_words(contenu))


if __name__ == "__main__":
    main()


