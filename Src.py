import winsound
import time
def ENDING_GOOD():
    print("PLACEHOLDER_GOOD_ENDING")
def ENDING_BAD():
    print("PLACEHOLDER_BAD_ENDING")
"""
#INVENTAR
if "prozkoumej" in volba:
    if "klíč(váhy)" in volba:
        if "klíč(váhy)" in inventar:
            print("Klíč se znamením vah.")
            BLANKV()
    if "nůž" in volba:
        if "nůž(tupý)" in inventar:
            print("Tupý kuchyňský nůž.")
            BLANKV()
        if "nůž(ostrý)" in inventar:
            print("Ostrý kuchyňský nůž. Vhodný pro řezání masa, ovoce i zeleniny")
            BLANKV()
    if "izolepa" in volba or "lepící páska" in volba:
        if "izolepa" in inventar:
            print("Stříbrná lepící páska, vhodná pro namáhané spoje.")
            BLANKV()
    if " " in volba:
        if "klíč(váhy)" in inventar:
            print("Klíč se znamením vah.")
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
        print(inventar)
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
    winsound.PlaySound("sound/basement.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
    print("Vítej do mojí hry! Pro provedení akce piš do příkazové řádky. Hra má tři hlavní akce: 'Prozkoumej' 'Vezmi' a 'Použij'. Svůj inventář si prohlédneš příkazem 'inventář'. Tyto akce kombinuj s předměty v herním světě nebo v inventáři. Objekty piš vždy v prvním pádě (hlavu=hlava atd.). Pojďme si to vyzkoušet v tomto úvodu.")
    print("Probouzíš se v chladné a vlhké místnosti. Vzadu na hlavě cítíš ostrou bolest. Tvé ruce jsou svázáné, ale naštěstí cítíš v kapse svůj věrný nůž.")
    print("Co uděláš?")
    global inventar
    global svazan
    global svetlo
    svetlo=0
    svazan=1
    inventar=[]
    SKLEP1V()
def SKLEP1V():
    global svazan
    global inventar
    global svetlo
    volba=input("Zadej příkaz:")
    volba=volba.lower()
    if volba=="inventář" or volba=="inventar":
        print(inventar)
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
            print("Obklopuje tě tma, skoro nic nevidíš. Naproti tobě proniká skulinkou pod něčím, co by mohly být dveře, trocha světla, která stačí na to aby sis všiml tlačítka na zdi.")
            SKLEP1V()
        if "kapsy" in volba or "kapsa" in volba:
            if "nůž" in inventar:
                print("Nic jiného už v kapsách nemáš.")
                SKLEP1V()
            else:
                print("V kapse jsi nahmatal malý kapesní nůž.")
                SKLEP1V()
        if "ruce" in volba:
            if svazan==1:
                print("Tvoje ruce jsou pevně svázané provazem.")
                SKLEP1V()
            else:
                print("Co jiného bys chtěl vidět? Jsou to tvoje ruce...")
                SKLEP1V()
        if "hlava" in volba:
            if svazan==1:
                print("Tvoje ruce jsou svázané a nejsi proto schopen ohmatat svoji hlavu.")
                SKLEP1V()
            else:
                print("Tvoje hlava je vzadu rozbitá. Krev ještě úplně nezaschla.")
                SKLEP1V()
        if "provaz" in volba or "provazy" in volba:
            if svazan==1:
                print("Provazy ti pevně drží ruce svázané.")
                SKLEP1V()
            else:
                print("Rozřezaný provaz leží na zemi. Je zničen tak že už nepůjde použít.")
                SKLEP1V()
        else:
            print("Asi ti nerozumím.")
            SKLEP1V()
    if "vezmi" in volba:
        if "nůž" in volba:
            if "nůž" in inventar:
                print("Nůž už máš v inventáři")
                SKLEP1V()
            else:
                print("Sebral jsi svůj nůž.")
                inventar.append("nůž")
                SKLEP1V()
        else:
            print("Nevím jak to udělat")
            SKLEP1V()
    if "použij" in volba:
        if "nůž" in volba:
            if svazan==1:
                if "provaz" in volba or "provazy" in volba:
                    winsound.PlaySound("sound/rope.wav", winsound.SND_ASYNC)
                    time.sleep(13)
                    print("Podařilo se ti provazy přeříznout. Nyní jsi volný.")
                    winsound.PlaySound("sound/basement.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
                    svazan=0
                    SKLEP1V()
                else:
                    print("To asi nepůjde")
                    SKLEP1V()
            else:
                if "provaz" in volba or "provazy" in volba:
                    print("Provazy už jsou přeřízlé")
                    SKLEP1V()
                else:
                    print("To asi nepůjde")
                    SKLEP1V()
        if "tlačítko" in volba:
            if svazan==1:
                print("Jsi svázaný, nedokážeš se k tlačítku dostat a stisknout ho.")
                SKLEP1V()
            else:
                winsound.PlaySound("sound/switch.wav", winsound.SND_ASYNC)
                time.sleep(1)
                SKLEP2T()
                svetlo=1
    if svetlo==1:
        return
    else:
        print("Tento příkaz neznám.")
        SKLEP1V()
#SC02 (SKLEP SVĚTLO)
def SKLEP2T():
    winsound.PlaySound("sound/basement.wav",winsound.SND_ASYNC | winsound.SND_LOOP)
    print("Místnost zalilo světlo. Kolem sebe vidíš něco co by mohl být sklep.")
    print("Co uděláš?")
    global stul
    global dvereopen
    stul=0
    dvereopen=0
    SKLEP2V()
def SKLEP2V():
    global inventar
    global stul
    global dvereopen
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
    if volba=="inventář" or volba=="inventar":
        print(inventar)
        SKLEP2V()
    if "prozkoumej" in volba:
        if "místnost" in volba:
            print("Kolem sebe vidíš malý sklep. V rohu místnosti leží něco co vypadá jako deka, po straně místnosti se pak nachází stůl na kterém něco leží.")
            SKLEP2V()
        if "stůl" in volba:
            print("Na stole se nachází kovová tyč, nějaké odpadky a prázdná láhev")
            stul=1
            SKLEP2V()
        if "deka" in volba:
            print("Stará špinavá a zapáchající deka. Něco by pod ní mohlo být.")
            SKLEP2V()
        if "tyč" in volba:
            if stul==1:
                print("Tyč na stole. Celkem dlouhá, celá ze železa.")
                SKLEP2V()
            else:
                print("Nevím co máš na mysli")
                SKLEP2V()
        if "láhev" in volba:
            if stul==1:
                print("Prázdná láhev. Nic v ní není.")
                SKLEP2V()
            else:
                print("Nevím co máš na mysli")
                SKLEP2V()
    if "vezmi" in volba:
        if "deka" in volba:
            print("To opravdu nechceš.")
            SKLEP2V()
        if "tyč" in volba:
            if "tyč" in inventar:
                print("Už máš tyč ve svém inventáři")
                SKLEP2V()
            else:
                if stul==1:
                    print("Vzal sis železnou tyč.")
                    inventar.append("tyč")
                    SKLEP2V()
                else:
                    print("Nevím o čem mluvíš")
                    SKLEP2V()
        if "láhev" in volba:
            print("Tu nebudeš asi potřebovat")
            SKLEP2V()
        if "odpadky" in volba:
            print("Fuj?")
            SKLEP2V()
    if "použij" in volba:
        if "deka" in volba:
            if "klíč" in inventar:
                print("Nic jiného už tam není")
                SKLEP2V()
            else:
                winsound.PlaySound("sound/blanket.wav",winsound.SND_ASYNC)
                time.sleep(1)
                winsound.PlaySound("sound/basement.wav",winsound.SND_ASYNC | winsound.SND_LOOP)
                print("Pod dekou byl klíč který sis vzal")
                inventar.append("klíč")
                SKLEP2V()
        if "nůž" in volba:
            print("To asi nepůjde")
            SKLEP2V()
        if "dveře" in volba:
            if dvereopen==1:
                print("Vycházíš z tmavého sklepení. Ve chvíli kdy vyjdeš schody ucítíš na svém zátylku ostrou bolest. Upadáš na zem a téměř okamžitě ztrácíš vědomí.")
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
                    print("Vypáčil jsi dveře")
                    dvereopen=1
                    inventar.remove("tyč")
                    SKLEP2V()
                else:
                    print("To nefunguje")
                    SKLEP2V()
            elif "klíč" in volba:
                if "klíč" in inventar:
                    print("Klíč se zlomil")
                    inventar.remove("klíč")
                    SKLEP2V()
                else:
                    print("To nejde")
            else:
                print("Dveře jsou zamčené")
                SKLEP2V()
    else:
        print("Tento příkaz neznám.")
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
    print("Propouzíš se na starém, zapáchajícím gauči. Vstáváš a zjišťuješ že se nacházíš v neznámé místnosti.")
    print("Co uděláš?")
    OPV()
def OPT2():
    print("Jsi v pokoji.")
    print("Co uděláš?")
    OPV()
def OPV():
    global inventar
    global pojistka
    global dvere_vahy_zamceno
    global zamek_alfa_zamcen
    global zamek_beta_zamcen
    global zamek_gama_zamcen
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
    if volba=="inventář" or volba=="inventar":
        print(inventar)
        OPV()
    if "prozkoumej" in volba:
        if "papír" in volba:
            if "papír(citronový)" in inventar:
                print("Prázdný papír vonící po citrónu.")
                OPV()
            if "papír(vzkaz)" in inventar:
                print("Na papíře je vzkaz hnědým písmem: '232.8°C'")
                OPV()
        if "místnost" in volba: 
            print("Nacházíš se v něčem co připomíná obývací pokoj. Naproti gauči se nachází velká televize. Za gaučem je potom schodiště vedoucí nahoru a pod schodištěm na stěně se nachází pojistková skříň. Naproti pojistkové skříni je polička s fotkami a vyhořelými svíčkami. Pokoj je spojený s chodbou, ve které jsou troje dveře. Jedny s nápisem 'Koupelna', druhé se znakem vah a hlavní dveře. Dále jde z pokoje průchod do kuchyně.")
            OPV()
        if "gauč" in volba:
            if "klíč(váhy)" in inventar:
                print("Je to starý zatuchlý gauč. Na gauči jsou zbytky krve, ale nejsi schopný poznat zda je tvoje.")
                OPV()
            else:
                print("Je to starý zatuchlý gauč. Na gauči jsou zbytky krve, ale nejsi schopný poznat zda je tvoje. Pod gaučem se něco nachází ale nejsi schopný na to dosáhnout.")
                OPV()
        if "skříň" in volba or "pojistky" in volba:
            if pojistka==0:
                print("Zdá se že je to stará pojistková skříň. Na místě s popiskem 'PATRO' chybí pojistka.")
                OPV()
            else:
                print("Jen stará pojistková skříň. Vše se zdá být v pořádku.")
                OPV()
        if "tv" in volba or "televize" in volba:
            print("Obyčejná televize. Zdá se být vypnutá.")
            OPV()
        if "schodiště" in volba or "schody" in volba:
            if pojistka==1:
                print("Schody vedoucí nahoru. Nahoře se svítí.")
                OPV()
            else:
                print("Schody vedoucí nahoru. Nahoře je tma.")
                OPV()
        if "dveře" in volba:
            if "hlavní" in volba:
                print("Hlavní dveře od domu vedoucí ven. Jsou zamčené třemi zámky.")
                if zamek_alfa_zamcen==1:
                    print("Zámek se znakem 'ALFA' je zamčený.")
                if zamek_beta_zamcen==1:
                    print("Zámek se znakem 'BETA' je zamčený.")
                if zamek_gama_zamcen==1:
                    print("Zámek se znakem 'GAMA' je zamčený.")
                elif zamek_alfa_zamcen==0 and zamek_beta_zamcen==0 and zamek_gama_zamcen==0:
                    print("Dveře jsou odemčené.")
                OPV()
            if "váhy" in volba:
                if dvere_vahy_zamceno==1:
                    print("Jsou to masivní dřevěné dveře. Na dveřích se nachází znak vah. Zdá se, že jsou zamčené.")
                    OPV()
                else:
                    print("Masivní dřevěné dveře se znamením vah. Jsou odemčené.")
                    OPV()
            if "koupelna" in volba:
                print("Jsou to dřevěné dveře, které kdysi dávno bývaly bílé. Ze spodní strany začaly před nějakou dobou plesnivět. Na dveřích je velkým písmem napsáno: 'KOUPELNA'.")
                OPV()
        if "police" in volba or "fotky" in volba:
            print("Improvizovaná dřevěná polička na které jsou fotky neznámých lidí. První je černobílá. Je na ní starší muž s knírem, který sedí v houpacím křesle. Pod fotkou je popis: 'Andrew Smith 1956-1983'. Druhá fotka zachycuje starší paní v šatech. Pod fotkou je popis: 'Amanda Smith 1957-1998'. Na třetí fotce je usmívající se mladá žena v rudých šatech. Pod její fotkou je popis: 'Maria Smith-Green 1979-2013'. Na poslední fotce je malé dítě v kolébce. Pod fotkou je popis: 'Thomas Green 2011-2013'")
            OPV()
        else:
            print("Nevím jak to udělat.")
            OPV()
    if "vezmi" in volba:
        print("Tak to asi nepůjde.")
        OPV()
    if "použij" in volba:
        if "izolepa" in volba and "tágo(zlomené)" in volba and "hák(zlomený)" in volba:
            if "izolepa" in inventar and "tágo(zlomené)" in inventar and "hák(zlomený)" in inventar:
                print("Slepil jsi zbytky tága a háku a vyrobil tak prodloužený hák.")
                inventar.remove("tágo(zlomené)")
                inventar.remove("hák(zlomený)")
                inventar.append("hák(prodloužený)")
                OPV()
            else:
                print("Nemáš všechny materiály.")
                OPV()
        if "lepidlo" in volba and "polovina klíče gama(a)" in volba and "polovina klíče gama(b)" in volba:
            if "lepidlo" in inventar and "polovina klíče GAMA(A)" in inventar and "polovina klíče GAMA(B)" in inventar:
                print("Slepil jsi dohromady klíč(GAMA)")
                inventar.remove("polovina klíče GAMA(A)")
                inventar.remove("polovina klíče GAMA(B)")
                inventar.append("klíč(GAMA)")
                OPV()
            else:
                print("Něco ti chybí.")
                OPV()
        if "svítilna" in volba and "baterie" in volba:
            if "svítilna(bez baterií)" in inventar and "baterie" in inventar:
                print("Vložil jsi baterie do svítilny.")
                inventar.remove("svítilna(bez baterií)")
                inventar.remove("baterie")
                inventar.append("svítilna")
                OPV()
            else:
                print("Tady něco schází.")
                OPV()
        if "nůž(tupý)" in volba and "brousek" in volba:
            if "nůž(tupý)" in inventar and "brousek" in inventar:
                print("Naostřil jsi nůž.")
                inventar.remove("nůž(tupý)")
                inventar.append("nůž(ostrý)")
                OPV()
            else:
                print("Něco potřebuješ")
                OPV()
        if "tv" in volba or "televize" in volba:
            print("Televize se zapla. V televizi jsou zprávy o nedávných vraždách. Pachatele se nepodařilo nikdy najít, ale všechny oběti měly do dlaní vyřezaný kříž. Po chvíli se rozhodneš televizi vypnout.")
            OPV()
        if "hák" in volba:
            if "hák(zlomený)" in inventar or "hák(prodloužený)" in inventar:
                if "gauč" in volba:
                    if "klíč(váhy)" in inventar:
                        print("Nic jiného už jsi nenašel")
                        OPV()
                    else:
                        print("Hákem sis přitáhl předmět pod gaučem. Ukázalo se že je to klíč se znakem vah. Klíč sis vzal.")
                        inventar.append("klíč(váhy)")
                        OPV()
                else:
                    print("Není možné.")
                    OPV()
            else:
                ("Nevím co se po mně chce.")
                OPV()
        if "klíč" in volba:
            if "váhy" in volba:
                if "dveře" and "váhy" in volba:
                    if dvere_vahy_zamceno==1:
                        if "klíč(váhy)" in inventar:
                            print("Odemkl sis dveře.")
                            dvere_vahy_zamceno=0
                            OPV()
                        else:
                            print("Nemáš klíč")
                            OPV()
                    else:
                        print("Dveře jsou už odemčené.")
                        OPV()
                else:
                    print("Tak to asi nezvládnu.")
                    OPV()
            if "alfa" in volba:
                if "dveře" and "hlavní" in volba:
                    if zamek_alfa_zamcen==1:
                        if "klíč(ALFA)" in inventar:
                            print("Odemkl jsi zámek 'ALFA'.")
                            zamek_alfa_zamcen=0
                            OPV()
                        else:
                            print("Nemáš klíč.")
                            OPV()
                    else:
                        print("Zámek už je odemčený.")
                        OPV()
                else:
                    print("Tohle není zrovna ideální.")
                    OPV()
            if "beta" in volba:
                if "dveře" and "hlavní" in volba:
                    if zamek_beta_zamcen==1:
                        if "klíč(BETA)" in inventar:
                            print("Odemkl jsi zámek 'BETA'.")
                            zamek_beta_zamcen=0
                            OPV()
                        else:
                            print("Nemáš klíč.")
                            OPV()
                    else:
                        print("Zámek už je odemčený.")
                        OPV()
                else:
                    print("Tohle není zrovna ideální.")
                    OPV()
            if "gama" in volba:
                if "dveře" and "hlavní" in volba:
                    if zamek_gama_zamcen==1:
                        if "klíč(GAMA)" in inventar:
                            print("Odemkl jsi zámek 'GAMA'.")
                            zamek_gama_zamcen=0
                            OPV()
                        else:
                            print("Nemáš klíč.")
                            OPV()
                    else:
                        print("Zámek už je odemčený.")
                        OPV()
                else:
                    print("Tohle není zrovna ideální.")
                    OPV()
        if "průchod" in volba or "kuchyně" in volba:
            KUCHYNET()
        if "skříň" in volba or "pojistky" in volba:
            if "pojistka" in volba:
                if "pojistka" in inventar:
                    print("Umístil jsi pojistku na její místo.")
                    inventar.remove("pojistka")
                    pojistka=1
                    OPV()
                else:
                    print("Nemáš žádnou pojistku.")
                    OPV()
            else:
                print("Takhle to nefunguje.")
                OPV()
        elif "dveře" in volba:
            if "hlavní" in volba:
                if zamek_alfa_zamcen==1 or zamek_beta_zamcen==1 or zamek_gama_zamcen==1:
                    print("Snažíš se dveře otevřít, ale je zamčeno.")
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
                    print("Lomcuješ dveřmi, ale je zamčeno.")
                    OPV()
                else:
                    HERNAT()
            else:
                print("To nějak nejde.")
                OPV()
        if "schody" in volba or "schodiště" in volba:
            if pojistka==1:
                CHODBAT()
            else:
                print("Nahoře je moc tma na to abys tam šel.")
                OPV()
        
        #Nutno dodělat předměty v inventáři
                        
    else:
        print("Tento příkaz neznám.")
        OPV()
#SC04 (Kuchyně)
def KUCHYNET():
    print("Tahle místnost je očividně kuchyně.")
    print("Co uděláš?")
    KUCHYNEV()
def KUCHYNEV():
    global inventar
    global trezor_zamcen
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
    if volba=="inventář" or volba=="inventar":
        print(inventar)
        KUCHYNEV()
    if "prozkoumej" in volba:
        if "papír" in volba:
            if "papír(citronový)" in inventar:
                print("Prázdný papír vonící po citrónu.")
                KUCHYNEV()
            if "papír(vzkaz)" in inventar:
                print("Na papíře je vzkaz hnědým písmem: '232.8°C'")
                KUCHYNEV()
        if "místnost" in volba or "kuchyně" in volba: 
            print("Uprostřed kuchyně se nachází velký jídelní stůl a podél jedné stěny se táhne kuchyňská linka na které leží tupý nůž. Tvoji pozornost ale upoutal trezor který leží na stole.")
            KUCHYNEV()
        if "nůž" in volba:
            if "nůž(tupý)" in inventar or "nůž(ostrý)" in inventar:
                print("Žádný jiný nůž už tu není.")
                KUCHYNEV()
            else:
                print("Starý kuchyňský nůž. Je úplně tupý.")
                KUCHYNEV()
        if "trezor" in volba:
            if trezor_zamcen==1:
                print("Zamčený trezor s číselným zámkem.")
                KUCHYNEV()
            else:
                print("Otevřený trezor. Nic v něm už není.")
                KUCHYNEV()
        if "stůl" in volba:
            print("Velký kuchyňský stůl z masivního dřeva. Kolem něj jsou rozestavěné židle a na něm leží masivní trezor.")
            KUCHYNEV()
        else:
            print("No tak to nezvládnu.")
            KUCHYNEV()
    if "vezmi" in volba:
        if "nůž" in volba:
            if "nůž(tupý)" in inventar or "nůž(ostrý)" in inventar:
                print("Žádný nůž tu nevidím.")
                KUCHYNEV()
            else:
                print("Vzal sis k sobě tupý nůž.")
                inventar.append("nůž(tupý)")
                KUCHYNEV()
        else:
            print("Nevím jak to udělat")
            KUCHYNEV()
    if "použij" in volba:
        if "izolepa" in volba and "tágo(zlomené)" in volba and "hák(zlomený)" in volba:
            if "izolepa" in inventar and "tágo(zlomené)" in inventar and "hák(zlomený)" in inventar:
                print("Slepil jsi zbytky tága a háku a vyrobil tak prodloužený hák.")
                inventar.remove("tágo(zlomené)")
                inventar.remove("hák(zlomený)")
                inventar.append("hák(prodloužený)")
                KUCHYNEV()
            else:
                print("Nemáš všechny materiály.")
                KUCHYNEV()
        if "lepidlo" in volba and "polovina klíče gama(a)" in volba and "polovina klíče gama(b)" in volba:
            if "lepidlo" in inventar and "polovina klíče GAMA(A)" in inventar and "polovina klíče GAMA(B)" in inventar:
                print("Slepil jsi dohromady klíč(GAMA)")
                inventar.remove("polovina klíče GAMA(A)")
                inventar.remove("polovina klíče GAMA(B)")
                inventar.append("klíč(GAMA)")
                KUCHYNEV()
            else:
                print("Něco ti chybí.")
                KUCHYNEV()
        if "svítilna" in volba and "baterie" in volba:
            if "svítilna(bez baterií)" in inventar and "baterie" in inventar:
                print("Vložil jsi baterie do svítilny.")
                inventar.remove("svítilna(bez baterií)")
                inventar.remove("baterie")
                inventar.append("svítilna")
                KUCHYNEV()
            else:
                print("Tady něco schází.")
                KUCHYNEV()
        if "nůž(tupý)" in volba and "brousek" in volba:
            if "nůž(tupý)" in inventar and "brousek" in inventar:
                print("Naostřil jsi nůž.")
                inventar.remove("nůž(tupý)")
                inventar.append("nůž(ostrý)")
                KUCHYNEV()
            else:
                print("Něco potřebuješ")
                KUCHYNEV()
        if "průchod" in volba or "pokoj" in volba:
            OPT2()
        if "trezor" in volba:
            if trezor_zamcen==1:
                C1=int(input("První číslo:"))
                C2=int(input("Druhé číslo:"))
                C3=int(input("Třetí číslo:"))
                C4=int(input("Čtvrté číslo:"))
                if C1==6 and C2==8 and C3==3 and C4==1:
                    trezor_zamcen=0
                    print("Trezor se otevřel. Uvnitř byla... Izolepa? Vzal sis ji k sobě.")
                    inventar.append("izolepa")
                    KUCHYNEV()
                else:
                    print("Nic se nestalo.")
                    KUCHYNEV()
            else:
                print("V trezori už nic není.")
                KUCHYNEV()
    #Chybí dodělat věci v inventáři
    else:
        print("Tento příkaz neznám.")
        KUCHYNEV()
#SC05 (Koupelna)
def KOUPELNAT():
    print("Vcházíš do něčeho, co by se dalo nazvat koupelnou.")
    print("Co uděláš?")
    KOUPELNAV()
def KOUPELNAV():
    global inventar
    global vana_naplnena
    global susicka
    global wc
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
    if volba=="inventář" or volba=="inventar":
        print(inventar)
        KOUPELNAV()
    if "prozkoumej" in volba:
        if "papír" in volba:
            if "papír(citronový)" in inventar:
                print("Prázdný papír vonící po citrónu.")
                KOUPELNAV()
            if "papír(vzkaz)" in inventar:
                print("Na papíře je vzkaz hnědým písmem: '232.8°C'")
                KOUPELNAV()
        if "místnost" in volba or "koupelna" in volba: 
            print("Je to tmavá místnost. Všechna okna jsou zakrytá a vzduch je tu jako v prádelně. Hned za dveřmi v rohu se nachází stará pračka a sušička. Na sušičce svítí červená kontrolka. Za nimi se nachází rozbité umyvadlo. Naproti od tebe je vana a záchodová mísa do kterých od dveří nevidíš.")
            KOUPELNAV()
        if "pračka" in volba:
            print("Stará pračka. Zespodu výrazně rezavá. Skrz okénko vepředu vidíš, že v ní nic není.")
            KOUPELNAV()
        if "sušička" in volba:
            if susicka==1:
                print("Stará, sotva funkční sušička. Na panelu svítí červená kontrolka.")
                KOUPELNAV()
            else:
                print("Tahle sušička už nikdy sušit nebude...")
                KOUPELNAV()
        if "umyvadlo" in volba:
            print("Rozbité umyvadlo, které rozhodně zažilo lepší časy. Ze zdi nad ním trčí olověná trubka, ze které pokapává rezavá voda.")
            KOUPELNAV()
        if "wc" in volba or "záchod" in volba or "toaleta" in volba:
            if wc==1:
                print("Špinavá toaletní mísa plná nechutné vody. Při bližším prozkoumání máš pocit že v té vodě něco vidíš.")
                KOUPELNAV()
            else:
                print("Špinavá toaletní mísa. Odmítáš se na ni dívat déle než nezbytně musíš.")
                KOUPELNAV()
        if "vana" in volba:
            if vana_naplnena==1:
                print("Špinavá vana plná špinavé vody. Prostě fuj.")
                KOUPELNAV()
            else:
                print("Prázdná vana. Pořád není nejčistší.")
                KOUPELNAV()
        if "dveře" in volba:
            print("Dveře vedoucí zpět na chodbu.")
            KOUPELNAV()
    
        else:
            print("Nevím jak to udělat")
            KOUPELNAV()
    if "použij" in volba:
        if "izolepa" in volba and "tágo(zlomené)" in volba and "hák(zlomený)" in volba:
            if "izolepa" in inventar and "tágo(zlomené)" in inventar and "hák(zlomený)" in inventar:
                print("Slepil jsi zbytky tága a háku a vyrobil tak prodloužený hák.")
                inventar.remove("tágo(zlomené)")
                inventar.remove("hák(zlomený)")
                inventar.append("hák(prodloužený)")
                KOUPELNAV()
            else:
                print("Nemáš všechny materiály.")
                KOUPELNAV()
        if "lepidlo" in volba and "polovina klíče gama(a)" in volba and "polovina klíče gama(b)" in volba:
            if "lepidlo" in inventar and "polovina klíče GAMA(A)" in inventar and "polovina klíče GAMA(B)" in inventar:
                print("Slepil jsi dohromady klíč(GAMA)")
                inventar.remove("polovina klíče GAMA(A)")
                inventar.remove("polovina klíče GAMA(B)")
                inventar.append("klíč(GAMA)")
                KOUPELNAV()
            else:
                print("Něco ti chybí.")
                KOUPELNAV()
        if "svítilna" in volba and "baterie" in volba:
            if "svítilna(bez baterií)" in inventar and "baterie" in inventar:
                print("Vložil jsi baterie do svítilny.")
                inventar.remove("svítilna(bez baterií)")
                inventar.remove("baterie")
                inventar.append("svítilna")
                KOUPELNAV()
            else:
                print("Tady něco schází.")
                KOUPELNAV()
        if "nůž(tupý)" in volba and "brousek" in volba:
            if "nůž(tupý)" in inventar and "brousek" in inventar:
                print("Naostřil jsi nůž.")
                inventar.remove("nůž(tupý)")
                inventar.append("nůž(ostrý)")
                KOUPELNAV()
            else:
                print("Něco potřebuješ")
                KOUPELNAV()
        if "dveře" in volba:
            OPT2()
        if "sušička" in volba:
            if susicka==1:
                print("Stisknul jsi tlačítko u červené kontrolky. Sušička se rozběhla a téměř okamžitě na to se z ní začal ozývat neuvěřitelný hluk. Poté co se zastavila (pravděpodobně nadobro) ses rozhodl ji otevřít. Uvnitř byla pojistka, kterou sis vzal.")
                inventar.append("pojistka")
                susicka=0
                KOUPELNAV()
            else:
                print("Stisknul jsi tlačítko. Sušička nic neudělala.")
                KOUPELNAV()
        if "wc" in volba or "toaleta" in volba or "záchod" in volba:
            if wc==1:
                print("Zadržuješ dech, zatínáš zuby a noříš svoji ruku do odporné záchodové vody. Po chvílí pátrání nahmatáš nějaký objekt. Po vytažení se ukázalo že je to klíč. Nebo teda aspoň jeho polovina. Rozhodl ses si ji vzít.")
                inventar.append("polovina klíče GAMA(A)")
                wc=0
                KOUPELNAV()
            else:
                print("Tam už rozhodně ruku znovu nestrčíš.")
                KOUPELNAV()
        if "vana" in volba:
            if vana_naplnena==1:
                print("Vytáhl jsi špunt u vany a po nějaké chvíli se všechna voda z vany vypustila. Na dně vany ležela malá vodotěsná svítilna. Po jejím vyzkoušení zjišťuješ, že v ní nejsou baterie, ale stejně si ji raději vezmeš.")
                inventar.append("svítilna(bez baterií)")
                vana_naplnena=0
                KOUPELNAV()
            else:
                print("Už tu není co dělat.")
                KOUPELNAV()
        else:
            print("To si nezvládnu.")
    else:
        print("Tento příkaz neznám.")
        KOUPELNAV()
#SC06 (Herna)
def HERNAT():
    print("Tato místnost se zdá byt herna.")
    print("Co uděláš?")
    HERNAV()
def HERNAV():
    global inventar
    global krb_plamen
    global telo_rozrezane
    global krb_alkohol
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
    if volba=="inventář" or volba=="inventar":
        print(inventar)
        HERNAV()
    if "prozkoumej" in volba:
        if "papír" in volba:
            if "papír(citronový)" in inventar:
                print("Prázdný papír vonící po citrónu.")
                HERNAV()
            if "papír(vzkaz)" in inventar:
                print("Na papíře je vzkaz hnědým písmem: '232.8°C'")
                HERNAV()
        if "místnost" in volba: 
            print("Uprostřed místnosti se nachází masivní kulečníkový stůl, který už rozhodně zažil lepší časy. U vzdálenější stěny stojí překvapivě zachovalý krb. Hned za dveřmi u stěny je stojan na tága a za kulečníkem na zemi leží nějaký tmavý objekt, který nejsi schopný zcela rozeznat.")
            HERNAV()
        if "objekt" in volba:
            print("Přiblížíš se k tmavému objektu a k tvému zděšení zjišťuješ že se jedná o lidské tělo.")
            HERNAV()
        if "tělo" in volba:
            if telo_rozrezane==1:
                print("Rozřezané tělo toho chudáka. Z toho co kdysi bývalo břicho teď vyhřezávají vnitřnosti a celou místnost plní nesnesitelný zápach.")
                HERNAV()
            else:
                print("Proti veškerému svému odporu se přiblížíš k tělu abys ho prozkoumal. Jedná se o muže středního věku. Příčina smrti se zdá být předávkování, aspoň tak usuzuješ podle prázdných krabiček od léků poházených kolem. Na obou rukách má vypálené kříže. Po bližším ohledání zjišťuješ, že na břiše má nakreslený znak 'BETA'.")
                HERNAV()
        if "kulečník" in volba or "stůl" in volba:
            if "polovina klíče GAMA(B)" in inventar or "klíč(GAMA)" in inventar:
                print("Masivní kulečníkový stůl. Pravděpodobně z počátku minulého století.")
                HERNAV()
            else:
                print("Masivní kulečníkový stůl. Pravděpodobně z počátku minulého století. V jedné z děr se něco nachází.")
                HERNAV()
        if "díra" in volba:
            print("V díře je něco co vypadá jako klíč, ale rukou se ti nedaří ho vytáhnout.")
            HERNAV()
        if "krb" in volba:
            if krb_plamen==1:
                print("Starý krb, ve kterém hoří mohutný plamen.")
                HERNAV()
            else:
                print("Starý krb, ve kterém se pravděpodobně často topilo. Je v něm připraveno dřevo na podpal.")
                HERNAV()
        if "stojan" in volba:
            if "tágo(zlomené)" in inventar or "hák(prodloužený)" in inventar:
                print("Stojan na tága.")
                HERNAV()
            else:
                print("Stojan na tága, ve kterém stojí jen jedno opuštěné zlomené tágo.")
                HERNAV()
    if "vezmi" in volba:
        if "tágo" in volba:
            if "tágo(zlomené)" in inventar or "hák(prodloužený)" in inventar:
                print("Nic už tu není.")
                HERNAV()
            else:
                print("Sebral jsi zlomené tágo.")
                inventar.append("tágo(zlomené)")
                HERNAV()
        else:
            print("Nevím jak to udělat.")
            HERNAV()
    if "použij" in volba:
        if "izolepa" in volba and "tágo(zlomené)" in volba and "hák(zlomený)" in volba:
            if "izolepa" in inventar and "tágo(zlomené)" in inventar and "hák(zlomený)" in inventar:
                print("Slepil jsi zbytky tága a háku a vyrobil tak prodloužený hák.")
                inventar.remove("tágo(zlomené)")
                inventar.remove("hák(zlomený)")
                inventar.append("hák(prodloužený)")
                HERNAV()
            else:
                print("Nemáš všechny materiály.")
                HERNAV()
        if "lepidlo" in volba and "polovina klíče gama(a)" in volba and "polovina klíče gama(b)" in volba:
            if "lepidlo" in inventar and "polovina klíče GAMA(A)" in inventar and "polovina klíče GAMA(B)" in inventar:
                print("Slepil jsi dohromady klíč(GAMA)")
                inventar.remove("polovina klíče GAMA(A)")
                inventar.remove("polovina klíče GAMA(B)")
                inventar.append("klíč(GAMA)")
                HERNAV()
            else:
                print("Něco ti chybí.")
                HERNAV()
        if "svítilna" in volba and "baterie" in volba:
            if "svítilna(bez baterií)" in inventar and "baterie" in inventar:
                print("Vložil jsi baterie do svítilny.")
                inventar.remove("svítilna(bez baterií)")
                inventar.remove("baterie")
                inventar.append("svítilna")
                HERNAV()
            else:
                print("Tady něco schází.")
                HERNAV()
        if "nůž(tupý)" in volba and "brousek" in volba:
            if "nůž(tupý)" in inventar and "brousek" in inventar:
                print("Naostřil jsi nůž.")
                inventar.remove("nůž(tupý)")
                inventar.append("nůž(ostrý)")
                HERNAV()
            else:
                print("Něco potřebuješ")
                HERNAV()
        if "dveře" in volba:
            OPT2()
        if "krb" in volba:
            if krb_plamen==1:
                if "papír" in volba:
                    if "papír(citronový)" in inventar:
                        print("Díky žáru plamene se na papíře objevil text.")
                        inventar.remove("papír(citronový)")
                        inventar.append("papír(vzkaz)")
                        HERNAV()
                    elif "papír(vzkaz)" in volba:
                        print("Nevím proč, ale rozhodl ses papír spálit.")
                        inventar.remove("papír(vzkaz)")
                        HERNAV()
                    else:
                        print("Žádný jiný papír už nemáš.")
                        HERNAV()
                else:
                    print("To nepůjde.")
                    HERNAV()
            else:
                if "alkohol" in volba:
                    if "alkohol" in inventar:
                        print("Nalil jsi na dřevo alkohol.")
                        krb_alkohol=1
                        inventar.remove("alkohol")
                        HERNAV()
                    else:
                        print("Nemáš žádný alkohol.")
                        HERNAV()
                if "zapalovač" in volba:
                    if "zapalovač" in inventar:
                        if krb_alkohol==1:
                            print("Zapálil jsi dřevo nasáklé alkoholem, které okamžitě vzplanulo.")
                            krb_plamen=1
                            HERNAV()
                        else:
                            print("Snažíš se dřevo v krbu zapálit, ale nedaří se ti to.")
                            HERNAV()
                    else:
                        print("Nemáš zapalovač.")
                        HERNAV()
        if "kulečník" in volba or "stůl" in volba or "díra" in volba:
            if "hák" in volba:
                if "hák(zlomený)" in inventar or "hák(prodloužený)"  in inventar:
                    if "klíč(GAMA)" in inventar or "polovina klíče GAMA(B)" in inventar:
                        print("Nic už tam není.")
                        HERNAV()
                    else:
                        print("Vytáhl jsi z díry polovinu klíče.")
                        inventar.append("polovina klíče GAMA(B)")
                        HERNAV()
                else:
                    print("Nemáš žádný hák.")
                    HERNAV()
            else:
                print("To není možné.")
                HERNAV()
        if "tělo" in volba:
            if "nůž" in volba:
                if "nůž(ostrý)" in inventar:
                    if telo_rozrezane==0:
                        print("S neuvěřitelným odporem vytahujeě svůj nůž a pomalu řežeě břicho mrtvého. Při prvním kontaktu nože se vyvalilo obrovské množství krve ale ty dále pokračuješ. Když se dostaneš k žaludku nacházíš klíč, který sis vzal.")
                        inventar.append("klíč(BETA)")
                        telo_rozrezane=1
                        HERNAV()
                    else:
                        print("Už nemáš žádný důvod.")
                        HERNAV()
                else:
                    print("Nemáš ostrý nůž.")
                    HERNAV()
            else:
                print("To nezvládnu.")
                HERNAV()
        #Inventář dodělat
    else:
        print("Tento příkaz neznám.")
        HERNAV()
#SC07 (Chodba)
def CHODBAT():
    print("Jsi na chodbě v druhém patře.")
    print("Co uděláš?")
    CHODBAV()
def CHODBAV():
    global inventar
    global kukacky
    global dvere_beran_zamceno
    global poklop
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
    if volba=="inventář" or volba=="inventar":
        print(inventar)
        CHODBAV()
    if "prozkoumej" in volba:
        if "papír" in volba:
            if "papír(citronový)" in inventar:
                print("Prázdný papír vonící po citrónu.")
                CHODBAV()
            if "papír(vzkaz)" in inventar:
                print("Na papíře je vzkaz hnědým písmem: '232.8°C'")
                CHODBAV()
        if "místnost" in volba: 
            print("Nacházíš se v podlouhlé chodbě. Na stěně naproti schodišti visí staré kukačky. Nalevo od nich jsou dveře vedoucí na balkón a okno proražené větví. Napravo jsou dvoje dveře. Jedny na sobě mají znak berana, ty druhé vedou do ložnice. Na stropě mezi těmito dveřmi je poklop s otvorem na otevření.")
            CHODBAV()
        if "kukačky" in volba:
            if kukacky==1:
                print("Staré kukačky. Nic zvláštního.")
                CHODBAV()
            else:
                print("Staré kukačky. Chybí jim minutová ručička.")
                CHODBAV()
        if "okno" in volba:
            print("Okno je proražené větví stromu. Zdá se, že by se po této větvi dalo přelézt na balkón")
            CHODBAV()
    if "použij" in volba:
        if "izolepa" in volba and "tágo(zlomené)" in volba and "hák(zlomený)" in volba:
            if "izolepa" in inventar and "tágo(zlomené)" in inventar and "hák(zlomený)" in inventar:
                print("Slepil jsi zbytky tága a háku a vyrobil tak prodloužený hák.")
                inventar.remove("tágo(zlomené)")
                inventar.remove("hák(zlomený)")
                inventar.append("hák(prodloužený)")
                CHODBAV()
            else:
                print("Nemáš všechny materiály.")
                CHODBAV()
        if "lepidlo" in volba and "polovina klíče gama(a)" in volba and "polovina klíče gama(b)" in volba:
            if "lepidlo" in inventar and "polovina klíče GAMA(A)" in inventar and "polovina klíče GAMA(B)" in inventar:
                print("Slepil jsi dohromady klíč(GAMA)")
                inventar.remove("polovina klíče GAMA(A)")
                inventar.remove("polovina klíče GAMA(B)")
                inventar.append("klíč(GAMA)")
                CHODBAV()
            else:
                print("Něco ti chybí.")
                CHODBAV()
        if "svítilna" in volba and "baterie" in volba:
            if "svítilna(bez baterií)" in inventar and "baterie" in inventar:
                print("Vložil jsi baterie do svítilny.")
                inventar.remove("svítilna(bez baterií)")
                inventar.remove("baterie")
                inventar.append("svítilna")
                CHODBAV()
            else:
                print("Tady něco schází.")
                CHODBAV()
        if "nůž(tupý)" in volba and "brousek" in volba:
            if "nůž(tupý)" in inventar and "brousek" in inventar:
                print("Naostřil jsi nůž.")
                inventar.remove("nůž(tupý)")
                inventar.append("nůž(ostrý)")
                CHODBAV()
            else:
                print("Něco potřebuješ")
                CHODBAV()
        if "dveře" in volba:
            if "ložnice" in volba:
                LOZNICET()
            if "balkon" in volba:
                print("Dveře jsou zablokované spadlou větví.")
                CHODBAV()
            if "beran" in volba or "knihovna" in volba:
                if dvere_beran_zamceno==1:
                    if "klíč(beran)" in volba:
                        if "klíč(beran)" in inventar:
                            print("Odemkl jsi dveře se znamením berana.")
                            dvere_beran_zamceno=0
                            CHODBAV()
                        else:
                            print("Nemáš patřičný klíč.")
                            CHODBAV()
                    else:
                        print("Dveře jsou zamčené.")
                        CHODBAV()
                else:
                    KNIHOVNAT()
        if "okno" in volba:
            print("Přelezl jsi po větvi stromu na balkón.")
            BALKONT()
        if "schody" in volba:
            OPT2()
        if "poklop" in volba:
            if poklop==0:
                if "hák" in volba:
                    if "hák(prodloužený)" in inventar:
                        print("Odklopil jsi poklop a dolů se spustily schody na půdu.")
                        poklop=1
                        CHODBAV()
                    else:
                        print("Nemáš dostatečně dlouhý nástroj.")
                        CHODBAV()
                else:
                    print("Poklop je zavřený.")
                    CHODBAV()
            else:
                PUDAT()
        if "kukačky" in volba:
            if "ručička" in volba:
                if "ručička" in inventar:
                    print("Zasadil jsi ručičku do hodin a nastavil 12 hodin. Místo kukačky na rameni vyjel klíč se znamením berana, který sis k sobě vzal.")
                    inventar.append("klíč(beran)")
                    inventar.remove("ručička")
                    kukacky=1
                    CHODBAV()
                else:
                    print("Nemáš žádnou ručičku.")
                    CHODBAV()
            else:
                print("To nepůjde.")
                CHODBAV()
    else:
        print("Tento příkaz neznám.")
        CHODBAV()
#SC08 (Ložnice)
def LOZNICET():
    print("Jsi v ložnici.")
    print("Co uděláš?")
    LOZNICEV()
def LOZNICEV():
    global inventar
    global kukacky
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
    if volba=="inventář" or volba=="inventar":
        print(inventar)
        LOZNICEV()
    if "prozkoumej" in volba:
        if "papír" in volba:
            if "papír(citronový)" in inventar:
                print("Prázdný papír vonící po citrónu.")
                LOZNICEV()
            if "papír(vzkaz)" in inventar:
                print("Na papíře je vzkaz hnědým písmem: '232.8°C'")
                LOZNICEV()
        if "místnost" in volba: 
            print("Celkem velká ložnice. Nalevo od vchodu je vitrína s modely letadel a šuplíky pod nimi. Naproti tobě pak leží rozbité hodiny. Napravo od vchodu je postel a noční stolek.")
            LOZNICEV()
        if "stolek" in volba:
            if "zapalovač" in inventar:
                print("Na stolku už nic není.")
                LOZNICEV()
            else:
                print("Na stolku leží zapalovač a cigarety. Majitel domu je pravděpodobně těžký kuřák.")
                LOZNICEV()
        if "zapalovač" in volba:
            print("Benzínový zapalovač. Je na něm vyrytý kříž.")
            LOZNICEV()
        if "postel" in volba:
            print("Velká postel pro dva lidi. Jen jedna polovina se zdá být používána.")
            LOZNICEV()
        if "vitrína" in volba:
            print("Velká skleněná vitrína. V poličkách jsou různé modely letadel. Pod nimi se nachází několik šuplíků.")
            LOZNICEV()
        if "šuplíky" in volba or "šuplík" in volba:
            if "lepidlo" in inventar:
                print("V šuplících už nic není.")
                LOZNICEV()
            else:
                print("V jednom z šuplíků jsi našel modelářské lepidlo a sadu baterií.")
                inventar.append("lepidlo")
                inventar.append("baterie")
                LOZNICEV()
        if "hodiny" in volba:
            if "ručička" in inventar:
                print("Rozbité hodiny. Nic zajimavého.")
                LOZNICEV()
            else:
                print("Rozbité hodiny. Kousek od nich leží vypadlá ručička.")
                LOZNICEV()
    if "vezmi" in volba:
        if "zapalovač" in volba:
            if "zapalovač" in inventar:
                print("Zapalovač už máš v inventáři.")
                LOZNICEV()
            else:
                print("Vzal sis k sobě zapalovač.")
                inventar.append("zapalovač")
                LOZNICEV()
        if "ručička" in volba:
            if "ručička" in inventar or kukacky==1:
                print("Žádná další ručička už tu není.")
                LOZNICEV()
            else:
                print("Vzal sis k sobě ručičku od hodin.")
                inventar.append("ručička")
                LOZNICEV()
        else:
            print("Nevím jak to udělat")
            LOZNICEV()
    if "použij" in volba:
        if "izolepa" in volba and "tágo(zlomené)" in volba and "hák(zlomený)" in volba:
            if "izolepa" in inventar and "tágo(zlomené)" in inventar and "hák(zlomený)" in inventar:
                print("Slepil jsi zbytky tága a háku a vyrobil tak prodloužený hák.")
                inventar.remove("tágo(zlomené)")
                inventar.remove("hák(zlomený)")
                inventar.append("hák(prodloužený)")
                LOZNICEV()
            else:
                print("Nemáš všechny materiály.")
                LOZNICEV()
        if "lepidlo" in volba and "polovina klíče gama(a)" in volba and "polovina klíče gama(b)" in volba:
            if "lepidlo" in inventar and "polovina klíče GAMA(A)" in inventar and "polovina klíče GAMA(B)" in inventar:
                print("Slepil jsi dohromady klíč(GAMA)")
                inventar.remove("polovina klíče GAMA(A)")
                inventar.remove("polovina klíče GAMA(B)")
                inventar.append("klíč(GAMA)")
                LOZNICEV()
            else:
                print("Něco ti chybí.")
                LOZNICEV()
        if "svítilna" in volba and "baterie" in volba:
            if "svítilna(bez baterií)" in inventar and "baterie" in inventar:
                print("Vložil jsi baterie do svítilny.")
                inventar.remove("svítilna(bez baterií)")
                inventar.remove("baterie")
                inventar.append("svítilna")
                LOZNICEV()
            else:
                print("Tady něco schází.")
                LOZNICEV()
        if "nůž(tupý)" in volba and "brousek" in volba:
            if "nůž(tupý)" in inventar and "brousek" in inventar:
                print("Naostřil jsi nůž.")
                inventar.remove("nůž(tupý)")
                inventar.append("nůž(ostrý)")
                LOZNICEV()
            else:
                print("Něco potřebuješ")
                LOZNICEV()
        if "dveře" in volba:
            CHODBAT()
    else:
        print("Tento příkaz neznám.")
        LOZNICEV()
#SC09 (Knihovna)
def KNIHOVNAT():
    print("Nacháziš se v místnosti, která slouží jako knihovna.")
    print("Co uděláš?")
    KNIHOVNAV()
def KNIHOVNAV():
    global inventar
    global PC
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
    if volba=="inventář" or volba=="inventar":
        print(inventar)
        KNIHOVNAV()
    if "prozkoumej" in volba:
        if "papír" in volba:
            if "papír(citronový)" in inventar:
                print("Prázdný papír vonící po citrónu.")
                KNIHOVNAV()
            if "papír(vzkaz)" in inventar:
                print("Na papíře je vzkaz hnědým písmem: '232.8°C'")
                KNIHOVNAV()
        if "místnost" in volba: 
            print("Pravděpodobně často používaná knihovna/pracovna. Naproti dveří je stůl s počítačem obklopený knihovnami po obou stranách.")
            KNIHOVNAV()
        if "knihovna" in volba:
            print("Knihovna plná knih od všech možných autorů ze všech možných období. Možná by se tu dalo najít něco zajimavého.")
            KNIHOVNAV()
        if "stůl" in volba:
            print("Starý dřevěný stůl na kterém je zapnutý počítač a podivný vzkaz.")
            KNIHOVNAV()
        if "počítač" in volba or "pc" in volba:
            if PC==0:
                print("Zapnutý počítač. Na obrazovce je kolonka pro heslo a pod ní text: 'W. Shakespeare 1603'")
                KNIHOVNAV()
            else:
                print("Na obrazovce je fotka trezoru s popiskem: R. 'Smithova *++*'.")
                KNIHOVNAV()
        if "vzkaz" in volba or "lístek" in volba:
            print("Na lístku je napsáno : 'Dobrotivý bůh se neohlíží na naše omyly, jestliže způsobují věci, které sami nemůžeme poznat.' a obrázek znaku 'alfa'")
            KNIHOVNAV()          
    if "použij" in volba:
        if "izolepa" in volba and "tágo(zlomené)" in volba and "hák(zlomený)" in volba:
            if "izolepa" in inventar and "tágo(zlomené)" in inventar and "hák(zlomený)" in inventar:
                print("Slepil jsi zbytky tága a háku a vyrobil tak prodloužený hák.")
                inventar.remove("tágo(zlomené)")
                inventar.remove("hák(zlomený)")
                inventar.append("hák(prodloužený)")
                KNIHOVNAV()
            else:
                print("Nemáš všechny materiály.")
                KNIHOVNAV()
        if "lepidlo" in volba and "polovina klíče gama(a)" in volba and "polovina klíče gama(b)" in volba:
            if "lepidlo" in inventar and "polovina klíče GAMA(A)" in inventar and "polovina klíče GAMA(B)" in inventar:
                print("Slepil jsi dohromady klíč(GAMA)")
                inventar.remove("polovina klíče GAMA(A)")
                inventar.remove("polovina klíče GAMA(B)")
                inventar.append("klíč(GAMA)")
                KNIHOVNAV()
            else:
                print("Něco ti chybí.")
                KNIHOVNAV()
        if "svítilna" in volba and "baterie" in volba:
            if "svítilna(bez baterií)" in inventar and "baterie" in inventar:
                print("Vložil jsi baterie do svítilny.")
                inventar.remove("svítilna(bez baterií)")
                inventar.remove("baterie")
                inventar.append("svítilna")
                KNIHOVNAV()
            else:
                print("Tady něco schází.")
                KNIHOVNAV()
        if "nůž(tupý)" in volba and "brousek" in volba:
            if "nůž(tupý)" in inventar and "brousek" in inventar:
                print("Naostřil jsi nůž.")
                inventar.remove("nůž(tupý)")
                inventar.append("nůž(ostrý)")
                KNIHOVNAV()
            else:
                print("Něco potřebuješ")
                KNIHOVNAV()
        if "dveře" in volba:
            CHODBAT()
        if "pc" in volba or "počítač" in volba:
            if PC==0:
                passw=input("Zadejte heslo:")
                if passw=="Hamlet":
                    print("Počítač se odemkl.")
                    PC=1
                    KNIHOVNAV()
                else:
                    print("Špatné heslo")
                    KNIHOVNAV()
            else:
                print("Na tomto počítači už není nic jiného.")
                KNIHOVNAV()
        if "knihovna" in volba:
            kniha=input("Jakou knihu hledáš? (Pro konec nech řádku prázdnou):")
            if kniha=="Dekameron":
                if "klíč(alfa)" in inventar:
                    print("Ačkoliv se jedná o opravdu mistrovské dílo, nic víc už v něm není.")
                    KNIHOVNAV()
                else:
                    print("Otevřel jsi toto mistrovské dílo a vypadl z něj klíč se znakem 'alfa'. Rozhodl ses si tento klíč vzít.")
                    inventar.append("klíč(ALFA)")
                    KNIHOVNAV()
            if kniha=="":
                KNIHOVNAV()
            if kniha=="Canterburské Povídky" or kniha=="canterburské povídky" or kniha=="Canterburské povídky":
                print("Očividně jen levná kopie Dekameronu.")
                KNIHOVNAV()
            else:
                print("Na této knize není nic zajimavého.")
                KNIHOVNAV()
    else:
        print("Tento příkaz neznám.")
        KNIHOVNAV()
#SC10 (Balkón)
def BALKONT():
    print("Jsi na balkóně.")
    print("Co uděláš?")
    BALKONV()
def BALKONV():
    global inventar
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
    if volba=="inventář" or volba=="inventar":
        print(inventar)
        BALKONV()
    if "prozkoumej" in volba:
        if "papír" in volba:
            if "papír(citronový)" in inventar:
                print("Prázdný papír vonící po citrónu.")
                BALKONV()
            if "papír(vzkaz)" in inventar:
                print("Na papíře je vzkaz hnědým písmem: '232.8°C'")
                BALKONV()
        if "místnost" in volba or "balkón" in volba or "balkon" in volba:
            if "hák(zlomený)" in inventar or "hák(prodloužený)" in inventar:
                print("Nacházíš se na balkóně. Je tu sice hezký výhled, ale jinak tu skoro nic není. Ze starého okapu teče voda, možná je ucpaný. Dveře blokuje větev po které ses sem dostal.")
                BALKONV()
            else:
                print("Nacházíš se na balkóně. Je tu sice hezký výhled, ale jinak tu skoro nic není. Ze starého okapu teče voda, možná je ucpaný. V rohu je opřený zlomený hák na čištění okapů. Dveře blokuje větev po které ses sem dostal.")
                BALKONV()
        if "hák" in volba:
            if "hák(zlomený)" in inventar:
                print("Zlomený hák na čištění okapů. Moc krátký na to abys s ním kamkoliv dosáhl.")
                BALKONV()
            elif "hák(prodloužený)" in inventar:
                print("Hák na čištění okapů prodloužený zlomeným tágem.")
                BALKONV()
            else:
                print("Zlomený hák na čištění okapů. Moc krátký na to abys s ním kamkoliv dosáhl.")
                BALKONV()
        if "okap" in volba or "rýna" in volba:
            if "zbraň" in inventar:
                print("Normální okap. Skrz díry z něj teče voda.")
                BALKONV()
            else:
                print("Starý okap ze kterého vytéká voda kvůli nějaké překážce.")
                BALKONV()
        if "dveře" in volba:
            print("Dveře vedoucí do domu jsou zablokované spadenou větví.")
            BALKONV()
        if "větev" in volba:
            print("Spadená větev po které je možné přelézt zpět do domu.")
            BALKONV()
    if "vezmi" in volba:
        if "hák" in volba:
            if "hák(zlomený)" in inventar or "hák(prodloužený)" in inventar:
                print("Hák už máš v inventáři.")
                BALKONV()
            else:
                print("Vzal sis zlomený hák")
                inventar.append("hák(zlomený)")
                BALKONV()
        else:
            print("Nevím jak to udělat")
            BALKONV()
    if "použij" in volba:
        if "izolepa" in volba and "tágo(zlomené)" in volba and "hák(zlomený)" in volba:
            if "izolepa" in inventar and "tágo(zlomené)" in inventar and "hák(zlomený)" in inventar:
                print("Slepil jsi zbytky tága a háku a vyrobil tak prodloužený hák.")
                inventar.remove("tágo(zlomené)")
                inventar.remove("hák(zlomený)")
                inventar.append("hák(prodloužený)")
                BALKONV()
            else:
                print("Nemáš všechny materiály.")
                BALKONV()
        if "lepidlo" in volba and "polovina klíče gama(a)" in volba and "polovina klíče gama(b)" in volba:
            if "lepidlo" in inventar and "polovina klíče GAMA(A)" in inventar and "polovina klíče GAMA(B)" in inventar:
                print("Slepil jsi dohromady klíč(GAMA)")
                inventar.remove("polovina klíče GAMA(A)")
                inventar.remove("polovina klíče GAMA(B)")
                inventar.append("klíč(GAMA)")
                BALKONV()
            else:
                print("Něco ti chybí.")
                BALKONV()
        if "svítilna" in volba and "baterie" in volba:
            if "svítilna(bez baterií)" in inventar and "baterie" in inventar:
                print("Vložil jsi baterie do svítilny.")
                inventar.remove("svítilna(bez baterií)")
                inventar.remove("baterie")
                inventar.append("svítilna")
                BALKONV()
            else:
                print("Tady něco schází.")
                BALKONV()
        if "nůž(tupý)" in volba and "brousek" in volba:
            if "nůž(tupý)" in inventar and "brousek" in inventar:
                print("Naostřil jsi nůž.")
                inventar.remove("nůž(tupý)")
                inventar.append("nůž(ostrý)")
                BALKONV()
            else:
                print("Něco potřebuješ")
                BALKONV()
        if "okno" in volba or "větev" in volba:
            CHODBAT()
    if "okap" in volba or "rýna" in volba:
        if "hák" in volba:
            if "hák(prodloužený)" in inventar:
                print("Použil jsi svůj prodloužený hák a vystrčil z okapu neznámý předmět. Zdá se že se jedná o nabitou zbraň. Rozhodl ses vzít si ji k sobě.")
                inventar.append("zbraň")
                BALKONV()
            else:
                print("Nemáš dostatečně dlouhý nástroj abys okap vyčistil.")
                BALKONV()
        else:
            print("Tohle nebude fungovat.")
            BALKONV()
    else:
        print("Tento příkaz neznám.")
        BALKONV()
#SC11 (Půda)
def PUDAT():
    global svitilna
    if svitilna==1:
        print("Nacházíš se na půdě.")
        print("Co uděláš?")
    else:
        print("Nacházíš se na půdě. Je tu hrozná tma a nic nevidíš.")
        print("Co uděláš?")
    PUDAV()
def PUDAV():
    global inventar
    global svitilna
    global skrin
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
    if volba=="inventář" or volba=="inventar":
        print(inventar)
        PUDAV()
    if volba:
        if svitilna==0:
            if "použij" in volba:
                if "svítilna" in volba:
                    if "svítilna" in inventar:
                        print("Svítilna se naštěstí opravdu rozsvítila a s její pomocí už vidíš vše co potřebuješ.")
                        svitilna=1
                        PUDAV()
                    else:
                        print("Nemáš si jak posvítit.")
                        PUDAV()
                if "poklop" in volba or "dveře" in volba:
                    CHODBAT()
                else:
                    print("To ti asi teď nepomůže.")
                    PUDAV()
            else:
                print("Nevidíš si ani na špičku nosu. Tohle nezvládneš")
                PUDAV()
            print("Je moc tma na to abys cokoliv rozeznal.")
            PUDAV()
        
        else:
            if "prozkoumej" in volba:
                if "papír" in volba:
                    if "papír(citronový)" in inventar:
                        print("Prázdný papír vonící po citrónu.")
                        PUDAV()
                    if "papír(vzkaz)" in inventar:
                        print("Na papíře je vzkaz hnědým písmem: '232.8°C'")
                        PUDAV()
                if "místnost" in volba: 
                    print("Tahle půda už zažila lepší časy. V celé mísnosti je znatelný zápach alkoholu. Napravo od poklopu se nachází regál se všemi možnými typy alkoholu. Nalevo od poklopu se pak nachází masivní železná skříň a napravo od ní je nástěnka s jediným papírem.")
                    PUDAV()
                if "regál" in volba:
                    print("Regál plný všemožných druhů alkoholu.")
                    PUDAV()
                if "skříň" in volba:
                    if skrin==0:
                        print("Masivní železná skříň. Je zamčená číselným zámkem. Na zámku je vyrytá značka '°F'")
                        PUDAV()
                    else:
                        print("Masivní železná skříň. Zdá se být orevřená.")
                        PUDAV()
                if "nástěnka" in volba:
                    if "papír" in inventar:
                        print("Na nástěnce už nic není.")
                        PUDAV()
                    else:
                        print("Na nástěnce je jeden papír. Zajimavé je že na papíře nic není, ale voní po citrónech.")
                        PUDAV()
            if "vezmi" in volba:
                if "papír" in volba or "lístek" in volba or "papírek" in volba:
                    if "papír" in inventar:
                        print("Papír už máš v inventáři.")
                    else:
                        print("Vzal sis k sobě papír.")
                        inventar.append("papír(citronový)")
                        PUDAV()
                if "alkohol" in volba:
                    if "alkohol" in inventar:
                        print("Alkohol už u sebe máš.")
                        PUDAV()
                    else:
                        print("Vzal sis k sobě láhev pálenky.")
                        inventar.append("alkohol")
                        PUDAV()
                else:
                    print("Nevím jak to udělat")
                    PUDAV()
            if "použij" in volba:
                if "poklop" in volba or "dveře" in volba:
                    CHODBAT()
                if "izolepa" in volba and "tágo(zlomené)" in volba and "hák(zlomený)" in volba:
                    if "izolepa" in inventar and "tágo(zlomené)" in inventar and "hák(zlomený)" in inventar:
                        print("Slepil jsi zbytky tága a háku a vyrobil tak prodloužený hák.")
                        inventar.remove("tágo(zlomené)")
                        inventar.remove("hák(zlomený)")
                        inventar.append("hák(prodloužený)")
                        PUDAV()
                    else:
                        print("Nemáš všechny materiály.")
                        PUDAV()
                if "lepidlo" in volba and "polovina klíče gama(a)" in volba and "polovina klíče gama(b)" in volba:
                    if "lepidlo" in inventar and "polovina klíče GAMA(A)" in inventar and "polovina klíče GAMA(B)" in inventar:
                        print("Slepil jsi dohromady klíč(GAMA)")
                        inventar.remove("polovina klíče GAMA(A)")
                        inventar.remove("polovina klíče GAMA(B)")
                        inventar.append("klíč(GAMA)")
                        PUDAV()
                    else:
                        print("Něco ti chybí.")
                        PUDAV()
                if "svítilna" in volba and "baterie" in volba:
                    if "svítilna(bez baterií)" in inventar and "baterie" in inventar:
                        print("Vložil jsi baterie do svítilny.")
                        inventar.remove("svítilna(bez baterií)")
                        inventar.remove("baterie")
                        inventar.append("svítilna")
                        PUDAV()
                    else:
                        print("Tady něco schází.")
                        PUDAV()
                if "nůž(tupý)" in volba and "brousek" in volba:
                    if "nůž(tupý)" in inventar and "brousek" in inventar:
                        print("Naostřil jsi nůž.")
                        inventar.remove("nůž(tupý)")
                        inventar.append("nůž(ostrý)")
                        PUDAV()
                    else:
                        print("Něco potřebuješ")
                        PUDAV()
                if "skříň" in volba:
                    if skrin==0:
                        A=input("První číslo:")
                        B=input("Druhé číslo:")
                        C=input("Třetí číslo:")
                        if A=="4" and B=="5" and C=="1":
                            print("Skříň se otevřela a v ní byl brousek, který sis vzal.")
                            inventar.append("brousek")
                            skrin=1
                            PUDAV()
                        else:
                            print("Nic se nestalo...")
                            PUDAV()
                    else:
                        print("Skříň je otevřená...")
                        PUDAV()
            else:
                print("Tento příkaz neznám.")
                PUDAV()
