import sys

def main(**kwargs):
    """
    This script provides basic structure to retrieve data from different databases, to look into one, you may use the following parameters:

        [-db]   database to look into (UniProt, KEGG, RCSB, ChEMBL, BRENDA)

        [-met]  target metabolite (metabolite name or ID from database)
    """

    if len(kwargs) == 0 or kwargs.get('-help') or kwargs.get('-h'):
        print(main.__doc__)
        return

    match kwargs['-db']:
        case "UniProt":
            import uniprot
            uniprot.fetch(kwargs.get('-met'))
        case "KEGG":
            import kegg
            kegg.fetch(kwargs.get('-met'))
        case "RCSB":
            import rcsb
            rcsb.fetch(kwargs.get('-met'))
        case "ChEMBL":
            import chembl
            chembl.fetch(kwargs.get('-met'))
        case "BRENDA":
            import brenda
            brenda.fetch(kwargs.get('-met'))

if __name__ == "__main__":
    # pass to main -key=value, if no value provided, assign -key=True
    main(**{arg.split('=')[0]: arg.split('=')[1] if '=' in arg else True for arg in sys.argv[1:]})
