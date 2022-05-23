what_are_cookie_text1 = """I cookie, i pixel e altre tecnologie di tracciamento (collettivamente, i @@cookie@@) sono una stringa di dati di solo testo che un sito Web trasferisce al file dei cookie del browser situato sul disco rigido del computer dell'utente e che consente al sito di riconoscerlo. I cookie possono aiutare un sito ad adattare i contenuti agli interessi principali dell'utente. Alcuni cookie ci consentono di ricreare e riprodurre le sessioni degli utenti sui nostri Siti. Quasi tutti i siti di grandi dimensioni utilizzano i cookie."""

a= "asdfasdfasdfas"
b= "asdfa3dfasdfas"

for i, row in enumerate(a):
  #print(i, " ------ ", row )
  for j , value in enumerate(b):
    if i == j and row != value:
      print(row, "----", value )

            