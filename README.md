# Openfisca-italy
![Build Status](https://circleci.com/gh/openfisca/openfisca-italy.svg?style=shield&circle-token=:circle-token)
## [EN] Introduction
OpenFisca is a versatile microsimulation free software. This repository contains the OpenFisca model of the Italian tax and benefit system. Therefore, the working language here is Italian. You can however check the [general OpenFisca documentation](http://openfisca.org/doc/) in English!
## [IT] Introduzione
OpenFisca è un software gratuito di microsimulazione versatile. Questa repository contiene il modello del sistema Italiano di tasse e benefici. Perciò, la lingua con cui lavoreremo sarà l'italiano. Si può comunque consultare la [documentazione](http://openfisca.org/doc/) scritta in inglese.
## Feature
### Obiettivi finali da raggiungere 
* Costruire un sistema di tasse e benefici completo per l'Italia, definendo ogni singola Variabile, Parametro, Riforma,Entità e Formula;
* Implementare un software grafico dalle diverse funzionalità che possa essere utilizzato dalla pubblica amministrazione per misurare l'impatto che porterebbe al sistema Italiano il cambiamento di una Variabile/Parametro/Riforma tramite un sistema di simulazioni.
### Obiettivi
L'obiettivo dal quale si vuole partire è quello di definire un sistema per gestire la disoccupazione. In particolare, i prossimi obiettivi da raggiungere per il campo della disoccupazione sono:
- [✓] Definire variabili, parametri, riforme.... per creare una base dalla quale partire per sviluppare delle features;
- [✓] __Feature 1__: Gestione IRPEF;
- [✓] __Feature 2__: Gestione IMU;
- [ ] __Feature 3__: Prototipo Web Api.

## Prerequisiti per l'installazione
### Sistemi operativi supportati
* Distribuzioni Gnu/Linux (in particolare Debian e Ubuntu);
* Mac OS X ;
* Windows;
### Strumenti necessari
* [Git](https://git-scm.com/)
* [Python v. 2.7](https://www.python.org/download/releases/2.7/)
* [Pip](https://pip.pypa.io/en/stable/installing/)
* [Numpy](https://pypi.python.org/pypi/numpy)
* [Pew](https://pypi.python.org/pypi/pew/)
## Installazione
Per ora non esiste ancora una versione stabile di OpenFisca-Italy.
## Iniziare a contribuire
Per iniziare a contribuire al progetto OpenFisca-Italy leggi la seguente [linea guida](http://openfisca.org/doc/contribute/guidelines.html) che spiega nel dettaglio le modalità con le quali effettuare le operazioni. Dopodiché esegui i seguenti step:
* Aprire un terminale; 
* Spostarsi nella directory nella quale si vuole clonare il progetto;
* Clonare il progetto nella directory corrente utilizzando il comando:
```bash
git clone https://github.com/openfisca/openfisca-italy
```

Questo è un esempio di output
![Cmd-all](https://i.imgur.com/Lci2IVz.png)
## Come contribuire
Prima di poter iniziare a scrivere codice (e inziare, quindi, a definire nuove Variabili,Parametri,Riforme,Formule etc...) dovrai leggere attentamente i [concetti chiave](http://openfisca.org/doc/key-concepts.html) sui cui si basa OpenFisca (e in generale un sistema di tasse e benefici) e la [guida dalla legge al codice](http://openfisca.org/doc/coding-the-legislation/index.html).
## Conclusione
:tada: Complimenti, se hai letto tutte le sezioni precedenti ed hai eseguito tutte le istruzioni al loro interno sei pronto per sviluppare il sistema di tasse e benefici per l'italia.:tada:
