# Zählen Sie, wie häufig die einzelnen Worte eines kurzen Textes in diesem vorkommen. Schreiben Sie
# hierfür ein Programm, das eine Zeichenkette in ihre Wörter zerlegt. Geben Sie dann die Häufigkeit
# der einzelnen Wörter dem User aus.
# Beispiel: Für die Zeichenkette "Ich studiere an der THI und ich habe Spaß" soll die Ausgabe an
# den User ähnlich aussehen wie: Ich: 2, studiere: 1, an: 1, der: 1, THI: 1, und: 1, Ich: 2, habe: 1,
# Spaß: 1.
# Tipp: Verwenden Sie die auf Listen definierte Funktion count()

entry = input("Geben Sie einen Satz ein und ich zähle die Häufigkeit der einzelnen Wörter: ")                    # Benutzereingabe erfragen
words = entry.split()                                                                                            # Zeichenkette in Wörter zerlegen 
if len(words) == 0:                                                                                              # Prüfen, ob die Liste leer ist
    print("Keine Wörter zum Zählen gefunden.")                                                                   # Nachricht bei leerer Eingabe 
else:
    word_count = {}                                                                                              # Leeres Dictionary für Wortzählung
    for word in words:                                                                                           # Durchlaufe jedes Wort in der Liste                
        word_count[word] = words.count(word)                                                                     # Zähle die Häufigkeit des Wortes und speichere es im Dictionary
    for word, count in word_count.items():                                                                       # Durchlaufe das Dictionary
        print(f"{word}: {count}")                                                                                # Ausgabe der Häufigkeit jedes Wortes