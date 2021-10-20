from COE.UI.UI_Fenetre import Fenetre


def main(istest=False):
    fenetre = Fenetre()
    while fenetre.get_loop():
        fenetre.menu.loop = not istest
        fenetre.display(istest)


if __name__ == "__main__":
    main()
