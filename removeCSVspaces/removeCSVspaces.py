import sys
import csv

def removeSpaces(inputfile,outputfile):
    inf = open(inputfile, 'r')
    outf = open(outputfile,'w')
    reader = csv.reader(inf, delimiter=',', quoting=csv.QUOTE_NONE)
    writer = csv.writer(outf)
    for linha in reader:
        wlinha = []
        for coluna in linha:
            valor = coluna.strip()
            wlinha.append(valor)
        writer.writerow(wlinha)
        

inf = sys.argv[1]
outf = sys.argv[2]
removeSpaces(inf,outf)