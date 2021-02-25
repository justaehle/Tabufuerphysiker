# -*- coding: utf-8 -*-
'''
Tabu-Spiel Uni Potsdam
Program from Julian Stähle,...
'''
import numpy as np
import wordlist #hier stehen die Dictionarys drin
Modus = "Spiel" #experimental und Spiel möglich

if Modus == "experimental":
    
        for i in range(3): #Anzahl der Wörter die man sich ausgeben lassen möchte für eine Runde
            a=np.random.randint(10) #len(wordlist.liste) später. momentan sind noch nicht so viele Elemente drin
            print(20*"-") #Abgrenzung der Worte
            print("===gesuchtes Wort===")
            print("###",wordlist.liste[a]["searched Word"],"###")#Gibt einem das Gesuchte Wort
            print("---Wörter die man nicht benutzen darf---")
            print(wordlist.liste[a]["word1"])# Wort 1 welches nicht benutzt werden darf
            print(wordlist.liste[a]["word2"])# Wort 2 welches nicht benutzt werden darf
            print(wordlist.liste[a]["word3"])# Wort 3 welches nicht benutzt werden darf

elif Modus == "Spiel":

    Spieler = ["Julian","Sönke","Hans"]
    for Name in Spieler:
        f = open(Name+".txt", 'a+')
        f.write('Für Spieler '+Name+"\n")
        for i in range(3): #Anzahl der Wörter die man sich ausgeben lassen möchte für eine Runde
            a=np.random.randint(10) #len(wordlist.liste) später. momentan sind noch nicht so viele Elemente drin
            print(20*"-") #Abgrenzung der Worte
            print("==="+str(i+1)+"tes gesuchtes Wort===")
            print("###",wordlist.liste[a]["searched Word"],"###")#Gibt einem das Gesuchte Wort
            print("---Wörter die man nicht benutzen darf---")
            print(wordlist.liste[a]["word1"])# Wort 1 welches nicht benutzt werden darf
            print(wordlist.liste[a]["word2"])# Wort 2 welches nicht benutzt werden darf
            print(wordlist.liste[a]["word3"])# Wort 3 welches nicht benutzt werden darf
            #
            #Schreibt obiges in eine Seperate Datei die man Leuten zuschicken kann.
            #
            f.write("==="+str(i+1)+"tes gesuchtes Wort===\n")
            f.write("###"+wordlist.liste[a]["searched Word"]+"###\n")
            f.write("---Wörter die man nicht benutzen darf---\n")
            f.write(wordlist.liste[a]["word1"]+"\n")
            f.write(wordlist.liste[a]["word2"]+"\n")
            f.write(wordlist.liste[a]["word3"]+"\n")
        f.close()