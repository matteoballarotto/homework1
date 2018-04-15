# homework1
Primo elaborato corso "Laboratorio ciberfisico"

## Consegna:
Si realizzi un package ROS contenente degli opportuni nodi per poter svolgere i compiti seguenti:

• Un nodo pubblica, 1 volta al secondo, un messaggio contenente un nome, una età, e un corso di laurea: nodo1.py <br>
• Un nodo permette di selezionare da tastiera quale parte del messaggio verrà mostrata a video: nodo2.py <br>
• Un nodo mostra a video la parte del messaggio selezionata: nodo3.py<br><br>


Il nodo che permette di selezionare da tastiera quale parte del messaggio mostrare dovrà comportarsi nel modo seguente:

• Digitando ‘a’ verrà stampato tutto il messaggio <br>
• ‘n’ mostrerà solo il nome <br>
• ‘e’ mostrerà solo l’età <br>
• ‘c’ mostrerà solo il corso di laurea <br><br>

Di seguito lo schema dei nodi e il dettaglio sull'invio dei messaggi <br>
![Rosgraph](include/rosgraph.svg)

<br><br>
Il nodo uno manda una volta al secondo il messaggio al nodo 3, mentre il nodo 2 una volta effettuata la selezione da tastiera  invia la scelta al nodo 3 il quale, una volta letta, mostra il messaggio relativo


### Esecuzione
<br><br>
Una volta clonato il repository, spostarlo nel workspace con il comando <br>
```
  mv homework1/ ~/catkin_ws/src/
```
<br><br>
Il sistema può essere fatto partire i due modi: <br>
• utilizzando il launchfile, digitando
```
  roslaunch homework1 homework1.launch
```
<br>
• aprendo 4 terminali, nei quali digitare: <br>
Terminale 1: <br>

```
  roscore
```

<br>
Terminale 2: <br>

```
  rosrun homework1 nodo1.py
```

<br>
Terminale 3: <br>

```
  rosrun homework1 nodo2.py
```

<br>
Terminale 4: <br>

```
  rosrun homework1 nodo3.py
```

<br>

Una volta terminata l'esecuzione, uscire con CTRL+C


### Funzionamento specifico <br>
Una volta a pieno regime, ovvero con tutti e tre i nodi attivi, il nodo 3, ovvero il listener, riceve una volta al secondo il messaggio dal nodo1, mentre la scelta la riceve solo quando l'utente la inserisce all'interno della console.<br>
Una volta ricevuta, mostra il messaggio in base alla scelta effettuata.<br>
Dopodichè di rimette in attesa fino ad altra scelta.

