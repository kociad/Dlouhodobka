import winsound
import time
from tkinter import *

global first_launch
first_launch=0

def ENDING_GOOD():
    print("PLACEHOLDER_GOOD_ENDING")
def ENDING_BAD():
    print("PLACEHOLDER_BAD_ENDING")
def PRINT():
    global t
    global first_launch
    if first_launch==1:
        text.config(state=NORMAL)
        text.insert(END, wolba.get())
        text.insert(END, "\n\n")
    wolba.delete(0,"end")
    for i in t:
        text.insert(END, i)
        time.sleep(0.025)
        text.update()
    text.insert(END, "\n\n")
    text.config(state=DISABLED)
"""
#INVENTAR
if "prozkoumej" in volba:
    if "klíč(váhy)" in volba:
        if "klíč(váhy)" in inventar:
            t="Klíč se znamením vah."
            BLANKV()
    if "nůž" in volba:
        if "nůž(tupý)" in inventar:
            t="Tupý kuchyňský nůž."
            BLANKV()
        if "nůž(ostrý)" in inventar:
            t="Ostrý kuchyňský nůž. Vhodný pro řezání masa, ovoce i zeleniny"
            BLANKV()
    if "izolepa" in volba or "lepící páska" in volba:
        if "izolepa" in inventar:
            t="Stříbrná lepící páska, vhodná pro namáhané spoje."
            BLANKV()
    if "nůž" in volba:
        if "nůž(ostrý)" in inventar:
            t="Ostrý kuchyňský nůž. Vhodný pro krájení masa nebo zeleniny."
            BLANKV()
        if "nůž(tupý)" in inventar:
            t="Tupý kuchyňský nůž. Tímhle nic nepřeřízneš."
            BLANKV()
    if "pojistka" in volba:
        if "pojistka" in inventar:
            t="Obyčejná pojistka."
            BLANKV()
    if "polovina klíče" in volba:
        if "polovina klíče 'OMEGA'(A)" in inventar or "polovina klíče 'OMEGA'(B)" in inventar:
            t="Polovina klíče se znamením 'OMEGA'."
            BLANKV()
    if "svítilna" in volba:
        if "svítilna(bez baterií)" in inventar:
            t="Vodotěsná svítilna. Bohužel v ní nejsou baterie."
            BLANKV()
        elif "svítilna" in inventar:
            t="Funkční vodotěsná svítilna."
            BLANKV()
    if "tágo" in volba:
        if "tágo(zlomené)" in inventar:
            t="Kulečníkové tágo. Bohužel je zlomené."
            BLANKV()
    if "klíč(omega)" in volba:
        if "klíč(OMEGA)" in inventar:
            t="Klíč se znamením 'OMEGA'."
            BLANKV()
    if "klíč(beta)" in volba:
        if "klíč(BETA)" in inventar:
            t="Klíč se znamením 'BETA'."
            BLANKV()
    if "klíč(beran)" in volba:
        if "klíč(beran)" in inventar:
            t="Klíč se znamením berana."
            BLANKV()
    if "lepidlo" in volba:
        if "lepidlo" in inventar:
            t="Silné modelářské lepidlo. Vhodné pro lepení dřeva, plastů i kovu."
            BLANKV()
    if "baterie" in volba:
        if "baterie" in inventar:
            t="Sada tužkových baterií."
            BLANKV()
    if "zapalovač" in volba:
        if "zapalovač" in inventar:
            t="Kvalitní benzínový zapalovač s vyrytým křížem."
            BLANKV()
    if "ručička" in volba:
        if "ručička" in inventar:
            t="Ručička z hodin."
            BLANKV()
    if "klíč(alfa)" in volba:
        if "klíč(ALFA)" in inventar:
            t="Klíč se znamením 'ALFA'."
            BLANKV()
    if "hák" in volba:
        if "hák(zlomený)" in inventar:
            t="Zlomený hák na čištění okapů. V tomhle stavu s ním asi nikam nedosáhneš."
            BLANKV()
        elif "hák(prodloužený)" in inventar:
            t="Hák na čištění okapů prodloužený zlomeným tágem."
            BLANKV()
    if "zbraň" in volba:
        if "zbraň" in inventar:
            t="Nabitá pistole."
            BLANKV()
    if "brousek" in volba:
        if "brousek" in inventar:
            t="Brousek. Vhodný pro ostření nožů."
            BLANKV()
"""
#SC00_BLANK
def BLANKT():
    print("PLACEHOLDER") #Úvodní text scény
    print("Co uděláš?")
    BLANKV()
def BLANKV():
    global inventar #Inventář musí být vždy globální
    volba=input("Zadej příkaz:")
    volba=volba.lower()
    #---------------------DEBUG----------------------
    if "dbg_tutorial_skip" in volba:
        NOVA_HRA()
    if "dbg_op" in volba:
        OPT()
    if "dbg_kuchyne" in volba:
        KUCHYNET()
    if "dbg_koupelna" in volba:
        KOUPELNAT()
    if "dbg_herna" in volba:
        HERNAT()
    if "dbg_knihovna" in volba:
        KNIHOVNAT()
    if "dbg_loznice" in volba:
        LOZNICET()
    if "dbg_balkon" in volba:
        BALKONT()
    if "dbg_puda" in volba:
        PUDAT()
    if "dbg_chodba" in volba:
        CHODBAT()
    if "dbg_inv" in volba:
        volbaa=input("Zadej předmět:")
        inventar.append(volbaa)
    #------------------------------------------------
    if volba=="inventář" or volba=="inventar": #Kontrola inventáře
        t=str(inventar)
        BLANKV() #Návrat na začátek fce
    if "prozkoumej" in volba:
        if "místnost" in volba: 
            print("PLACEHOLDER")
            BLANKV()
        if "OBJECT" in volba:
            if "ITEM" in inventar:
                print("PLACEHOLDER_NO_ITEM")
                BLANKV()
            else:
                print("PLACEHOLDER")
                BLANKV()
    if "vezmi" in volba:
        if "ITEM" in volba:
            if "ITEM" in inventar:
                print("PLACEHOLDER_NO_ITEM")
            else:
                print("PLACEHOLDER_ITEM_TAKEN")
                inventar.append("ITEM")
                BLANKV()
        else:
            print("Nevím jak to udělat")
            BLANKV()
    if "použij" in volba:
        if "PLACEHOLDER_DOOR" in volba:
            return
            #další scéna
    else:
        print("Tento příkaz neznám.")
        BLANKV()
