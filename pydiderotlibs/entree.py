# -*- coding: utf-8 -*-

import tkinter as tk

print("""
Merci d'utiliser la librairie entree du module pydiderot.\n
N'hésitez pas à consulter la documentation en ligne:\n
https://pydiderotlibs.rtfd.io/librairies/entree.html
""")


def demander_texte(titre="Entrez un texte", message=None):
    """
    Ouvre une fenêtre avec le titre "titre" et attend une chaine de caractères.

    Arguments:
        titre (str, optionnel): Le titre de la fenetre (``"Entrez un texte"`` par défaut).
        message (str, optionnel): Si présent, on ajoute un champ de texte contenant ``message``.

    Returns:
        La chaine de caractère (type ``str``) entrée par l'utilisateur.
    """

    def _sauver_valeur(event=None):
        """
        Si entree est non vide, la fonction sauve sa valeur dans value et ferme la fenetre
        """
        if entree.get():
            value.set(entree.get())
            fenetre.destroy()

    fenetre = tk.Tk()
    fenetre.title(titre)

    # Si message est entré, on ajoute un champ message.
    # permet par exemple l'affichage d'érreurs.
    if message is not None:
        label = tk.Label(fenetre, text=message)
        label.pack()

    value = tk.StringVar()

    entree = tk.Entry(fenetre, textvariable=value, width=50)
    entree.pack()
    # la touche retour appelle _sauver_valeur
    entree.bind('<Key-Return>', _sauver_valeur)
    # Donne le focus à la fenetre et au widget entree
    # Peut-etre focus_set serait plus poli?
    # http://tkinter.fdex.eu/doc/uwm.html#focus_set
    # http://tkinter.fdex.eu/doc/uwm.html#focus_force
    entree.focus_force()

    bouton = tk.Button(fenetre, text='Valider', command=_sauver_valeur)
    bouton.pack()
    fenetre.mainloop()
    return value.get()


def demander_reel(titre="Entrez un nombre réel"):
    """Ouvre une fenetre et attend un nombre réel.

    Si ce n'est pas un nombre réel, on repose la question en ajoutant un message d'erreur.

    Arguments:
        titre (str, optionnel): Titre de la fenetre (``"Entrez un nombre réel"`` par défaut).

    Returns:
        Le nombre réel entré par l'utilisateur (type ``float``).
    """
    message = None
    while True:
        texte = demander_texte(titre, message)
        # Si texte est vide, l'utilisateur à fermé la fenetre
        if not texte:
            return
        # Tente de convertir en float
        try:
            reel = float(texte)
        except ValueError:
            message = "La donnée est incorrecte. Ce n'est pas un nombre"
            continue
        else:
            break
    return reel


def demander_entier(titre="Entrez un nombre entier"):
    """Ouvre une fenetre et attend un nombre entier.

    Si ce n'est pas un nombre entier, on repose la question en ajoutant un message d'erreur.

    Arguments:
        titre (str, optionnel): Titre de la fenêtre (``"Entrez un nombre entier"`` par défaut).

    Returns:
        Le nombre entier entré par l'utilisateur (type ``int``).
    """
    message = None
    while True:
        texte = demander_texte(titre, message)
        # si texte est vide, cela veut dire que l'utilisateur à fermé la fenêtre
        if not texte:
            return
        # on essaye de convertir en int
        try:
            entier = int(texte)
        except ValueError:
            message = "La donnée est incorrecte. Ce n'est pas un nombre ENTIER"
            continue
        else:
            break
    return entier
