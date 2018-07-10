# Python ohjelmointia aloittelijoille kurssi: (Baarikierrokseni)

* Ohjelman suoritus vaatii python 3 toimiakseen
* Ohjelma käynnistetään antamalla komentoriville käsky: python3 index.py
* Ohjelma on komentorivipohjainen

# Dokumentaatio

Kun ohjelman suoritus alkaa pyydetään käyttäjää syöttämään tietokannan nimi. Tietokannan nimeen lisätään .json pääte, sillä tietokannan tyyppi on json tiedosto. JSON (lyhenne sanoista JavaScript Object Notation) on yksinkertainen avoimen standardin tiedostomuoto tiedonvälitykseen. Nimestään ja JavaScript-perustastaan huolimatta JSON on JavaScriptistä riippumaton.

Projektin tietorakenteen tyypiksi tai tietokannaksi valittiin JSON, sillä se on kevyt ja helpporakenteinen yksinkertaiselle ohjelmalle. Pythoniin saa myös suoraan importattua json kirjaston, joten sen valinta oli luontevaa. JSON tiedostoja on myös mahdollista käsitellä muilla ohjelmointikielillä, kuten esimerkiksi JavaScriptillä.

Jos tietokanta löytyy ennestään, eli nimi on oikea, asetetaan tietokanta globaaliin muuttujaan ja siirrytään ohjelman suorituksessa eteenpäin antamalla käyttäjälle ohjeet ohjelman toiminnasta jonka jälkeen siirrytään funktioon "start", joka odottaa käyttäjän syötettä.

Käyttäjällä on käytettävissään seuraavat komennot

0. Apu
1. Lisää baarikierros
2. Listaa baarikierrokset
3. Poista baarikierros
4. Muokkaa kierrosta
5. Lopeta

Kun käyttäjä on syöttänyt numeron haluamastaan toimenpiteeestä, yksinkertaisella if else lausekkeella ajetaan numeroa vastaava funktio.

Jos taas tietokantaa ei löydy, luodaan uusi tiedosto jonka päätteenä on .json ja nimenä käyttäjän kirjoittama nimi. Sen jälkeen asetetaan globaaliin muuttujaan tietokannan nimi ja alustetaan tiedostoon jsonin perus rakenne käyttämällä file writea. Sitten siirrytään taas pääohjelmaan "start"

Ohjelman listauksessa listataan indeksin perusteella kaikki kierrokset ja kierroksen ominaiset tiedot indentoituna alle.

Poistotoimenpiteessä käyttäjä syöttää indeksinumeron jonka perusteella kierros poistetaan.

Muokkaus toimii samaan tapaan, objekti etsitään indeksillä, jonka jälkeen sitä on helppoa muokata.

Lisääminen tapahtuu jsonin appendilla, eli taulukkoon lisätään uusi objekti käyttäjän syötteiden mukaisesti.

Json on importattu projektiin, jotta json tiedoston käsittely olisi helpompaa pythonin avulla.

Myös system on importattu, jotta ohjelma saadaan lopetettua ilman virheilmoituksia.

Nämä ovat Pythonin omaa toiminnallisuutta.

Lisäksi projektin alkuun on laitettu coding: utf-8 jotta suomalaiset ääkköset toimivat kivasti. Projektia myös ajetaan python versiolla kolme, jotta formatoinnit toimivat ns. oikein. Python versiossa 2 json tiedoston tulostamiseen tuli preformatointeja, joita emme halua loppukäyttäjälle näyttää.

Json tietokantaratkaisuun päädyttiin sen yksinkertaisuuden takia ja siihen liittyvän apukirjaston sai myös importattua suoraan pythoniin.

# Puutteet

* Syötettävää ja muokattavaa dataa ei validoida mitenkään. Ohjelma voi siis kaatua käyttäjän syötteiden takia tai antaa virheilmoituksen.
* Listaamisessa ei ole filttereitä eikä hakua
* Ohjelmaa on testattu vain yhdessä ympäristössä