#SC01 (SKLEP TMA)
def SKLEP1T():
    global t
    winsound.PlaySound("sound/basement.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
    t="Vítej do mojí hry! Pro provedení akce piš do příkazové řádky. Hra má tři hlavní akce: 'Prozkoumej' 'Vezmi' a 'Použij'. Svůj inventář si prohlédneš příkazem 'inventář'. Tyto akce kombinuj s předměty v herním světě nebo v inventáři. Objekty piš vždy v prvním pádě (hlavu=hlava atd.). Pojďme si to vyzkoušet v tomto úvodu. \n\nProbouzíš se v chladné a vlhké místnosti. Vzadu na hlavě cítíš ostrou bolest. Tvé ruce jsou svázáné, ale naštěstí cítíš v kapse svůj věrný nůž. Zkus napsat 'prozkoumej kapsy'.\n\nCo uděláš?"
    global inventar
    global svazan
    global svetlo
    svetlo=0
    svazan=1
    inventar=[]
    SKLEP1V()
def SKLEP1V():
    global first_launch
    global svazan
    global inventar
    global svetlo
    global t
    PRINT()
    first_launch=1
    submit.wait_variable(var)
    volba=wolba.get()
    volba=volba.lower()
    if volba=="inventář" or volba=="inventar":
        t=str(inventar)
        SKLEP1V()
    #---------------------DEBUG----------------------
    if "dbg_tutorial_skip" in volba:
        NOVA_HRA()
    if "dbg_op" in volba:
        OPT()
    if "dbg_kuchyne" in volba:
        KUCHYNET()
    if "dbg_koupelna" in volba:
        KOUPELNAT()
    if "dbg_herna" in volba:
        HERNAT()
    if "dbg_knihovna" in volba:
        KNIHOVNAT()
    if "dbg_loznice" in volba:
        LOZNICET()
    if "dbg_balkon" in volba:
        BALKONT()
    if "dbg_puda" in volba:
        PUDAT()
    if "dbg_chodba" in volba:
        CHODBAT()
    if "dbg_inv" in volba:
        volbaa=input("Zadej předmět:")
        inventar.append(volbaa)
    #------------------------------------------------
    if "prozkoumej" in volba:
        if "místnost" in volba:
            t=("Obklopuje tě tma, skoro nic nevidíš. Naproti tobě proniká skulinkou pod něčím, co by mohly být dveře, trocha světla, která stačí na to aby sis všiml tlačítka na zdi. Zkus ho zmáčknout příkazem 'použij tlačítko'.")
            SKLEP1V()
        if "kapsy" in volba or "kapsa" in volba:
            if "nůž" in inventar:
                t=("Nic jiného už v kapsách nemáš.")
                SKLEP1V()
            else:
                t=("V kapse jsi nahmatal malý kapesní nůž. Vezmi ho příkazem 'vezmi nůž'.")
                SKLEP1V()
        if "ruce" in volba:
            if svazan==1:
                t=("Tvoje ruce jsou pevně svázané provazem.")
                SKLEP1V()
            else:
                t=("Co jiného bys chtěl vidět? Jsou to tvoje ruce...")
                SKLEP1V()
        if "hlava" in volba:
            if svazan==1:
                t=("Tvoje ruce jsou svázané a nejsi proto schopen ohmatat svoji hlavu.")
                SKLEP1V()
            else:
                t=("Tvoje hlava je vzadu rozbitá. Krev ještě úplně nezaschla.")
                SKLEP1V()
        if "provaz" in volba or "provazy" in volba:
            if svazan==1:
                t=("Provazy ti pevně drží ruce svázané.")
                SKLEP1V()
            else:
                t=("Rozřezaný provaz leží na zemi. Je zničen tak že už nepůjde použít.")
                SKLEP1V()
        else:
            t=("Asi ti nerozumím.")
            SKLEP1V()
    if "vezmi" in volba:
        if "nůž" in volba:
            if "nůž" in inventar:
                t=("Nůž už máš v inventáři")
                SKLEP1V()
            else:
                t=("Sebral jsi svůj nůž. Zkus ho použít na provazy příkazem 'použij nůž na provazy'.")
                inventar.append("nůž")
                SKLEP1V()
        else:
            t=("Nevím jak to udělat")
            SKLEP1V()
    if "použij" in volba:
        if "nůž" in volba:
            if svazan==1:
                if "provaz" in volba or "provazy" in volba:
                    winsound.PlaySound("sound/rope.wav", winsound.SND_ASYNC)
                    time.sleep(13)
                    t=("Podařilo se ti provazy přeříznout. Nyní jsi volný. Zkus se podívat kolem.")
                    winsound.PlaySound("sound/basement.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
                    svazan=0
                    SKLEP1V()
                else:
                    t=("To asi nepůjde")
                    SKLEP1V()
            else:
                if "provaz" in volba or "provazy" in volba:
                    t=("Provazy už jsou přeřízlé")
                    SKLEP1V()
                else:
                    t=("To asi nepůjde")
                    SKLEP1V()
        if "tlačítko" in volba:
            if svazan==1:
                t=("Jsi svázaný, nedokážeš se k tlačítku dostat a stisknout ho. Nejdříve se uvolni.")
                SKLEP1V()
            else:
                winsound.PlaySound("sound/switch.wav", winsound.SND_ASYNC)
                time.sleep(1)
                SKLEP2T()
                svetlo=1
    if svetlo==1:
        return
    else:
        t=("Tento příkaz neznám: ",volba)
        SKLEP1V()
#SC02 (SKLEP SVĚTLO)
def SKLEP2T():
    global t
    winsound.PlaySound("sound/basement.wav",winsound.SND_ASYNC | winsound.SND_LOOP)
    t=("Místnost zalilo světlo. Kolem sebe vidíš něco co by mohl být sklep. Teď si to vyzkoušej sám!\n\nCo uděláš?")
    global stul
    global dvereopen
    stul=0
    dvereopen=0
    SKLEP2V()
def SKLEP2V():
    global t
    global inventar
    global stul
    global dvereopen
    PRINT()
    submit.wait_variable(var)
    volba=wolba.get()
    volba=volba.lower()
    #---------------------DEBUG----------------------
    if "dbg_tutorial_skip" in volba:
        NOVA_HRA()
    if "dbg_op" in volba:
        OPT()
    if "dbg_kuchyne" in volba:
        KUCHYNET()
    if "dbg_koupelna" in volba:
        KOUPELNAT()
    if "dbg_herna" in volba:
        HERNAT()
    if "dbg_knihovna" in volba:
        KNIHOVNAT()
    if "dbg_loznice" in volba:
        LOZNICET()
    if "dbg_balkon" in volba:
        BALKONT()
    if "dbg_puda" in volba:
        PUDAT()
    if "dbg_chodba" in volba:
        CHODBAT()
    if "dbg_inv" in volba:
        volbaa=input("Zadej předmět:")
        inventar.append(volbaa)
    #------------------------------------------------
    if volba=="inventář" or volba=="inventar":
        t=str(inventar)
        SKLEP2V()
    if "prozkoumej" in volba:
        if "místnost" in volba:
            t=("Kolem sebe vidíš malý sklep. V rohu místnosti leží něco co vypadá jako deka, po straně místnosti se pak nachází stůl na kterém něco leží.")
            SKLEP2V()
        if "stůl" in volba:
            t=("Na stole se nachází kovová tyč, nějaké odpadky a prázdná láhev")
            stul=1
            SKLEP2V()
        if "deka" in volba:
            t=("Stará špinavá a zapáchající deka. Něco by pod ní mohlo být.")
            SKLEP2V()
        if "tyč" in volba:
            if stul==1:
                t=("Tyč na stole. Celkem dlouhá, celá ze železa.")
                SKLEP2V()
            else:
                t=("Nevím co máš na mysli")
                SKLEP2V()
        if "láhev" in volba:
            if stul==1:
                t=("Prázdná láhev. Nic v ní není.")
                SKLEP2V()
            else:
                t=("Nevím co máš na mysli")
                SKLEP2V()
    if "vezmi" in volba:
        if "deka" in volba:
            t=("To opravdu nechceš.")
            SKLEP2V()
        if "tyč" in volba:
            if "tyč" in inventar:
                t=("Už máš tyč ve svém inventáři")
                SKLEP2V()
            else:
                if stul==1:
                    t=("Vzal sis železnou tyč.")
                    inventar.append("tyč")
                    SKLEP2V()
                else:
                    t=("Nevím o čem mluvíš")
                    SKLEP2V()
        if "láhev" in volba:
            t=("Tu nebudeš asi potřebovat")
            SKLEP2V()
        if "odpadky" in volba:
            t=("Fuj?")
            SKLEP2V()
    if "použij" in volba:
        if "deka" in volba:
            if "klíč" in inventar:
                t=("Nic jiného už tam není")
                SKLEP2V()
            else:
                winsound.PlaySound("sound/blanket.wav",winsound.SND_ASYNC)
                time.sleep(1)
                winsound.PlaySound("sound/basement.wav",winsound.SND_ASYNC | winsound.SND_LOOP)
                t=("Pod dekou byl klíč který sis vzal")
                inventar.append("klíč")
                SKLEP2V()
        if "nůž" in volba:
            t=("To asi nepůjde")
            SKLEP2V()
        if "dveře" in volba:
            if dvereopen==1:
                t=("Vycházíš z tmavého sklepení. Ve chvíli kdy vyjdeš schody ucítíš na svém zátylku ostrou bolest. Upadáš na zem a téměř okamžitě ztrácíš vědomí.")
                winsound.PlaySound(None, winsound.SND_ASYNC)
                winsound.PlaySound("sound/hit.wav", winsound.SND_ASYNC)
                time.sleep(1)
                winsound.PlaySound("sound/thud.wav",winsound.SND_ASYNC)
                NOVA_HRA()
            elif "tyč" in volba:
                if "tyč" in inventar:
                    winsound.PlaySound("sound/door_break.wav",winsound.SND_ASYNC)
                    time.sleep(2)
                    winsound.PlaySound("sound/basement.wav",winsound.SND_ASYNC | winsound.SND_LOOP)
                    t=("Vypáčil jsi dveře")
                    dvereopen=1
                    inventar.remove("tyč")
                    SKLEP2V()
                else:
                    t=("To nefunguje")
                    SKLEP2V()
            elif "klíč" in volba:
                if "klíč" in inventar:
                    t=("Klíč se zlomil")
                    inventar.remove("klíč")
                    SKLEP2V()
                else:
                    t=("To nejde")
            else:
                t=("Dveře jsou zamčené")
                SKLEP2V()
    else:
        t=("Tento příkaz neznám: ",volba)
        SKLEP2V()
#SC03 (Obývací pokoj)
def NOVA_HRA():
    ###
    winsound.PlaySound("sound/hit.wav", winsound.SND_ASYNC)
    ###
    global inventar
    inventar=[]
    global zamek_alfa_zamcen
    zamek_alfa_zamcen=1
    global zamek_beta_zamcen
    zamek_beta_zamcen=1
    global zamek_gama_zamcen
    zamek_gama_zamcen=1
    global trezor_zamcen
    trezor_zamcen=1
    global dvere_vahy_zamceno
    dvere_vahy_zamceno=1
    global vana_naplnena
    vana_naplnena=1
    global susicka
    susicka=1
    global pojistka
    pojistka=0
    global krb_plamen
    krb_plamen=0
    global hak_zlomeny
    hak_zlomeny=1
    global wc
    wc=1
    global telo_rozrezane
    telo_rozrezane=0
    global krb_alkohol
    krb_alkohol=0
    global kukacky
    kukacky=0
    global dvere_beran_zamceno
    dvere_beran_zamceno=1
    global PC
    PC=0
    global poklop
    poklop=0
    global svitilna
    svitilna=0
    global skrin
    skrin=0
    #Nutno dodělat některé přepínače
    OPT()
def OPT():
    global t
    t=("Probouzíš se na starém, zapáchajícím gauči. Vstáváš a zjišťuješ že se nacházíš v neznámé místnosti. \n\nCo uděláš?")
    OPV()
def OPT2():
    global t
    t=("Jsi v pokoji.")
    t=("Co uděláš?")
    OPV()
def OPV():
    global t
    global inventar
    global pojistka
    global dvere_vahy_zamceno
    global zamek_alfa_zamcen
    global zamek_beta_zamcen
    global zamek_gama_zamcen
    PRINT()
    submit.wait_variable(var)
    volba=wolba.get()
    volba=volba.lower()
    #---------------------DEBUG----------------------
    if "dbg_tutorial_skip" in volba:
        NOVA_HRA()
    if "dbg_op" in volba:
        OPT()
    if "dbg_kuchyne" in volba:
        KUCHYNET()
    if "dbg_koupelna" in volba:
        KOUPELNAT()
    if "dbg_herna" in volba:
        HERNAT()
    if "dbg_knihovna" in volba:
        KNIHOVNAT()
    if "dbg_loznice" in volba:
        LOZNICET()
    if "dbg_balkon" in volba:
        BALKONT()
    if "dbg_puda" in volba:
        PUDAT()
    if "dbg_chodba" in volba:
        CHODBAT()
    if "dbg_inv" in volba:
        volbaa=input("Zadej předmět:")
        inventar.append(volbaa)
    #------------------------------------------------
    if volba=="inventář" or volba=="inventar":
        t=str(inventar)
        OPV()
    if "prozkoumej" in volba:
        if "klíč(váhy)" in volba:
            if "klíč(váhy)" in inventar:
                t="Klíč se znamením vah."
                OPV()
        if "izolepa" in volba or "lepící páska" in volba:
            if "izolepa" in inventar:
                t="Stříbrná lepící páska, vhodná pro namáhané spoje."
                OPV()
        if "nůž" in volba:
            if "nůž(ostrý)" in inventar:
                t="Ostrý kuchyňský nůž. Vhodný pro krájení masa nebo zeleniny."
                OPV()
            if "nůž(tupý)" in inventar:
                t="Tupý kuchyňský nůž. Tímhle nic nepřeřízneš."
                OPV()
        if "pojistka" in volba:
            if "pojistka" in inventar:
                t="Obyčejná pojistka."
                OPV()
        if "polovina klíče" in volba:
            if "polovina klíče 'OMEGA'(A)" in inventar or "polovina klíče 'OMEGA'(B)" in inventar:
                t="Polovina klíče se znamením 'OMEGA'."
                OPV()
        if "svítilna" in volba:
            if "svítilna(bez baterií)" in inventar:
                t="Vodotěsná svítilna. Bohužel v ní nejsou baterie."
                OPV()
            elif "svítilna" in inventar:
                t="Funkční vodotěsná svítilna."
                OPV()
        if "tágo" in volba:
            if "tágo(zlomené)" in inventar:
                t="Kulečníkové tágo. Bohužel je zlomené."
                OPV()
        if "klíč(omega)" in volba:
            if "klíč(OMEGA)" in inventar:
                t="Klíč se znamením 'OMEGA'."
                OPV()
        if "klíč(beta)" in volba:
            if "klíč(BETA)" in inventar:
                t="Klíč se znamením 'BETA'."
                OPV()
        if "klíč(beran)" in volba:
            if "klíč(beran)" in inventar:
                t="Klíč se znamením berana."
                OPV()
        if "lepidlo" in volba:
            if "lepidlo" in inventar:
                t="Silné modelářské lepidlo. Vhodné pro lepení dřeva, plastů i kovu."
                OPV()
        if "baterie" in volba:
            if "baterie" in inventar:
                t="Sada tužkových baterií."
                OPV()
        if "zapalovač" in volba:
            if "zapalovač" in inventar:
                t="Kvalitní benzínový zapalovač s vyrytým křížem."
                OPV()
        if "ručička" in volba:
            if "ručička" in inventar:
                t="Ručička z hodin."
                OPV()
        if "klíč(alfa)" in volba:
            if "klíč(ALFA)" in inventar:
                t="Klíč se znamením 'ALFA'."
                OPV()
        if "hák" in volba:
            if "hák(zlomený)" in inventar:
                t="Zlomený hák na čištění okapů. V tomhle stavu s ním asi nikam nedosáhneš."
                OPV()
            elif "hák(prodloužený)" in inventar:
                t="Hák na čištění okapů prodloužený zlomeným tágem."
                OPV()
        if "zbraň" in volba:
            if "zbraň" in inventar:
                t="Nabitá pistole."
                OPV()
        if "brousek" in volba:
            if "brousek" in inventar:
                t="Brousek. Vhodný pro ostření nožů."
                OPV()
        if "papír" in volba:
            if "papír(citronový)" in inventar:
                t=("Prázdný papír vonící po citrónu.")
                OPV()
            if "papír(vzkaz)" in inventar:
                t=("Na papíře je vzkaz hnědým písmem: '232.8°C'")
                OPV()
        if "místnost" in volba: 
            t=("Nacházíš se v něčem co připomíná obývací pokoj. Naproti gauči se nachází velká televize. Za gaučem je potom schodiště vedoucí nahoru a pod schodištěm na stěně se nachází pojistková skříň. Naproti pojistkové skříni je polička s fotkami a vyhořelými svíčkami. Pokoj je spojený s chodbou, ve které jsou troje dveře. Jedny s nápisem 'Koupelna', druhé se znakem vah a hlavní dveře. Dále jde z pokoje průchod do kuchyně.")
            OPV()
        if "gauč" in volba:
            if "klíč(váhy)" in inventar:
                t=("Je to starý zatuchlý gauč. Na gauči jsou zbytky krve, ale nejsi schopný poznat zda je tvoje.")
                OPV()
            else:
                t=("Je to starý zatuchlý gauč. Na gauči jsou zbytky krve, ale nejsi schopný poznat zda je tvoje. Pod gaučem se něco nachází ale nejsi schopný na to dosáhnout.")
                OPV()
        if "skříň" in volba or "pojistky" in volba:
            if pojistka==0:
                t=("Zdá se že je to stará pojistková skříň. Na místě s popiskem 'PATRO' chybí pojistka.")
                OPV()
            else:
                t=("Jen stará pojistková skříň. Vše se zdá být v pořádku.")
                OPV()
        if "tv" in volba or "televize" in volba:
            t=("Obyčejná televize. Zdá se být vypnutá.")
            OPV()
        if "schodiště" in volba or "schody" in volba:
            if pojistka==1:
                t=("Schody vedoucí nahoru. Nahoře se svítí.")
                OPV()
            else:
                t=("Schody vedoucí nahoru. Nahoře je tma.")
                OPV()
        if "dveře" in volba:
            if "hlavní" in volba:
                t=("Hlavní dveře od domu vedoucí ven. Jsou zamčené třemi zámky.")
                if zamek_alfa_zamcen==1:
                    t=("Zámek se znakem 'ALFA' je zamčený.")
                if zamek_beta_zamcen==1:
                    t=("Zámek se znakem 'BETA' je zamčený.")
                if zamek_gama_zamcen==1:
                    t=("Zámek se znakem 'GAMA' je zamčený.")
                elif zamek_alfa_zamcen==0 and zamek_beta_zamcen==0 and zamek_gama_zamcen==0:
                    t=("Dveře jsou odemčené.")
                OPV()
            if "váhy" in volba:
                if dvere_vahy_zamceno==1:
                    t=("Jsou to masivní dřevěné dveře. Na dveřích se nachází znak vah. Zdá se, že jsou zamčené.")
                    OPV()
                else:
                    t=("Masivní dřevěné dveře se znamením vah. Jsou odemčené.")
                    OPV()
            if "koupelna" in volba:
                t=("Jsou to dřevěné dveře, které kdysi dávno bývaly bílé. Ze spodní strany začaly před nějakou dobou plesnivět. Na dveřích je velkým písmem napsáno: 'KOUPELNA'.")
                OPV()
        if "police" in volba or "fotky" in volba:
            t=("Improvizovaná dřevěná polička na které jsou fotky neznámých lidí. První je černobílá. Je na ní starší muž s knírem, který sedí v houpacím křesle. Pod fotkou je popis: 'Andrew Smith 1956-1983'. Druhá fotka zachycuje starší paní v šatech. Pod fotkou je popis: 'Amanda Smith 1957-1998'. Na třetí fotce je usmívající se mladá žena v rudých šatech. Pod její fotkou je popis: 'Maria Smith-Green 1979-2013'. Na poslední fotce je malé dítě v kolébce. Pod fotkou je popis: 'Thomas Green 2011-2013'")
            OPV()
        else:
            t=("Nevím jak to udělat.")
            OPV()
    if "vezmi" in volba:
        t=("Tak to asi nepůjde.")
        OPV()
    if "použij" in volba:
        if "izolepa" in volba and "tágo(zlomené)" in volba and "hák(zlomený)" in volba:
            if "izolepa" in inventar and "tágo(zlomené)" in inventar and "hák(zlomený)" in inventar:
                t=("Slepil jsi zbytky tága a háku a vyrobil tak prodloužený hák.")
                inventar.remove("tágo(zlomené)")
                inventar.remove("hák(zlomený)")
                inventar.append("hák(prodloužený)")
                OPV()
            else:
                t=("Nemáš všechny materiály.")
                OPV()
        if "lepidlo" in volba and "polovina klíče gama(a)" in volba and "polovina klíče gama(b)" in volba:
            if "lepidlo" in inventar and "polovina klíče GAMA(A)" in inventar and "polovina klíče GAMA(B)" in inventar:
                t=("Slepil jsi dohromady klíč(GAMA)")
                inventar.remove("polovina klíče GAMA(A)")
                inventar.remove("polovina klíče GAMA(B)")
                inventar.append("klíč(GAMA)")
                OPV()
            else:
                t=("Něco ti chybí.")
                OPV()
        if "svítilna" in volba and "baterie" in volba:
            if "svítilna(bez baterií)" in inventar and "baterie" in inventar:
                t=("Vložil jsi baterie do svítilny.")
                inventar.remove("svítilna(bez baterií)")
                inventar.remove("baterie")
                inventar.append("svítilna")
                OPV()
            else:
                t=("Tady něco schází.")
                OPV()
        if "nůž(tupý)" in volba and "brousek" in volba:
            if "nůž(tupý)" in inventar and "brousek" in inventar:
                t=("Naostřil jsi nůž.")
                inventar.remove("nůž(tupý)")
                inventar.append("nůž(ostrý)")
                OPV()
            else:
                t=("Něco potřebuješ")
                OPV()
        if "tv" in volba or "televize" in volba:
            t=("Televize se zapla. V televizi jsou zprávy o nedávných vraždách. Pachatele se nepodařilo nikdy najít, ale všechny oběti měly do dlaní vyřezaný kříž. Po chvíli se rozhodneš televizi vypnout.")
            OPV()
        if "hák" in volba:
            if "hák(zlomený)" in inventar or "hák(prodloužený)" in inventar:
                if "gauč" in volba:
                    if "klíč(váhy)" in inventar:
                        t=("Nic jiného už jsi nenašel")
                        OPV()
                    else:
                        t=("Hákem sis přitáhl předmět pod gaučem. Ukázalo se že je to klíč se znakem vah. Klíč sis vzal.")
                        inventar.append("klíč(váhy)")
                        OPV()
                else:
                    t=("Není možné.")
                    OPV()
            else:
                ("Nevím co se po mně chce.")
                OPV()
        if "klíč" in volba:
            if "váhy" in volba:
                if "dveře" and "váhy" in volba:
                    if dvere_vahy_zamceno==1:
                        if "klíč(váhy)" in inventar:
                            t=("Odemkl sis dveře.")
                            dvere_vahy_zamceno=0
                            OPV()
                        else:
                            t=("Nemáš klíč")
                            OPV()
                    else:
                        t=("Dveře jsou už odemčené.")
                        OPV()
                else:
                    t=("Tak to asi nezvládnu.")
                    OPV()
            if "alfa" in volba:
                if "dveře" and "hlavní" in volba:
                    if zamek_alfa_zamcen==1:
                        if "klíč(ALFA)" in inventar:
                            t=("Odemkl jsi zámek 'ALFA'.")
                            zamek_alfa_zamcen=0
                            OPV()
                        else:
                            t=("Nemáš klíč.")
                            OPV()
                    else:
                        t=("Zámek už je odemčený.")
                        OPV()
                else:
                    t=("Tohle není zrovna ideální.")
                    OPV()
            if "beta" in volba:
                if "dveře" and "hlavní" in volba:
                    if zamek_beta_zamcen==1:
                        if "klíč(BETA)" in inventar:
                            t=("Odemkl jsi zámek 'BETA'.")
                            zamek_beta_zamcen=0
                            OPV()
                        else:
                            t=("Nemáš klíč.")
                            OPV()
                    else:
                        t=("Zámek už je odemčený.")
                        OPV()
                else:
                    t=("Tohle není zrovna ideální.")
                    OPV()
            if "gama" in volba:
                if "dveře" and "hlavní" in volba:
                    if zamek_gama_zamcen==1:
                        if "klíč(GAMA)" in inventar:
                            t=("Odemkl jsi zámek 'GAMA'.")
                            zamek_gama_zamcen=0
                            OPV()
                        else:
                            t=("Nemáš klíč.")
                            OPV()
                    else:
                        t=("Zámek už je odemčený.")
                        OPV()
                else:
                    t=("Tohle není zrovna ideální.")
                    OPV()
        if "průchod" in volba or "kuchyně" in volba:
            KUCHYNET()
        if "skříň" in volba or "pojistky" in volba:
            if "pojistka" in volba:
                if "pojistka" in inventar:
                    t=("Umístil jsi pojistku na její místo.")
                    inventar.remove("pojistka")
                    pojistka=1
                    OPV()
                else:
                    t=("Nemáš žádnou pojistku.")
                    OPV()
            else:
                t=("Takhle to nefunguje.")
                OPV()
        elif "dveře" in volba:
            if "hlavní" in volba:
                if zamek_alfa_zamcen==1 or zamek_beta_zamcen==1 or zamek_gama_zamcen==1:
                    t=("Snažíš se dveře otevřít, ale je zamčeno.")
                    OPV()
                else:
                    if "zbraň" in inventar:
                        ENDING_GOOD()
                    else:
                        ENDING_BAD()
            if "koupelna" in volba:
                KOUPELNAT()
            if "váhy" in volba:
                if dvere_vahy_zamceno==1:
                    t=("Lomcuješ dveřmi, ale je zamčeno.")
                    OPV()
                else:
                    HERNAT()
            else:
                t=("To nějak nejde.")
                OPV()
        if "schody" in volba or "schodiště" in volba:
            if pojistka==1:
                CHODBAT()
            else:
                t=("Nahoře je moc tma na to abys tam šel.")
                OPV()
        
        #Nutno dodělat předměty v inventáři
                        
    else:
        t=("Tento příkaz neznám: ",volba)
        OPV()
#SC04 (Kuchyně)
def KUCHYNET():
    global t
    t=("Tahle místnost je očividně kuchyně. \n\nCo uděláš?")
    KUCHYNEV()
def KUCHYNEV():
    global t
    global inventar
    global trezor_zamcen
    PRINT()
    submit.wait_variable(var)
    volba=wolba.get()
    volba=volba.lower()
    #---------------------DEBUG----------------------
    if "dbg_tutorial_skip" in volba:
        NOVA_HRA()
    if "dbg_op" in volba:
        OPT()
    if "dbg_kuchyne" in volba:
        KUCHYNET()
    if "dbg_koupelna" in volba:
        KOUPELNAT()
    if "dbg_herna" in volba:
        HERNAT()
    if "dbg_knihovna" in volba:
        KNIHOVNAT()
    if "dbg_loznice" in volba:
        LOZNICET()
    if "dbg_balkon" in volba:
        BALKONT()
    if "dbg_puda" in volba:
        PUDAT()
    if "dbg_chodba" in volba:
        CHODBAT()
    if "dbg_inv" in volba:
        volbaa=input("Zadej předmět:")
        inventar.append(volbaa)
    #------------------------------------------------
    if volba=="inventář" or volba=="inventar":
        t=str(inventar)
        KUCHYNEV()
    if "prozkoumej" in volba:
        if "klíč(váhy)" in volba:
            if "klíč(váhy)" in inventar:
                t="Klíč se znamením vah."
                KUCHYNEV()
        if "izolepa" in volba or "lepící páska" in volba:
            if "izolepa" in inventar:
                t="Stříbrná lepící páska, vhodná pro namáhané spoje."
                KUCHYNEV()
        if "nůž" in volba:
            if "nůž(ostrý)" in inventar:
                t="Ostrý kuchyňský nůž. Vhodný pro krájení masa nebo zeleniny."
                KUCHYNEV()
            if "nůž(tupý)" in inventar:
                t="Tupý kuchyňský nůž. Tímhle nic nepřeřízneš."
                KUCHYNEV()
        if "pojistka" in volba:
            if "pojistka" in inventar:
                t="Obyčejná pojistka."
                KUCHYNEV()
        if "polovina klíče" in volba:
            if "polovina klíče 'OMEGA'(A)" in inventar or "polovina klíče 'OMEGA'(B)" in inventar:
                t="Polovina klíče se znamením 'OMEGA'."
                KUCHYNEV()
        if "svítilna" in volba:
            if "svítilna(bez baterií)" in inventar:
                t="Vodotěsná svítilna. Bohužel v ní nejsou baterie."
                KUCHYNEV()
            elif "svítilna" in inventar:
                t="Funkční vodotěsná svítilna."
                KUCHYNEV()
        if "tágo" in volba:
            if "tágo(zlomené)" in inventar:
                t="Kulečníkové tágo. Bohužel je zlomené."
                KUCHYNEV()
        if "klíč(omega)" in volba:
            if "klíč(OMEGA)" in inventar:
                t="Klíč se znamením 'OMEGA'."
                KUCHYNEV()
        if "klíč(beta)" in volba:
            if "klíč(BETA)" in inventar:
                t="Klíč se znamením 'BETA'."
                KUCHYNEV()
        if "klíč(beran)" in volba:
            if "klíč(beran)" in inventar:
                t="Klíč se znamením berana."
                KUCHYNEV()
        if "lepidlo" in volba:
            if "lepidlo" in inventar:
                t="Silné modelářské lepidlo. Vhodné pro lepení dřeva, plastů i kovu."
                KUCHYNEV()
        if "baterie" in volba:
            if "baterie" in inventar:
                t="Sada tužkových baterií."
                KUCHYNEV()
        if "zapalovač" in volba:
            if "zapalovač" in inventar:
                t="Kvalitní benzínový zapalovač s vyrytým křížem."
                KUCHYNEV()
        if "ručička" in volba:
            if "ručička" in inventar:
                t="Ručička z hodin."
                KUCHYNEV()
        if "klíč(alfa)" in volba:
            if "klíč(ALFA)" in inventar:
                t="Klíč se znamením 'ALFA'."
                KUCHYNEV()
        if "hák" in volba:
            if "hák(zlomený)" in inventar:
                t="Zlomený hák na čištění okapů. V tomhle stavu s ním asi nikam nedosáhneš."
                KUCHYNEV()
            elif "hák(prodloužený)" in inventar:
                t="Hák na čištění okapů prodloužený zlomeným tágem."
                KUCHYNEV()
        if "zbraň" in volba:
            if "zbraň" in inventar:
                t="Nabitá pistole."
                KUCHYNEV()
        if "brousek" in volba:
            if "brousek" in inventar:
                t="Brousek. Vhodný pro ostření nožů."
                KUCHYNEV()
        if "papír" in volba:
            if "papír(citronový)" in inventar:
                t=("Prázdný papír vonící po citrónu.")
                KUCHYNEV()
            if "papír(vzkaz)" in inventar:
                t=("Na papíře je vzkaz hnědým písmem: '232.8°C'")
                KUCHYNEV()
        if "místnost" in volba or "kuchyně" in volba: 
            t=("Uprostřed kuchyně se nachází velký jídelní stůl a podél jedné stěny se táhne kuchyňská linka na které leží tupý nůž. Tvoji pozornost ale upoutal trezor který leží na stole.")
            KUCHYNEV()
        if "nůž" in volba:
            if "nůž(tupý)" in inventar or "nůž(ostrý)" in inventar:
                t=("Žádný jiný nůž už tu není.")
                KUCHYNEV()
            else:
                t=("Starý kuchyňský nůž. Je úplně tupý.")
                KUCHYNEV()
        if "trezor" in volba:
            if trezor_zamcen==1:
                t=("Zamčený trezor s číselným zámkem.")
                KUCHYNEV()
            else:
                t=("Otevřený trezor. Nic v něm už není.")
                KUCHYNEV()
        if "stůl" in volba:
            t=("Velký kuchyňský stůl z masivního dřeva. Kolem něj jsou rozestavěné židle a na něm leží masivní trezor.")
            KUCHYNEV()
        else:
            t=("No tak to nezvládnu.")
            KUCHYNEV()
    if "vezmi" in volba:
        if "nůž" in volba:
            if "nůž(tupý)" in inventar or "nůž(ostrý)" in inventar:
                t=("Žádný nůž tu nevidím.")
                KUCHYNEV()
            else:
                t=("Vzal sis k sobě tupý nůž.")
                inventar.append("nůž(tupý)")
                KUCHYNEV()
        else:
            t=("Nevím jak to udělat")
            KUCHYNEV()
    if "použij" in volba:
        if "izolepa" in volba and "tágo(zlomené)" in volba and "hák(zlomený)" in volba:
            if "izolepa" in inventar and "tágo(zlomené)" in inventar and "hák(zlomený)" in inventar:
                t=("Slepil jsi zbytky tága a háku a vyrobil tak prodloužený hák.")
                inventar.remove("tágo(zlomené)")
                inventar.remove("hák(zlomený)")
                inventar.append("hák(prodloužený)")
                KUCHYNEV()
            else:
                t=("Nemáš všechny materiály.")
                KUCHYNEV()
        if "lepidlo" in volba and "polovina klíče gama(a)" in volba and "polovina klíče gama(b)" in volba:
            if "lepidlo" in inventar and "polovina klíče GAMA(A)" in inventar and "polovina klíče GAMA(B)" in inventar:
                t=("Slepil jsi dohromady klíč(GAMA)")
                inventar.remove("polovina klíče GAMA(A)")
                inventar.remove("polovina klíče GAMA(B)")
                inventar.append("klíč(GAMA)")
                KUCHYNEV()
            else:
                t=("Něco ti chybí.")
                KUCHYNEV()
        if "svítilna" in volba and "baterie" in volba:
            if "svítilna(bez baterií)" in inventar and "baterie" in inventar:
                t=("Vložil jsi baterie do svítilny.")
                inventar.remove("svítilna(bez baterií)")
                inventar.remove("baterie")
                inventar.append("svítilna")
                KUCHYNEV()
            else:
                t=("Tady něco schází.")
                KUCHYNEV()
        if "nůž(tupý)" in volba and "brousek" in volba:
            if "nůž(tupý)" in inventar and "brousek" in inventar:
                t=("Naostřil jsi nůž.")
                inventar.remove("nůž(tupý)")
                inventar.append("nůž(ostrý)")
                KUCHYNEV()
            else:
                t=("Něco potřebuješ")
                KUCHYNEV()
        if "průchod" in volba or "pokoj" in volba:
            OPT2()
        if "trezor" in volba:
            if trezor_zamcen==1:
                t="První číslo:"
                PRINT()
                submit.wait_variable(var)
                C1=int(wolba.get())
                t="Druhé číslo:"
                PRINT()
                submit.wait_variable(var)
                C2=int(wolba.get())
                t="Třetí číslo:"
                PRINT()
                submit.wait_variable(var)
                C3=int(wolba.get())
                t="Čtvrté číslo:"
                PRINT()
                submit.wait_variable(var)
                C4=int(wolba.get())
                if C1==6 and C2==8 and C3==3 and C4==1:
                    trezor_zamcen=0
                    t=("Trezor se otevřel. Uvnitř byla... Izolepa? Vzal sis ji k sobě.")
                    inventar.append("izolepa")
                    KUCHYNEV()
                else:
                    t=("Nic se nestalo.")
                    KUCHYNEV()
            else:
                t=("V trezori už nic není.")
                KUCHYNEV()
    #Chybí dodělat věci v inventáři
    else:
        t=("Tento příkaz neznám: ",volba)
        KUCHYNEV()
#SC05 (Koupelna)
def KOUPELNAT():
    global t
    t=("Vcházíš do něčeho, co by se dalo nazvat koupelnou. \n\nCo uděláš?")
    KOUPELNAV()
def KOUPELNAV():
    global t
    global inventar
    global vana_naplnena
    global susicka
    global wc
    PRINT()
    submit.wait_variable(var)
    volba=wolba.get()
    volba=volba.lower()
    #---------------------DEBUG----------------------
    if "dbg_tutorial_skip" in volba:
        NOVA_HRA()
    if "dbg_op" in volba:
        OPT()
    if "dbg_kuchyne" in volba:
        KUCHYNET()
    if "dbg_koupelna" in volba:
        KOUPELNAT()
    if "dbg_herna" in volba:
        HERNAT()
    if "dbg_knihovna" in volba:
        KNIHOVNAT()
    if "dbg_loznice" in volba:
        LOZNICET()
    if "dbg_balkon" in volba:
        BALKONT()
    if "dbg_puda" in volba:
        PUDAT()
    if "dbg_chodba" in volba:
        CHODBAT()
    if "dbg_inv" in volba:
        volbaa=input("Zadej předmět:")
        inventar.append(volbaa)
    #------------------------------------------------
    if volba=="inventář" or volba=="inventar":
        t=str(inventar)
        KOUPELNAV()
    if "prozkoumej" in volba:
        if "klíč(váhy)" in volba:
            if "klíč(váhy)" in inventar:
                t="Klíč se znamením vah."
                KOUPELNAV()
        if "izolepa" in volba or "lepící páska" in volba:
            if "izolepa" in inventar:
                t="Stříbrná lepící páska, vhodná pro namáhané spoje."
                KOUPELNAV()
        if "nůž" in volba:
            if "nůž(ostrý)" in inventar:
                t="Ostrý kuchyňský nůž. Vhodný pro krájení masa nebo zeleniny."
                KOUPELNAV()
            if "nůž(tupý)" in inventar:
                t="Tupý kuchyňský nůž. Tímhle nic nepřeřízneš."
                KOUPELNAV()
        if "pojistka" in volba:
            if "pojistka" in inventar:
                t="Obyčejná pojistka."
                KOUPELNAV()
        if "polovina klíče" in volba:
            if "polovina klíče 'OMEGA'(A)" in inventar or "polovina klíče 'OMEGA'(B)" in inventar:
                t="Polovina klíče se znamením 'OMEGA'."
                KOUPELNAV()
        if "svítilna" in volba:
            if "svítilna(bez baterií)" in inventar:
                t="Vodotěsná svítilna. Bohužel v ní nejsou baterie."
                KOUPELNAV()
            elif "svítilna" in inventar:
                t="Funkční vodotěsná svítilna."
                KOUPELNAV()
        if "tágo" in volba:
            if "tágo(zlomené)" in inventar:
                t="Kulečníkové tágo. Bohužel je zlomené."
                KOUPELNAV()
        if "klíč(omega)" in volba:
            if "klíč(OMEGA)" in inventar:
                t="Klíč se znamením 'OMEGA'."
                KOUPELNAV()
        if "klíč(beta)" in volba:
            if "klíč(BETA)" in inventar:
                t="Klíč se znamením 'BETA'."
                KOUPELNAV()
        if "klíč(beran)" in volba:
            if "klíč(beran)" in inventar:
                t="Klíč se znamením berana."
                KOUPELNAV()
        if "lepidlo" in volba:
            if "lepidlo" in inventar:
                t="Silné modelářské lepidlo. Vhodné pro lepení dřeva, plastů i kovu."
                KOUPELNAV()
        if "baterie" in volba:
            if "baterie" in inventar:
                t="Sada tužkových baterií."
                KOUPELNAV()
        if "zapalovač" in volba:
            if "zapalovač" in inventar:
                t="Kvalitní benzínový zapalovač s vyrytým křížem."
                KOUPELNAV()
        if "ručička" in volba:
            if "ručička" in inventar:
                t="Ručička z hodin."
                KOUPELNAV()
        if "klíč(alfa)" in volba:
            if "klíč(ALFA)" in inventar:
                t="Klíč se znamením 'ALFA'."
                KOUPELNAV()
        if "hák" in volba:
            if "hák(zlomený)" in inventar:
                t="Zlomený hák na čištění okapů. V tomhle stavu s ním asi nikam nedosáhneš."
                KOUPELNAV()
            elif "hák(prodloužený)" in inventar:
                t="Hák na čištění okapů prodloužený zlomeným tágem."
                KOUPELNAV()
        if "zbraň" in volba:
            if "zbraň" in inventar:
                t="Nabitá pistole."
                KOUPELNAV()
        if "brousek" in volba:
            if "brousek" in inventar:
                t="Brousek. Vhodný pro ostření nožů."
                KOUPELNAV()
        if "papír" in volba:
            if "papír(citronový)" in inventar:
                t=("Prázdný papír vonící po citrónu.")
                KOUPELNAV()
            if "papír(vzkaz)" in inventar:
                t=("Na papíře je vzkaz hnědým písmem: '232.8°C'")
                KOUPELNAV()
        if "místnost" in volba or "koupelna" in volba: 
            t=("Je to tmavá místnost. Všechna okna jsou zakrytá a vzduch je tu jako v prádelně. Hned za dveřmi v rohu se nachází stará pračka a sušička. Na sušičce svítí červená kontrolka. Za nimi se nachází rozbité umyvadlo. Naproti od tebe je vana a záchodová mísa do kterých od dveří nevidíš.")
            KOUPELNAV()
        if "pračka" in volba:
            t=("Stará pračka. Zespodu výrazně rezavá. Skrz okénko vepředu vidíš, že v ní nic není.")
            KOUPELNAV()
        if "sušička" in volba:
            if susicka==1:
                t=("Stará, sotva funkční sušička. Na panelu svítí červená kontrolka.")
                KOUPELNAV()
            else:
                t=("Tahle sušička už nikdy sušit nebude...")
                KOUPELNAV()
        if "umyvadlo" in volba:
            t=("Rozbité umyvadlo, které rozhodně zažilo lepší časy. Ze zdi nad ním trčí olověná trubka, ze které pokapává rezavá voda.")
            KOUPELNAV()
        if "wc" in volba or "záchod" in volba or "toaleta" in volba:
            if wc==1:
                t=("Špinavá toaletní mísa plná nechutné vody. Při bližším prozkoumání máš pocit že v té vodě něco vidíš.")
                KOUPELNAV()
            else:
                t=("Špinavá toaletní mísa. Odmítáš se na ni dívat déle než nezbytně musíš.")
                KOUPELNAV()
        if "vana" in volba:
            if vana_naplnena==1:
                t=("Špinavá vana plná špinavé vody. Prostě fuj.")
                KOUPELNAV()
            else:
                t=("Prázdná vana. Pořád není nejčistší.")
                KOUPELNAV()
        if "dveře" in volba:
            t=("Dveře vedoucí zpět na chodbu.")
            KOUPELNAV()
    
        else:
            t=("Nevím jak to udělat")
            KOUPELNAV()
    if "použij" in volba:
        if "izolepa" in volba and "tágo(zlomené)" in volba and "hák(zlomený)" in volba:
            if "izolepa" in inventar and "tágo(zlomené)" in inventar and "hák(zlomený)" in inventar:
                t=("Slepil jsi zbytky tága a háku a vyrobil tak prodloužený hák.")
                inventar.remove("tágo(zlomené)")
                inventar.remove("hák(zlomený)")
                inventar.append("hák(prodloužený)")
                KOUPELNAV()
            else:
                t=("Nemáš všechny materiály.")
                KOUPELNAV()
        if "lepidlo" in volba and "polovina klíče gama(a)" in volba and "polovina klíče gama(b)" in volba:
            if "lepidlo" in inventar and "polovina klíče GAMA(A)" in inventar and "polovina klíče GAMA(B)" in inventar:
                t=("Slepil jsi dohromady klíč(GAMA)")
                inventar.remove("polovina klíče GAMA(A)")
                inventar.remove("polovina klíče GAMA(B)")
                inventar.append("klíč(GAMA)")
                KOUPELNAV()
            else:
                t=("Něco ti chybí.")
                KOUPELNAV()
        if "svítilna" in volba and "baterie" in volba:
            if "svítilna(bez baterií)" in inventar and "baterie" in inventar:
                t=("Vložil jsi baterie do svítilny.")
                inventar.remove("svítilna(bez baterií)")
                inventar.remove("baterie")
                inventar.append("svítilna")
                KOUPELNAV()
            else:
                t=("Tady něco schází.")
                KOUPELNAV()
        if "nůž(tupý)" in volba and "brousek" in volba:
            if "nůž(tupý)" in inventar and "brousek" in inventar:
                t=("Naostřil jsi nůž.")
                inventar.remove("nůž(tupý)")
                inventar.append("nůž(ostrý)")
                KOUPELNAV()
            else:
                t=("Něco potřebuješ")
                KOUPELNAV()
        if "dveře" in volba:
            OPT2()
        if "sušička" in volba:
            if susicka==1:
                t=("Stisknul jsi tlačítko u červené kontrolky. Sušička se rozběhla a téměř okamžitě na to se z ní začal ozývat neuvěřitelný hluk. Poté co se zastavila (pravděpodobně nadobro) ses rozhodl ji otevřít. Uvnitř byla pojistka, kterou sis vzal.")
                inventar.append("pojistka")
                susicka=0
                KOUPELNAV()
            else:
                t=("Stisknul jsi tlačítko. Sušička nic neudělala.")
                KOUPELNAV()
        if "wc" in volba or "toaleta" in volba or "záchod" in volba:
            if wc==1:
                t=("Zadržuješ dech, zatínáš zuby a noříš svoji ruku do odporné záchodové vody. Po chvílí pátrání nahmatáš nějaký objekt. Po vytažení se ukázalo že je to klíč. Nebo teda aspoň jeho polovina. Rozhodl ses si ji vzít.")
                inventar.append("polovina klíče GAMA(A)")
                wc=0
                KOUPELNAV()
            else:
                t=("Tam už rozhodně ruku znovu nestrčíš.")
                KOUPELNAV()
        if "vana" in volba:
            if vana_naplnena==1:
                t=("Vytáhl jsi špunt u vany a po nějaké chvíli se všechna voda z vany vypustila. Na dně vany ležela malá vodotěsná svítilna. Po jejím vyzkoušení zjišťuješ, že v ní nejsou baterie, ale stejně si ji raději vezmeš.")
                inventar.append("svítilna(bez baterií)")
                vana_naplnena=0
                KOUPELNAV()
            else:
                t=("Už tu není co dělat.")
                KOUPELNAV()
        else:
            t=("To si nezvládnu.")
    else:
        t=("Tento příkaz neznám: ",volba)
        KOUPELNAV()
#SC06 (Herna)
def HERNAT():
    global t
    t=("Tato místnost se zdá byt herna. \n\nCo uděláš?")
    HERNAV()
def HERNAV():
    global t
    global inventar
    global krb_plamen
    global telo_rozrezane
    global krb_alkohol
    PRINT()
    submit.wait_variable(var)
    volba=wolba.get()
    volba=volba.lower()
    #---------------------DEBUG----------------------
    if "dbg_tutorial_skip" in volba:
        NOVA_HRA()
    if "dbg_op" in volba:
        OPT()
    if "dbg_kuchyne" in volba:
        KUCHYNET()
    if "dbg_koupelna" in volba:
        KOUPELNAT()
    if "dbg_herna" in volba:
        HERNAT()
    if "dbg_knihovna" in volba:
        KNIHOVNAT()
    if "dbg_loznice" in volba:
        LOZNICET()
    if "dbg_balkon" in volba:
        BALKONT()
    if "dbg_puda" in volba:
        PUDAT()
    if "dbg_chodba" in volba:
        CHODBAT()
    if "dbg_inv" in volba:
        volbaa=input("Zadej předmět:")
        inventar.append(volbaa)
    #------------------------------------------------
    if volba=="inventář" or volba=="inventar":
        t=str(inventar)
        HERNAV()
    if "prozkoumej" in volba:
        if "klíč(váhy)" in volba:
            if "klíč(váhy)" in inventar:
                t="Klíč se znamením vah."
                HERNAV()
        if "izolepa" in volba or "lepící páska" in volba:
            if "izolepa" in inventar:
                t="Stříbrná lepící páska, vhodná pro namáhané spoje."
                HERNAV()
        if "nůž" in volba:
            if "nůž(ostrý)" in inventar:
                t="Ostrý kuchyňský nůž. Vhodný pro krájení masa nebo zeleniny."
                HERNAV()
            if "nůž(tupý)" in inventar:
                t="Tupý kuchyňský nůž. Tímhle nic nepřeřízneš."
                HERNAV()
        if "pojistka" in volba:
            if "pojistka" in inventar:
                t="Obyčejná pojistka."
                HERNAV()
        if "polovina klíče" in volba:
            if "polovina klíče 'OMEGA'(A)" in inventar or "polovina klíče 'OMEGA'(B)" in inventar:
                t="Polovina klíče se znamením 'OMEGA'."
                HERNAV()
        if "svítilna" in volba:
            if "svítilna(bez baterií)" in inventar:
                t="Vodotěsná svítilna. Bohužel v ní nejsou baterie."
                HERNAV()
            elif "svítilna" in inventar:
                t="Funkční vodotěsná svítilna."
                HERNAV()
        if "tágo" in volba:
            if "tágo(zlomené)" in inventar:
                t="Kulečníkové tágo. Bohužel je zlomené."
                HERNAV()
        if "klíč(omega)" in volba:
            if "klíč(OMEGA)" in inventar:
                t="Klíč se znamením 'OMEGA'."
                HERNAV()
        if "klíč(beta)" in volba:
            if "klíč(BETA)" in inventar:
                t="Klíč se znamením 'BETA'."
                HERNAV()
        if "klíč(beran)" in volba:
            if "klíč(beran)" in inventar:
                t="Klíč se znamením berana."
                HERNAV()
        if "lepidlo" in volba:
            if "lepidlo" in inventar:
                t="Silné modelářské lepidlo. Vhodné pro lepení dřeva, plastů i kovu."
                HERNAV()
        if "baterie" in volba:
            if "baterie" in inventar:
                t="Sada tužkových baterií."
                HERNAV()
        if "zapalovač" in volba:
            if "zapalovač" in inventar:
                t="Kvalitní benzínový zapalovač s vyrytým křížem."
                HERNAV()
        if "ručička" in volba:
            if "ručička" in inventar:
                t="Ručička z hodin."
                HERNAV()
        if "klíč(alfa)" in volba:
            if "klíč(ALFA)" in inventar:
                t="Klíč se znamením 'ALFA'."
                HERNAV()
        if "hák" in volba:
            if "hák(zlomený)" in inventar:
                t="Zlomený hák na čištění okapů. V tomhle stavu s ním asi nikam nedosáhneš."
                HERNAV()
            elif "hák(prodloužený)" in inventar:
                t="Hák na čištění okapů prodloužený zlomeným tágem."
                HERNAV()
        if "zbraň" in volba:
            if "zbraň" in inventar:
                t="Nabitá pistole."
                HERNAV()
        if "brousek" in volba:
            if "brousek" in inventar:
                t="Brousek. Vhodný pro ostření nožů."
                HERNAV()
        if "papír" in volba:
            if "papír(citronový)" in inventar:
                t=("Prázdný papír vonící po citrónu.")
                HERNAV()
            if "papír(vzkaz)" in inventar:
                t=("Na papíře je vzkaz hnědým písmem: '232.8°C'")
                HERNAV()
        if "místnost" in volba: 
            t=("Uprostřed místnosti se nachází masivní kulečníkový stůl, který už rozhodně zažil lepší časy. U vzdálenější stěny stojí překvapivě zachovalý krb. Hned za dveřmi u stěny je stojan na tága a za kulečníkem na zemi leží nějaký tmavý objekt, který nejsi schopný zcela rozeznat.")
            HERNAV()
        if "objekt" in volba:
            t=("Přiblížíš se k tmavému objektu a k tvému zděšení zjišťuješ že se jedná o lidské tělo.")
            HERNAV()
        if "tělo" in volba:
            if telo_rozrezane==1:
                t=("Rozřezané tělo toho chudáka. Z toho co kdysi bývalo břicho teď vyhřezávají vnitřnosti a celou místnost plní nesnesitelný zápach.")
                HERNAV()
            else:
                t=("Proti veškerému svému odporu se přiblížíš k tělu abys ho prozkoumal. Jedná se o muže středního věku. Příčina smrti se zdá být předávkování, aspoň tak usuzuješ podle prázdných krabiček od léků poházených kolem. Na obou rukách má vypálené kříže. Po bližším ohledání zjišťuješ, že na břiše má nakreslený znak 'BETA'.")
                HERNAV()
        if "kulečník" in volba or "stůl" in volba:
            if "polovina klíče GAMA(B)" in inventar or "klíč(GAMA)" in inventar:
                t=("Masivní kulečníkový stůl. Pravděpodobně z počátku minulého století.")
                HERNAV()
            else:
                t=("Masivní kulečníkový stůl. Pravděpodobně z počátku minulého století. V jedné z děr se něco nachází.")
                HERNAV()
        if "díra" in volba:
            t=("V díře je něco co vypadá jako klíč, ale rukou se ti nedaří ho vytáhnout.")
            HERNAV()
        if "krb" in volba:
            if krb_plamen==1:
                t=("Starý krb, ve kterém hoří mohutný plamen.")
                HERNAV()
            else:
                t=("Starý krb, ve kterém se pravděpodobně často topilo. Je v něm připraveno dřevo na podpal.")
                HERNAV()
        if "stojan" in volba:
            if "tágo(zlomené)" in inventar or "hák(prodloužený)" in inventar:
                t=("Stojan na tága.")
                HERNAV()
            else:
                t=("Stojan na tága, ve kterém stojí jen jedno opuštěné zlomené tágo.")
                HERNAV()
    if "vezmi" in volba:
        if "tágo" in volba:
            if "tágo(zlomené)" in inventar or "hák(prodloužený)" in inventar:
                t=("Nic už tu není.")
                HERNAV()
            else:
                t=("Sebral jsi zlomené tágo.")
                inventar.append("tágo(zlomené)")
                HERNAV()
        else:
            t=("Nevím jak to udělat.")
            HERNAV()
    if "použij" in volba:
        if "izolepa" in volba and "tágo(zlomené)" in volba and "hák(zlomený)" in volba:
            if "izolepa" in inventar and "tágo(zlomené)" in inventar and "hák(zlomený)" in inventar:
                t=("Slepil jsi zbytky tága a háku a vyrobil tak prodloužený hák.")
                inventar.remove("tágo(zlomené)")
                inventar.remove("hák(zlomený)")
                inventar.append("hák(prodloužený)")
                HERNAV()
            else:
                t=("Nemáš všechny materiály.")
                HERNAV()
        if "lepidlo" in volba and "polovina klíče gama(a)" in volba and "polovina klíče gama(b)" in volba:
            if "lepidlo" in inventar and "polovina klíče GAMA(A)" in inventar and "polovina klíče GAMA(B)" in inventar:
                t=("Slepil jsi dohromady klíč(GAMA)")
                inventar.remove("polovina klíče GAMA(A)")
                inventar.remove("polovina klíče GAMA(B)")
                inventar.append("klíč(GAMA)")
                HERNAV()
            else:
                t=("Něco ti chybí.")
                HERNAV()
        if "svítilna" in volba and "baterie" in volba:
            if "svítilna(bez baterií)" in inventar and "baterie" in inventar:
                t=("Vložil jsi baterie do svítilny.")
                inventar.remove("svítilna(bez baterií)")
                inventar.remove("baterie")
                inventar.append("svítilna")
                HERNAV()
            else:
                t=("Tady něco schází.")
                HERNAV()
        if "nůž(tupý)" in volba and "brousek" in volba:
            if "nůž(tupý)" in inventar and "brousek" in inventar:
                t=("Naostřil jsi nůž.")
                inventar.remove("nůž(tupý)")
                inventar.append("nůž(ostrý)")
                HERNAV()
            else:
                t=("Něco potřebuješ")
                HERNAV()
        if "dveře" in volba:
            OPT2()
        if "krb" in volba:
            if krb_plamen==1:
                if "papír" in volba:
                    if "papír(citronový)" in inventar:
                        t=("Díky žáru plamene se na papíře objevil text.")
                        inventar.remove("papír(citronový)")
                        inventar.append("papír(vzkaz)")
                        HERNAV()
                    elif "papír(vzkaz)" in volba:
                        t=("Nevím proč, ale rozhodl ses papír spálit.")
                        inventar.remove("papír(vzkaz)")
                        HERNAV()
                    else:
                        t=("Žádný jiný papír už nemáš.")
                        HERNAV()
                else:
                    t=("To nepůjde.")
                    HERNAV()
            else:
                if "alkohol" in volba:
                    if "alkohol" in inventar:
                        t=("Nalil jsi na dřevo alkohol.")
                        krb_alkohol=1
                        inventar.remove("alkohol")
                        HERNAV()
                    else:
                        t=("Nemáš žádný alkohol.")
                        HERNAV()
                if "zapalovač" in volba:
                    if "zapalovač" in inventar:
                        if krb_alkohol==1:
                            t=("Zapálil jsi dřevo nasáklé alkoholem, které okamžitě vzplanulo.")
                            krb_plamen=1
                            HERNAV()
                        else:
                            t=("Snažíš se dřevo v krbu zapálit, ale nedaří se ti to.")
                            HERNAV()
                    else:
                        t=("Nemáš zapalovač.")
                        HERNAV()
        if "kulečník" in volba or "stůl" in volba or "díra" in volba:
            if "hák" in volba:
                if "hák(zlomený)" in inventar or "hák(prodloužený)"  in inventar:
                    if "klíč(GAMA)" in inventar or "polovina klíče GAMA(B)" in inventar:
                        t=("Nic už tam není.")
                        HERNAV()
                    else:
                        t=("Vytáhl jsi z díry polovinu klíče.")
                        inventar.append("polovina klíče GAMA(B)")
                        HERNAV()
                else:
                    t=("Nemáš žádný hák.")
                    HERNAV()
            else:
                t=("To není možné.")
                HERNAV()
        if "tělo" in volba:
            if "nůž" in volba:
                if "nůž(ostrý)" in inventar:
                    if telo_rozrezane==0:
                        t=("S neuvěřitelným odporem vytahujeě svůj nůž a pomalu řežeě břicho mrtvého. Při prvním kontaktu nože se vyvalilo obrovské množství krve ale ty dále pokračuješ. Když se dostaneš k žaludku nacházíš klíč, který sis vzal.")
                        inventar.append("klíč(BETA)")
                        telo_rozrezane=1
                        HERNAV()
                    else:
                        t=("Už nemáš žádný důvod.")
                        HERNAV()
                else:
                    t=("Nemáš ostrý nůž.")
                    HERNAV()
            else:
                t=("To nezvládnu.")
                HERNAV()
        #Inventář dodělat
    else:
        t=("Tento příkaz neznám: ",volba)
        HERNAV()
#SC07 (Chodba)
def CHODBAT():
    global t
    t=("Jsi na chodbě v druhém patře. \n\nCo uděláš?")
    CHODBAV()
def CHODBAV():
    global t
    global inventar
    global kukacky
    global dvere_beran_zamceno
    global poklop
    PRINT()
    submit.wait_variable(var)
    volba=wolba.get()
    volba=volba.lower()
    #---------------------DEBUG----------------------
    if "dbg_tutorial_skip" in volba:
        NOVA_HRA()
    if "dbg_op" in volba:
        OPT()
    if "dbg_kuchyne" in volba:
        KUCHYNET()
    if "dbg_koupelna" in volba:
        KOUPELNAT()
    if "dbg_herna" in volba:
        HERNAT()
    if "dbg_knihovna" in volba:
        KNIHOVNAT()
    if "dbg_loznice" in volba:
        LOZNICET()
    if "dbg_balkon" in volba:
        BALKONT()
    if "dbg_puda" in volba:
        PUDAT()
    if "dbg_chodba" in volba:
        CHODBAT()
    if "dbg_inv" in volba:
        volbaa=input("Zadej předmět:")
        inventar.append(volbaa)
    #------------------------------------------------
    if volba=="inventář" or volba=="inventar":
        t=str(inventar)
        CHODBAV()
    if "prozkoumej" in volba:
        if "klíč(váhy)" in volba:
            if "klíč(váhy)" in inventar:
                t="Klíč se znamením vah."
                CHODBAV()
        if "izolepa" in volba or "lepící páska" in volba:
            if "izolepa" in inventar:
                t="Stříbrná lepící páska, vhodná pro namáhané spoje."
                CHODBAV()
        if "nůž" in volba:
            if "nůž(ostrý)" in inventar:
                t="Ostrý kuchyňský nůž. Vhodný pro krájení masa nebo zeleniny."
                CHODBAV()
            if "nůž(tupý)" in inventar:
                t="Tupý kuchyňský nůž. Tímhle nic nepřeřízneš."
                CHODBAV()
        if "pojistka" in volba:
            if "pojistka" in inventar:
                t="Obyčejná pojistka."
                CHODBAV()
        if "polovina klíče" in volba:
            if "polovina klíče 'OMEGA'(A)" in inventar or "polovina klíče 'OMEGA'(B)" in inventar:
                t="Polovina klíče se znamením 'OMEGA'."
                CHODBAV()
        if "svítilna" in volba:
            if "svítilna(bez baterií)" in inventar:
                t="Vodotěsná svítilna. Bohužel v ní nejsou baterie."
                CHODBAV()
            elif "svítilna" in inventar:
                t="Funkční vodotěsná svítilna."
                CHODBAV()
        if "tágo" in volba:
            if "tágo(zlomené)" in inventar:
                t="Kulečníkové tágo. Bohužel je zlomené."
                CHODBAV()
        if "klíč(omega)" in volba:
            if "klíč(OMEGA)" in inventar:
                t="Klíč se znamením 'OMEGA'."
                CHODBAV()
        if "klíč(beta)" in volba:
            if "klíč(BETA)" in inventar:
                t="Klíč se znamením 'BETA'."
                CHODBAV()
        if "klíč(beran)" in volba:
            if "klíč(beran)" in inventar:
                t="Klíč se znamením berana."
                CHODBAV()
        if "lepidlo" in volba:
            if "lepidlo" in inventar:
                t="Silné modelářské lepidlo. Vhodné pro lepení dřeva, plastů i kovu."
                CHODBAV()
        if "baterie" in volba:
            if "baterie" in inventar:
                t="Sada tužkových baterií."
                CHODBAV()
        if "zapalovač" in volba:
            if "zapalovač" in inventar:
                t="Kvalitní benzínový zapalovač s vyrytým křížem."
                CHODBAV()
        if "ručička" in volba:
            if "ručička" in inventar:
                t="Ručička z hodin."
                CHODBAV()
        if "klíč(alfa)" in volba:
            if "klíč(ALFA)" in inventar:
                t="Klíč se znamením 'ALFA'."
                CHODBAV()
        if "hák" in volba:
            if "hák(zlomený)" in inventar:
                t="Zlomený hák na čištění okapů. V tomhle stavu s ním asi nikam nedosáhneš."
                CHODBAV()
            elif "hák(prodloužený)" in inventar:
                t="Hák na čištění okapů prodloužený zlomeným tágem."
                CHODBAV()
        if "zbraň" in volba:
            if "zbraň" in inventar:
                t="Nabitá pistole."
                CHODBAV()
        if "brousek" in volba:
            if "brousek" in inventar:
                t="Brousek. Vhodný pro ostření nožů."
                CHODBAV()
        if "papír" in volba:
            if "papír(citronový)" in inventar:
                t=("Prázdný papír vonící po citrónu.")
                CHODBAV()
            if "papír(vzkaz)" in inventar:
                t=("Na papíře je vzkaz hnědým písmem: '232.8°C'")
                CHODBAV()
        if "místnost" in volba: 
            t=("Nacházíš se v podlouhlé chodbě. Na stěně naproti schodišti visí staré kukačky. Nalevo od nich jsou dveře vedoucí na balkón a okno proražené větví. Napravo jsou dvoje dveře. Jedny na sobě mají znak berana, ty druhé vedou do ložnice. Na stropě mezi těmito dveřmi je poklop s otvorem na otevření.")
            CHODBAV()
        if "kukačky" in volba:
            if kukacky==1:
                t=("Staré kukačky. Nic zvláštního.")
                CHODBAV()
            else:
                t=("Staré kukačky. Chybí jim minutová ručička.")
                CHODBAV()
        if "okno" in volba:
            t=("Okno je proražené větví stromu. Zdá se, že by se po této větvi dalo přelézt na balkón")
            CHODBAV()
    if "použij" in volba:
        if "izolepa" in volba and "tágo(zlomené)" in volba and "hák(zlomený)" in volba:
            if "izolepa" in inventar and "tágo(zlomené)" in inventar and "hák(zlomený)" in inventar:
                t=("Slepil jsi zbytky tága a háku a vyrobil tak prodloužený hák.")
                inventar.remove("tágo(zlomené)")
                inventar.remove("hák(zlomený)")
                inventar.append("hák(prodloužený)")
                CHODBAV()
            else:
                t=("Nemáš všechny materiály.")
                CHODBAV()
        if "lepidlo" in volba and "polovina klíče gama(a)" in volba and "polovina klíče gama(b)" in volba:
            if "lepidlo" in inventar and "polovina klíče GAMA(A)" in inventar and "polovina klíče GAMA(B)" in inventar:
                t=("Slepil jsi dohromady klíč(GAMA)")
                inventar.remove("polovina klíče GAMA(A)")
                inventar.remove("polovina klíče GAMA(B)")
                inventar.append("klíč(GAMA)")
                CHODBAV()
            else:
                t=("Něco ti chybí.")
                CHODBAV()
        if "svítilna" in volba and "baterie" in volba:
            if "svítilna(bez baterií)" in inventar and "baterie" in inventar:
                t=("Vložil jsi baterie do svítilny.")
                inventar.remove("svítilna(bez baterií)")
                inventar.remove("baterie")
                inventar.append("svítilna")
                CHODBAV()
            else:
                t=("Tady něco schází.")
                CHODBAV()
        if "nůž(tupý)" in volba and "brousek" in volba:
            if "nůž(tupý)" in inventar and "brousek" in inventar:
                t=("Naostřil jsi nůž.")
                inventar.remove("nůž(tupý)")
                inventar.append("nůž(ostrý)")
                CHODBAV()
            else:
                t=("Něco potřebuješ")
                CHODBAV()
        if "dveře" in volba:
            if "ložnice" in volba:
                LOZNICET()
            if "balkon" in volba:
                t=("Dveře jsou zablokované spadlou větví.")
                CHODBAV()
            if "beran" in volba or "knihovna" in volba:
                if dvere_beran_zamceno==1:
                    if "klíč(beran)" in volba:
                        if "klíč(beran)" in inventar:
                            t=("Odemkl jsi dveře se znamením berana.")
                            dvere_beran_zamceno=0
                            CHODBAV()
                        else:
                            t=("Nemáš patřičný klíč.")
                            CHODBAV()
                    else:
                        t=("Dveře jsou zamčené.")
                        CHODBAV()
                else:
                    KNIHOVNAT()
        if "okno" in volba:
            t=("Přelezl jsi po větvi stromu na balkón.")
            BALKONT()
        if "schody" in volba:
            OPT2()
        if "poklop" in volba:
            if poklop==0:
                if "hák" in volba:
                    if "hák(prodloužený)" in inventar:
                        t=("Odklopil jsi poklop a dolů se spustily schody na půdu.")
                        poklop=1
                        CHODBAV()
                    else:
                        t=("Nemáš dostatečně dlouhý nástroj.")
                        CHODBAV()
                else:
                    t=("Poklop je zavřený.")
                    CHODBAV()
            else:
                PUDAT()
        if "kukačky" in volba:
            if "ručička" in volba:
                if "ručička" in inventar:
                    t=("Zasadil jsi ručičku do hodin a nastavil 12 hodin. Místo kukačky na rameni vyjel klíč se znamením berana, který sis k sobě vzal.")
                    inventar.append("klíč(beran)")
                    inventar.remove("ručička")
                    kukacky=1
                    CHODBAV()
                else:
                    t=("Nemáš žádnou ručičku.")
                    CHODBAV()
            else:
                t=("To nepůjde.")
                CHODBAV()
    else:
        t=("Tento příkaz neznám: ",volba)
        CHODBAV()
#SC08 (Ložnice)
def LOZNICET():
    global t
    t=("Jsi v ložnici. \n\nCo uděláš?")
    LOZNICEV()
def LOZNICEV():
    global t
    global inventar
    global kukacky
    PRINT()
    submit.wait_variable(var)
    volba=wolba.get()
    volba=volba.lower()
    #---------------------DEBUG----------------------
    if "dbg_tutorial_skip" in volba:
        NOVA_HRA()
    if "dbg_op" in volba:
        OPT()
    if "dbg_kuchyne" in volba:
        KUCHYNET()
    if "dbg_koupelna" in volba:
        KOUPELNAT()
    if "dbg_herna" in volba:
        HERNAT()
    if "dbg_knihovna" in volba:
        KNIHOVNAT()
    if "dbg_loznice" in volba:
        LOZNICET()
    if "dbg_balkon" in volba:
        BALKONT()
    if "dbg_puda" in volba:
        PUDAT()
    if "dbg_chodba" in volba:
        CHODBAT()
    if "dbg_inv" in volba:
        volbaa=input("Zadej předmět:")
        inventar.append(volbaa)
    #------------------------------------------------
    if volba=="inventář" or volba=="inventar":
        t=str(inventar)
        LOZNICEV()
    if "prozkoumej" in volba:
        if "klíč(váhy)" in volba:
            if "klíč(váhy)" in inventar:
                t="Klíč se znamením vah."
                LOZNICEV()
        if "izolepa" in volba or "lepící páska" in volba:
            if "izolepa" in inventar:
                t="Stříbrná lepící páska, vhodná pro namáhané spoje."
                LOZNICEV()
        if "nůž" in volba:
            if "nůž(ostrý)" in inventar:
                t="Ostrý kuchyňský nůž. Vhodný pro krájení masa nebo zeleniny."
                LOZNICEV()
            if "nůž(tupý)" in inventar:
                t="Tupý kuchyňský nůž. Tímhle nic nepřeřízneš."
                LOZNICEV()
        if "pojistka" in volba:
            if "pojistka" in inventar:
                t="Obyčejná pojistka."
                LOZNICEV()
        if "polovina klíče" in volba:
            if "polovina klíče 'OMEGA'(A)" in inventar or "polovina klíče 'OMEGA'(B)" in inventar:
                t="Polovina klíče se znamením 'OMEGA'."
                LOZNICEV()
        if "svítilna" in volba:
            if "svítilna(bez baterií)" in inventar:
                t="Vodotěsná svítilna. Bohužel v ní nejsou baterie."
                LOZNICEV()
            elif "svítilna" in inventar:
                t="Funkční vodotěsná svítilna."
                LOZNICEV()
        if "tágo" in volba:
            if "tágo(zlomené)" in inventar:
                t="Kulečníkové tágo. Bohužel je zlomené."
                LOZNICEV()
        if "klíč(omega)" in volba:
            if "klíč(OMEGA)" in inventar:
                t="Klíč se znamením 'OMEGA'."
                LOZNICEV()
        if "klíč(beta)" in volba:
            if "klíč(BETA)" in inventar:
                t="Klíč se znamením 'BETA'."
                LOZNICEV()
        if "klíč(beran)" in volba:
            if "klíč(beran)" in inventar:
                t="Klíč se znamením berana."
                LOZNICEV()
        if "lepidlo" in volba:
            if "lepidlo" in inventar:
                t="Silné modelářské lepidlo. Vhodné pro lepení dřeva, plastů i kovu."
                LOZNICEV()
        if "baterie" in volba:
            if "baterie" in inventar:
                t="Sada tužkových baterií."
                LOZNICEV()
        if "zapalovač" in volba:
            if "zapalovač" in inventar:
                t="Kvalitní benzínový zapalovač s vyrytým křížem."
                LOZNICEV()
        if "ručička" in volba:
            if "ručička" in inventar:
                t="Ručička z hodin."
                LOZNICEV()
        if "klíč(alfa)" in volba:
            if "klíč(ALFA)" in inventar:
                t="Klíč se znamením 'ALFA'."
                LOZNICEV()
        if "hák" in volba:
            if "hák(zlomený)" in inventar:
                t="Zlomený hák na čištění okapů. V tomhle stavu s ním asi nikam nedosáhneš."
                LOZNICEV()
            elif "hák(prodloužený)" in inventar:
                t="Hák na čištění okapů prodloužený zlomeným tágem."
                LOZNICEV()
        if "zbraň" in volba:
            if "zbraň" in inventar:
                t="Nabitá pistole."
                LOZNICEV()
        if "brousek" in volba:
            if "brousek" in inventar:
                t="Brousek. Vhodný pro ostření nožů."
                LOZNICEV()
        if "papír" in volba:
            if "papír(citronový)" in inventar:
                t=("Prázdný papír vonící po citrónu.")
                LOZNICEV()
            if "papír(vzkaz)" in inventar:
                t=("Na papíře je vzkaz hnědým písmem: '232.8°C'")
                LOZNICEV()
        if "místnost" in volba: 
            t=("Celkem velká ložnice. Nalevo od vchodu je vitrína s modely letadel a šuplíky pod nimi. Naproti tobě pak leží rozbité hodiny. Napravo od vchodu je postel a noční stolek.")
            LOZNICEV()
        if "stolek" in volba:
            if "zapalovač" in inventar:
                t=("Na stolku už nic není.")
                LOZNICEV()
            else:
                t=("Na stolku leží zapalovač a cigarety. Majitel domu je pravděpodobně těžký kuřák.")
                LOZNICEV()
        if "zapalovač" in volba:
            t=("Benzínový zapalovač. Je na něm vyrytý kříž.")
            LOZNICEV()
        if "postel" in volba:
            t=("Velká postel pro dva lidi. Jen jedna polovina se zdá být používána.")
            LOZNICEV()
        if "vitrína" in volba:
            t=("Velká skleněná vitrína. V poličkách jsou různé modely letadel. Pod nimi se nachází několik šuplíků.")
            LOZNICEV()
        if "šuplíky" in volba or "šuplík" in volba:
            if "lepidlo" in inventar:
                t=("V šuplících už nic není.")
                LOZNICEV()
            else:
                t=("V jednom z šuplíků jsi našel modelářské lepidlo a sadu baterií.")
                inventar.append("lepidlo")
                inventar.append("baterie")
                LOZNICEV()
        if "hodiny" in volba:
            if "ručička" in inventar:
                t=("Rozbité hodiny. Nic zajimavého.")
                LOZNICEV()
            else:
                t=("Rozbité hodiny. Kousek od nich leží vypadlá ručička.")
                LOZNICEV()
    if "vezmi" in volba:
        if "zapalovač" in volba:
            if "zapalovač" in inventar:
                t=("Zapalovač už máš v inventáři.")
                LOZNICEV()
            else:
                t=("Vzal sis k sobě zapalovač.")
                inventar.append("zapalovač")
                LOZNICEV()
        if "ručička" in volba:
            if "ručička" in inventar or kukacky==1:
                t=("Žádná další ručička už tu není.")
                LOZNICEV()
            else:
                t=("Vzal sis k sobě ručičku od hodin.")
                inventar.append("ručička")
                LOZNICEV()
        else:
            t=("Nevím jak to udělat")
            LOZNICEV()
    if "použij" in volba:
        if "izolepa" in volba and "tágo(zlomené)" in volba and "hák(zlomený)" in volba:
            if "izolepa" in inventar and "tágo(zlomené)" in inventar and "hák(zlomený)" in inventar:
                t=("Slepil jsi zbytky tága a háku a vyrobil tak prodloužený hák.")
                inventar.remove("tágo(zlomené)")
                inventar.remove("hák(zlomený)")
                inventar.append("hák(prodloužený)")
                LOZNICEV()
            else:
                t=("Nemáš všechny materiály.")
                LOZNICEV()
        if "lepidlo" in volba and "polovina klíče gama(a)" in volba and "polovina klíče gama(b)" in volba:
            if "lepidlo" in inventar and "polovina klíče GAMA(A)" in inventar and "polovina klíče GAMA(B)" in inventar:
                t=("Slepil jsi dohromady klíč(GAMA)")
                inventar.remove("polovina klíče GAMA(A)")
                inventar.remove("polovina klíče GAMA(B)")
                inventar.append("klíč(GAMA)")
                LOZNICEV()
            else:
                t=("Něco ti chybí.")
                LOZNICEV()
        if "svítilna" in volba and "baterie" in volba:
            if "svítilna(bez baterií)" in inventar and "baterie" in inventar:
                t=("Vložil jsi baterie do svítilny.")
                inventar.remove("svítilna(bez baterií)")
                inventar.remove("baterie")
                inventar.append("svítilna")
                LOZNICEV()
            else:
                t=("Tady něco schází.")
                LOZNICEV()
        if "nůž(tupý)" in volba and "brousek" in volba:
            if "nůž(tupý)" in inventar and "brousek" in inventar:
                t=("Naostřil jsi nůž.")
                inventar.remove("nůž(tupý)")
                inventar.append("nůž(ostrý)")
                LOZNICEV()
            else:
                t=("Něco potřebuješ")
                LOZNICEV()
        if "dveře" in volba:
            CHODBAT()
    else:
        t=("Tento příkaz neznám: ",volba)
        LOZNICEV()
#SC09 (Knihovna)
def KNIHOVNAT():
    global t
    t=("Nacháziš se v místnosti, která slouží jako knihovna. \n\nCo uděláš?")
    KNIHOVNAV()
def KNIHOVNAV():
    global t
    global inventar
    global PC
    PRINT()
    submit.wait_variable(var)
    volba=wolba.get()
    volba=volba.lower()
    #---------------------DEBUG----------------------
    if "dbg_tutorial_skip" in volba:
        NOVA_HRA()
    if "dbg_op" in volba:
        OPT()
    if "dbg_kuchyne" in volba:
        KUCHYNET()
    if "dbg_koupelna" in volba:
        KOUPELNAT()
    if "dbg_herna" in volba:
        HERNAT()
    if "dbg_knihovna" in volba:
        KNIHOVNAT()
    if "dbg_loznice" in volba:
        LOZNICET()
    if "dbg_balkon" in volba:
        BALKONT()
    if "dbg_puda" in volba:
        PUDAT()
    if "dbg_chodba" in volba:
        CHODBAT()
    if "dbg_inv" in volba:
        volbaa=input("Zadej předmět:")
        inventar.append(volbaa)
    #------------------------------------------------
    if volba=="inventář" or volba=="inventar":
        t=str(inventar)
        KNIHOVNAV()
    if "prozkoumej" in volba:
        if "klíč(váhy)" in volba:
            if "klíč(váhy)" in inventar:
                t="Klíč se znamením vah."
                KNIHOVNAV()
        if "izolepa" in volba or "lepící páska" in volba:
            if "izolepa" in inventar:
                t="Stříbrná lepící páska, vhodná pro namáhané spoje."
                KNIHOVNAV()
        if "nůž" in volba:
            if "nůž(ostrý)" in inventar:
                t="Ostrý kuchyňský nůž. Vhodný pro krájení masa nebo zeleniny."
                KNIHOVNAV()
            if "nůž(tupý)" in inventar:
                t="Tupý kuchyňský nůž. Tímhle nic nepřeřízneš."
                KNIHOVNAV()
        if "pojistka" in volba:
            if "pojistka" in inventar:
                t="Obyčejná pojistka."
                KNIHOVNAV()
        if "polovina klíče" in volba:
            if "polovina klíče 'OMEGA'(A)" in inventar or "polovina klíče 'OMEGA'(B)" in inventar:
                t="Polovina klíče se znamením 'OMEGA'."
                KNIHOVNAV()
        if "svítilna" in volba:
            if "svítilna(bez baterií)" in inventar:
                t="Vodotěsná svítilna. Bohužel v ní nejsou baterie."
                KNIHOVNAV()
            elif "svítilna" in inventar:
                t="Funkční vodotěsná svítilna."
                KNIHOVNAV()
        if "tágo" in volba:
            if "tágo(zlomené)" in inventar:
                t="Kulečníkové tágo. Bohužel je zlomené."
                KNIHOVNAV()
        if "klíč(omega)" in volba:
            if "klíč(OMEGA)" in inventar:
                t="Klíč se znamením 'OMEGA'."
                KNIHOVNAV()
        if "klíč(beta)" in volba:
            if "klíč(BETA)" in inventar:
                t="Klíč se znamením 'BETA'."
                KNIHOVNAV()
        if "klíč(beran)" in volba:
            if "klíč(beran)" in inventar:
                t="Klíč se znamením berana."
                KNIHOVNAV()
        if "lepidlo" in volba:
            if "lepidlo" in inventar:
                t="Silné modelářské lepidlo. Vhodné pro lepení dřeva, plastů i kovu."
                KNIHOVNAV()
        if "baterie" in volba:
            if "baterie" in inventar:
                t="Sada tužkových baterií."
                KNIHOVNAV()
        if "zapalovač" in volba:
            if "zapalovač" in inventar:
                t="Kvalitní benzínový zapalovač s vyrytým křížem."
                KNIHOVNAV()
        if "ručička" in volba:
            if "ručička" in inventar:
                t="Ručička z hodin."
                KNIHOVNAV()
        if "klíč(alfa)" in volba:
            if "klíč(ALFA)" in inventar:
                t="Klíč se znamením 'ALFA'."
                KNIHOVNAV()
        if "hák" in volba:
            if "hák(zlomený)" in inventar:
                t="Zlomený hák na čištění okapů. V tomhle stavu s ním asi nikam nedosáhneš."
                KNIHOVNAV()
            elif "hák(prodloužený)" in inventar:
                t="Hák na čištění okapů prodloužený zlomeným tágem."
                KNIHOVNAV()
        if "zbraň" in volba:
            if "zbraň" in inventar:
                t="Nabitá pistole."
                KNIHOVNAV()
        if "brousek" in volba:
            if "brousek" in inventar:
                t="Brousek. Vhodný pro ostření nožů."
                KNIHOVNAV()
        if "papír" in volba:
            if "papír(citronový)" in inventar:
                t=("Prázdný papír vonící po citrónu.")
                KNIHOVNAV()
            if "papír(vzkaz)" in inventar:
                t=("Na papíře je vzkaz hnědým písmem: '232.8°C'")
                KNIHOVNAV()
        if "místnost" in volba: 
            t=("Pravděpodobně často používaná knihovna/pracovna. Naproti dveří je stůl s počítačem obklopený knihovnami po obou stranách.")
            KNIHOVNAV()
        if "knihovna" in volba:
            t=("Knihovna plná knih od všech možných autorů ze všech možných období. Možná by se tu dalo najít něco zajimavého.")
            KNIHOVNAV()
        if "stůl" in volba:
            t=("Starý dřevěný stůl na kterém je zapnutý počítač a podivný vzkaz.")
            KNIHOVNAV()
        if "počítač" in volba or "pc" in volba:
            if PC==0:
                t=("Zapnutý počítač. Na obrazovce je kolonka pro heslo a pod ní text: 'W. Shakespeare 1603'")
                KNIHOVNAV()
            else:
                t=("Na obrazovce je fotka trezoru s popiskem: R. 'Smithova *++*'.")
                KNIHOVNAV()
        if "vzkaz" in volba or "lístek" in volba:
            t=("Na lístku je napsáno : 'Dobrotivý bůh se neohlíží na naše omyly, jestliže způsobují věci, které sami nemůžeme poznat.' a obrázek znaku 'alfa'")
            KNIHOVNAV()          
    if "použij" in volba:
        if "izolepa" in volba and "tágo(zlomené)" in volba and "hák(zlomený)" in volba:
            if "izolepa" in inventar and "tágo(zlomené)" in inventar and "hák(zlomený)" in inventar:
                t=("Slepil jsi zbytky tága a háku a vyrobil tak prodloužený hák.")
                inventar.remove("tágo(zlomené)")
                inventar.remove("hák(zlomený)")
                inventar.append("hák(prodloužený)")
                KNIHOVNAV()
            else:
                t=("Nemáš všechny materiály.")
                KNIHOVNAV()
        if "lepidlo" in volba and "polovina klíče gama(a)" in volba and "polovina klíče gama(b)" in volba:
            if "lepidlo" in inventar and "polovina klíče GAMA(A)" in inventar and "polovina klíče GAMA(B)" in inventar:
                t=("Slepil jsi dohromady klíč(GAMA)")
                inventar.remove("polovina klíče GAMA(A)")
                inventar.remove("polovina klíče GAMA(B)")
                inventar.append("klíč(GAMA)")
                KNIHOVNAV()
            else:
                t=("Něco ti chybí.")
                KNIHOVNAV()
        if "svítilna" in volba and "baterie" in volba:
            if "svítilna(bez baterií)" in inventar and "baterie" in inventar:
                t=("Vložil jsi baterie do svítilny.")
                inventar.remove("svítilna(bez baterií)")
                inventar.remove("baterie")
                inventar.append("svítilna")
                KNIHOVNAV()
            else:
                t=("Tady něco schází.")
                KNIHOVNAV()
        if "nůž(tupý)" in volba and "brousek" in volba:
            if "nůž(tupý)" in inventar and "brousek" in inventar:
                t=("Naostřil jsi nůž.")
                inventar.remove("nůž(tupý)")
                inventar.append("nůž(ostrý)")
                KNIHOVNAV()
            else:
                t=("Něco potřebuješ")
                KNIHOVNAV()
        if "dveře" in volba:
            CHODBAT()
        if "pc" in volba or "počítač" in volba:
            if PC==0:
                t="Zadejte heslo:"
                PRINT()
                submit.wait_variable(var)
                passw=wolba.get()
                if passw=="Hamlet":
                    t=("Počítač se odemkl.")
                    PC=1
                    KNIHOVNAV()
                else:
                    t=("Špatné heslo")
                    KNIHOVNAV()
            else:
                t=("Na tomto počítači už není nic jiného.")
                KNIHOVNAV()
        if "knihovna" in volba:
            t="Jakou knihu hledáš? (Pro konec nech řádku prázdnou):"
            PRINT()
            submit.wait_variable(var)
            kniha=wolba.get()
            if kniha=="Dekameron":
                if "klíč(alfa)" in inventar:
                    t=("Ačkoliv se jedná o opravdu mistrovské dílo, nic víc už v něm není.")
                    KNIHOVNAV()
                else:
                    t=("Otevřel jsi toto mistrovské dílo a vypadl z něj klíč se znakem 'alfa'. Rozhodl ses si tento klíč vzít.")
                    inventar.append("klíč(ALFA)")
                    KNIHOVNAV()
            if kniha=="":
                KNIHOVNAV()
            if kniha=="Canterburské Povídky" or kniha=="canterburské povídky" or kniha=="Canterburské povídky":
                t=("Očividně jen levná kopie Dekameronu.")
                KNIHOVNAV()
            else:
                t=("Na této knize není nic zajimavého.")
                KNIHOVNAV()
    else:
        t=("Tento příkaz neznám: ",volba)
        KNIHOVNAV()
#SC10 (Balkón)
def BALKONT():
    global t
    t=("Jsi na balkóně. \n\nCo uděláš?")
    BALKONV()
def BALKONV():
    global t
    global inventar
    PRINT()
    submit.wait_variable(var)
    volba=wolba.get()
    volba=volba.lower()
    #---------------------DEBUG----------------------
    if "dbg_tutorial_skip" in volba:
        NOVA_HRA()
    if "dbg_op" in volba:
        OPT()
    if "dbg_kuchyne" in volba:
        KUCHYNET()
    if "dbg_koupelna" in volba:
        KOUPELNAT()
    if "dbg_herna" in volba:
        HERNAT()
    if "dbg_knihovna" in volba:
        KNIHOVNAT()
    if "dbg_loznice" in volba:
        LOZNICET()
    if "dbg_balkon" in volba:
        BALKONT()
    if "dbg_puda" in volba:
        PUDAT()
    if "dbg_chodba" in volba:
        CHODBAT()
    if "dbg_inv" in volba:
        volbaa=input("Zadej předmět:")
        inventar.append(volbaa)
    #------------------------------------------------
    if volba=="inventář" or volba=="inventar":
        t=str(inventar)
        BALKONV()
    if "prozkoumej" in volba:
        if "klíč(váhy)" in volba:
            if "klíč(váhy)" in inventar:
                t="Klíč se znamením vah."
                BALKONV()
        if "izolepa" in volba or "lepící páska" in volba:
            if "izolepa" in inventar:
                t="Stříbrná lepící páska, vhodná pro namáhané spoje."
                BALKONV()
        if "nůž" in volba:
            if "nůž(ostrý)" in inventar:
                t="Ostrý kuchyňský nůž. Vhodný pro krájení masa nebo zeleniny."
                BALKONV()
            if "nůž(tupý)" in inventar:
                t="Tupý kuchyňský nůž. Tímhle nic nepřeřízneš."
                BALKONV()
        if "pojistka" in volba:
            if "pojistka" in inventar:
                t="Obyčejná pojistka."
                BALKONV()
        if "polovina klíče" in volba:
            if "polovina klíče 'OMEGA'(A)" in inventar or "polovina klíče 'OMEGA'(B)" in inventar:
                t="Polovina klíče se znamením 'OMEGA'."
                BALKONV()
        if "svítilna" in volba:
            if "svítilna(bez baterií)" in inventar:
                t="Vodotěsná svítilna. Bohužel v ní nejsou baterie."
                BALKONV()
            elif "svítilna" in inventar:
                t="Funkční vodotěsná svítilna."
                BALKONV()
        if "tágo" in volba:
            if "tágo(zlomené)" in inventar:
                t="Kulečníkové tágo. Bohužel je zlomené."
                BALKONV()
        if "klíč(omega)" in volba:
            if "klíč(OMEGA)" in inventar:
                t="Klíč se znamením 'OMEGA'."
                BALKONV()
        if "klíč(beta)" in volba:
            if "klíč(BETA)" in inventar:
                t="Klíč se znamením 'BETA'."
                BALKONV()
        if "klíč(beran)" in volba:
            if "klíč(beran)" in inventar:
                t="Klíč se znamením berana."
                BALKONV()
        if "lepidlo" in volba:
            if "lepidlo" in inventar:
                t="Silné modelářské lepidlo. Vhodné pro lepení dřeva, plastů i kovu."
                BALKONV()
        if "baterie" in volba:
            if "baterie" in inventar:
                t="Sada tužkových baterií."
                BALKONV()
        if "zapalovač" in volba:
            if "zapalovač" in inventar:
                t="Kvalitní benzínový zapalovač s vyrytým křížem."
                BALKONV()
        if "ručička" in volba:
            if "ručička" in inventar:
                t="Ručička z hodin."
                BALKONV()
        if "klíč(alfa)" in volba:
            if "klíč(ALFA)" in inventar:
                t="Klíč se znamením 'ALFA'."
                BALKONV()
        if "hák" in volba:
            if "hák(zlomený)" in inventar:
                t="Zlomený hák na čištění okapů. V tomhle stavu s ním asi nikam nedosáhneš."
                BALKONV()
            elif "hák(prodloužený)" in inventar:
                t="Hák na čištění okapů prodloužený zlomeným tágem."
                BALKONV()
        if "zbraň" in volba:
            if "zbraň" in inventar:
                t="Nabitá pistole."
                BALKONV()
        if "brousek" in volba:
            if "brousek" in inventar:
                t="Brousek. Vhodný pro ostření nožů."
                BALKONV()
        if "papír" in volba:
            if "papír(citronový)" in inventar:
                t=("Prázdný papír vonící po citrónu.")
                BALKONV()
            if "papír(vzkaz)" in inventar:
                t=("Na papíře je vzkaz hnědým písmem: '232.8°C'")
                BALKONV()
        if "místnost" in volba or "balkón" in volba or "balkon" in volba:
            if "hák(zlomený)" in inventar or "hák(prodloužený)" in inventar:
                t=("Nacházíš se na balkóně. Je tu sice hezký výhled, ale jinak tu skoro nic není. Ze starého okapu teče voda, možná je ucpaný. Dveře blokuje větev po které ses sem dostal.")
                BALKONV()
            else:
                t=("Nacházíš se na balkóně. Je tu sice hezký výhled, ale jinak tu skoro nic není. Ze starého okapu teče voda, možná je ucpaný. V rohu je opřený zlomený hák na čištění okapů. Dveře blokuje větev po které ses sem dostal.")
                BALKONV()
        if "hák" in volba:
            if "hák(zlomený)" in inventar:
                t=("Zlomený hák na čištění okapů. Moc krátký na to abys s ním kamkoliv dosáhl.")
                BALKONV()
            elif "hák(prodloužený)" in inventar:
                t=("Hák na čištění okapů prodloužený zlomeným tágem.")
                BALKONV()
            else:
                t=("Zlomený hák na čištění okapů. Moc krátký na to abys s ním kamkoliv dosáhl.")
                BALKONV()
        if "okap" in volba or "rýna" in volba:
            if "zbraň" in inventar:
                t=("Normální okap. Skrz díry z něj teče voda.")
                BALKONV()
            else:
                t=("Starý okap ze kterého vytéká voda kvůli nějaké překážce.")
                BALKONV()
        if "dveře" in volba:
            t=("Dveře vedoucí do domu jsou zablokované spadenou větví.")
            BALKONV()
        if "větev" in volba:
            t=("Spadená větev po které je možné přelézt zpět do domu.")
            BALKONV()
    if "vezmi" in volba:
        if "hák" in volba:
            if "hák(zlomený)" in inventar or "hák(prodloužený)" in inventar:
                t=("Hák už máš v inventáři.")
                BALKONV()
            else:
                t=("Vzal sis zlomený hák")
                inventar.append("hák(zlomený)")
                BALKONV()
        else:
            t=("Nevím jak to udělat")
            BALKONV()
    if "použij" in volba:
        if "izolepa" in volba and "tágo(zlomené)" in volba and "hák(zlomený)" in volba:
            if "izolepa" in inventar and "tágo(zlomené)" in inventar and "hák(zlomený)" in inventar:
                t=("Slepil jsi zbytky tága a háku a vyrobil tak prodloužený hák.")
                inventar.remove("tágo(zlomené)")
                inventar.remove("hák(zlomený)")
                inventar.append("hák(prodloužený)")
                BALKONV()
            else:
                t=("Nemáš všechny materiály.")
                BALKONV()
        if "lepidlo" in volba and "polovina klíče gama(a)" in volba and "polovina klíče gama(b)" in volba:
            if "lepidlo" in inventar and "polovina klíče GAMA(A)" in inventar and "polovina klíče GAMA(B)" in inventar:
                t=("Slepil jsi dohromady klíč(GAMA)")
                inventar.remove("polovina klíče GAMA(A)")
                inventar.remove("polovina klíče GAMA(B)")
                inventar.append("klíč(GAMA)")
                BALKONV()
            else:
                t=("Něco ti chybí.")
                BALKONV()
        if "svítilna" in volba and "baterie" in volba:
            if "svítilna(bez baterií)" in inventar and "baterie" in inventar:
                t=("Vložil jsi baterie do svítilny.")
                inventar.remove("svítilna(bez baterií)")
                inventar.remove("baterie")
                inventar.append("svítilna")
                BALKONV()
            else:
                t=("Tady něco schází.")
                BALKONV()
        if "nůž(tupý)" in volba and "brousek" in volba:
            if "nůž(tupý)" in inventar and "brousek" in inventar:
                t=("Naostřil jsi nůž.")
                inventar.remove("nůž(tupý)")
                inventar.append("nůž(ostrý)")
                BALKONV()
            else:
                t=("Něco potřebuješ")
                BALKONV()
        if "okno" in volba or "větev" in volba:
            CHODBAT()
    if "okap" in volba or "rýna" in volba:
        if "hák" in volba:
            if "hák(prodloužený)" in inventar:
                t=("Použil jsi svůj prodloužený hák a vystrčil z okapu neznámý předmět. Zdá se že se jedná o nabitou zbraň. Rozhodl ses vzít si ji k sobě.")
                inventar.append("zbraň")
                BALKONV()
            else:
                t=("Nemáš dostatečně dlouhý nástroj abys okap vyčistil.")
                BALKONV()
        else:
            t=("Tohle nebude fungovat.")
            BALKONV()
    else:
        t=("Tento příkaz neznám: ",volba)
        BALKONV()
#SC11 (Půda)
def PUDAT():
    global t
    global svitilna
    if svitilna==1:
        t=("Nacházíš se na půdě. \n\nCo uděláš?")
    else:
        t=("Nacházíš se na půdě. Je tu hrozná tma a nic nevidíš. \n\nCo uděláš?")
    PUDAV()
def PUDAV():
    global t
    global inventar
    global svitilna
    global skrin
    PRINT()
    submit.wait_variable(var)
    volba=wolba.get()
    volba=volba.lower()
    #---------------------DEBUG----------------------
    if "dbg_tutorial_skip" in volba:
        NOVA_HRA()
    if "dbg_op" in volba:
        OPT()
    if "dbg_kuchyne" in volba:
        KUCHYNET()
    if "dbg_koupelna" in volba:
        KOUPELNAT()
    if "dbg_herna" in volba:
        HERNAT()
    if "dbg_knihovna" in volba:
        KNIHOVNAT()
    if "dbg_loznice" in volba:
        LOZNICET()
    if "dbg_balkon" in volba:
        BALKONT()
    if "dbg_puda" in volba:
        PUDAT()
    if "dbg_chodba" in volba:
        CHODBAT()
    if "dbg_inv" in volba:
        volbaa=input("Zadej předmět:")
        inventar.append(volbaa)
    #------------------------------------------------
    if volba=="inventář" or volba=="inventar":
        t=str(inventar)
        PUDAV()
    if volba:
        if svitilna==0:
            if "použij" in volba:
                if "svítilna" in volba:
                    if "svítilna" in inventar:
                        t=("Svítilna se naštěstí opravdu rozsvítila a s její pomocí už vidíš vše co potřebuješ.")
                        svitilna=1
                        PUDAV()
                    else:
                        t=("Nemáš si jak posvítit.")
                        PUDAV()
                if "poklop" in volba or "dveře" in volba:
                    CHODBAT()
                else:
                    t=("To ti asi teď nepomůže.")
                    PUDAV()
            else:
                t=("Nevidíš si ani na špičku nosu. Tohle nezvládneš")
                PUDAV()
            t=("Je moc tma na to abys cokoliv rozeznal.")
            PUDAV()
        
        else:
            if "prozkoumej" in volba:
                if "klíč(váhy)" in volba:
                    if "klíč(váhy)" in inventar:
                        t="Klíč se znamením vah."
                        PUDAV()
                if "izolepa" in volba or "lepící páska" in volba:
                    if "izolepa" in inventar:
                        t="Stříbrná lepící páska, vhodná pro namáhané spoje."
                        PUDAV()
                if "nůž" in volba:
                    if "nůž(ostrý)" in inventar:
                        t="Ostrý kuchyňský nůž. Vhodný pro krájení masa nebo zeleniny."
                        PUDAV()
                    if "nůž(tupý)" in inventar:
                        t="Tupý kuchyňský nůž. Tímhle nic nepřeřízneš."
                        PUDAV()
                if "pojistka" in volba:
                    if "pojistka" in inventar:
                        t="Obyčejná pojistka."
                        PUDAV()
                if "polovina klíče" in volba:
                    if "polovina klíče 'OMEGA'(A)" in inventar or "polovina klíče 'OMEGA'(B)" in inventar:
                        t="Polovina klíče se znamením 'OMEGA'."
                        PUDAV()
                if "svítilna" in volba:
                    if "svítilna(bez baterií)" in inventar:
                        t="Vodotěsná svítilna. Bohužel v ní nejsou baterie."
                        PUDAV()
                    elif "svítilna" in inventar:
                        t="Funkční vodotěsná svítilna."
                        PUDAV()
                if "tágo" in volba:
                    if "tágo(zlomené)" in inventar:
                        t="Kulečníkové tágo. Bohužel je zlomené."
                        PUDAV()
                if "klíč(omega)" in volba:
                    if "klíč(OMEGA)" in inventar:
                        t="Klíč se znamením 'OMEGA'."
                        PUDAV()
                if "klíč(beta)" in volba:
                    if "klíč(BETA)" in inventar:
                        t="Klíč se znamením 'BETA'."
                        PUDAV()
                if "klíč(beran)" in volba:
                    if "klíč(beran)" in inventar:
                        t="Klíč se znamením berana."
                        PUDAV()
                if "lepidlo" in volba:
                    if "lepidlo" in inventar:
                        t="Silné modelářské lepidlo. Vhodné pro lepení dřeva, plastů i kovu."
                        PUDAV()
                if "baterie" in volba:
                    if "baterie" in inventar:
                        t="Sada tužkových baterií."
                        PUDAV()
                if "zapalovač" in volba:
                    if "zapalovač" in inventar:
                        t="Kvalitní benzínový zapalovač s vyrytým křížem."
                        PUDAV()
                if "ručička" in volba:
                    if "ručička" in inventar:
                        t="Ručička z hodin."
                        PUDAV()
                if "klíč(alfa)" in volba:
                    if "klíč(ALFA)" in inventar:
                        t="Klíč se znamením 'ALFA'."
                        PUDAV()
                if "hák" in volba:
                    if "hák(zlomený)" in inventar:
                        t="Zlomený hák na čištění okapů. V tomhle stavu s ním asi nikam nedosáhneš."
                        PUDAV()
                    elif "hák(prodloužený)" in inventar:
                        t="Hák na čištění okapů prodloužený zlomeným tágem."
                        PUDAV()
                if "zbraň" in volba:
                    if "zbraň" in inventar:
                        t="Nabitá pistole."
                        PUDAV()
                if "brousek" in volba:
                    if "brousek" in inventar:
                        t="Brousek. Vhodný pro ostření nožů."
                        PUDAV()
                if "papír" in volba:
                    if "papír(citronový)" in inventar:
                        t=("Prázdný papír vonící po citrónu.")
                        PUDAV()
                    if "papír(vzkaz)" in inventar:
                        t=("Na papíře je vzkaz hnědým písmem: '232.8°C'")
                        PUDAV()
                if "místnost" in volba: 
                    t=("Tahle půda už zažila lepší časy. V celé mísnosti je znatelný zápach alkoholu. Napravo od poklopu se nachází regál se všemi možnými typy alkoholu. Nalevo od poklopu se pak nachází masivní železná skříň a napravo od ní je nástěnka s jediným papírem.")
                    PUDAV()
                if "regál" in volba:
                    t=("Regál plný všemožných druhů alkoholu.")
                    PUDAV()
                if "skříň" in volba:
                    if skrin==0:
                        t=("Masivní železná skříň. Je zamčená číselným zámkem. Na zámku je vyrytá značka '°F'")
                        PUDAV()
                    else:
                        t=("Masivní železná skříň. Zdá se být orevřená.")
                        PUDAV()
                if "nástěnka" in volba:
                    if "papír" in inventar:
                        t=("Na nástěnce už nic není.")
                        PUDAV()
                    else:
                        t=("Na nástěnce je jeden papír. Zajimavé je že na papíře nic není, ale voní po citrónech.")
                        PUDAV()
            if "vezmi" in volba:
                if "papír" in volba or "lístek" in volba or "papírek" in volba:
                    if "papír" in inventar:
                        t=("Papír už máš v inventáři.")
                    else:
                        t=("Vzal sis k sobě papír.")
                        inventar.append("papír(citronový)")
                        PUDAV()
                if "alkohol" in volba:
                    if "alkohol" in inventar:
                        t=("Alkohol už u sebe máš.")
                        PUDAV()
                    else:
                        t=("Vzal sis k sobě láhev pálenky.")
                        inventar.append("alkohol")
                        PUDAV()
                else:
                    t=("Nevím jak to udělat")
                    PUDAV()
            if "použij" in volba:
                if "poklop" in volba or "dveře" in volba:
                    CHODBAT()
                if "izolepa" in volba and "tágo(zlomené)" in volba and "hák(zlomený)" in volba:
                    if "izolepa" in inventar and "tágo(zlomené)" in inventar and "hák(zlomený)" in inventar:
                        t=("Slepil jsi zbytky tága a háku a vyrobil tak prodloužený hák.")
                        inventar.remove("tágo(zlomené)")
                        inventar.remove("hák(zlomený)")
                        inventar.append("hák(prodloužený)")
                        PUDAV()
                    else:
                        t=("Nemáš všechny materiály.")
                        PUDAV()
                if "lepidlo" in volba and "polovina klíče gama(a)" in volba and "polovina klíče gama(b)" in volba:
                    if "lepidlo" in inventar and "polovina klíče GAMA(A)" in inventar and "polovina klíče GAMA(B)" in inventar:
                        t=("Slepil jsi dohromady klíč(GAMA)")
                        inventar.remove("polovina klíče GAMA(A)")
                        inventar.remove("polovina klíče GAMA(B)")
                        inventar.append("klíč(GAMA)")
                        PUDAV()
                    else:
                        t=("Něco ti chybí.")
                        PUDAV()
                if "svítilna" in volba and "baterie" in volba:
                    if "svítilna(bez baterií)" in inventar and "baterie" in inventar:
                        t=("Vložil jsi baterie do svítilny.")
                        inventar.remove("svítilna(bez baterií)")
                        inventar.remove("baterie")
                        inventar.append("svítilna")
                        PUDAV()
                    else:
                        t=("Tady něco schází.")
                        PUDAV()
                if "nůž(tupý)" in volba and "brousek" in volba:
                    if "nůž(tupý)" in inventar and "brousek" in inventar:
                        t=("Naostřil jsi nůž.")
                        inventar.remove("nůž(tupý)")
                        inventar.append("nůž(ostrý)")
                        PUDAV()
                    else:
                        t=("Něco potřebuješ")
                        PUDAV()
                if "skříň" in volba:
                    if skrin==0:
                        A=input("První číslo:")
                        B=input("Druhé číslo:")
                        C=input("Třetí číslo:")
                        if A=="4" and B=="5" and C=="1":
                            t=("Skříň se otevřela a v ní byl brousek, který sis vzal.")
                            inventar.append("brousek")
                            skrin=1
                            PUDAV()
                        else:
                            t=("Nic se nestalo...")
                            PUDAV()
                    else:
                        t=("Skříň je otevřená...")
                        PUDAV()
            else:
                t=("Tento příkaz neznám: ",volba)
                PUDAV()
###########################################################################################################################################################################################################
def vr(event=None):
    var.set(1)
    
main=Tk()

main.resizable(False, False)
main.configure(bg="gray")

var=IntVar()
rychlost=StringVar()
rychlost.set(2)

main.bind("<Return>", vr)

scroll=Scrollbar(main)
scroll.pack(side=RIGHT, fill=Y)

start=Button(main, text="START", command=SKLEP1T)
start.pack(padx=5, pady=5)

text=Text(main, width=100, height=50, wrap=WORD, yscrollcommand=scroll, bg="black", fg="yellow", relief="flat")
text.pack(padx=5, pady=5)

wolba=Entry(main, width=130, relief="flat")
wolba.pack(padx=5, pady=5)

submit=Button(main, text="OK", command=vr)
submit.pack(padx=5, pady=5)

main.mainloop()
