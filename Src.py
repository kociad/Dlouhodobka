import winsound
import time
#SC00_BLANK
def BLANKT():
    print("PLACEHOLDER") #Úvodní text scény
    print("Co uděláš?")
def BLANKV():
    global inventar #Inventář musí být vždy globální
    volba=input("Zadej příkaz:")
    volba=volba.lower()
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
    print("Vítej do mojí hry! Pro provedení akce piš do příkazové řádky. Hra má tři hlavní akce: 'Prozkoumej' 'Vezmi' a 'Použij'. Svůj inventář si prohlédneš příkazem 'inventář'. Tyto akce kombinuj s předměty v herním světě nebo v inventáři. Objekty piš vždy v prvním pádě (hlavu=hlava atd.). Přeji příjemné hraní")
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
    if "dbg_opv" in volba:
        NOVA_HRA()
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
    global nuz_tupy
    nuz_tupy=1
    global dvere_vahy_zamceno
    dvere_vahy_zamceno=1
    global vana_naplnena
    vana_naplnena=1
    global pojistka
    pojistka=0
    global krb_plamen
    krb_plamen=0
    global hak_zlomeny
    hak_zlomeny=1
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
    if volba=="inventář" or volba=="inventar":
        print(inventar)
        OPV()
    if "prozkoumej" in volba:
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
        #Nutno dopsat inventář
        else:
            print("Nevím jak to udělat.")
            OPV()
    if "vezmi" in volba:
        print("Tak to asi nepůjde.")
        OPV()
    if "použij" in volba:
        if "tv" in volba or "televize" in volba:
            print("Televize se zapla. V televizi jsou zprávy o nedávných vraždách. Pachatele se nepodařilo nikdy najít, ale všechny oběti měly do dlaní vyřezaný kříž. Po chvíli se rozhodneš televizi vypnout.")
            OPV()
        if "dveře" in volba:
            if "hlavní" in volba:
                if zamek_alfa_zamcen==1 or zamek_beta_zamcen==1 or zamek_gama_zamcen==1:
                    print("Snažíš se dveře otevřít, ale je zamčeno.")
                    OPV()
                else:
                    if "zbraň" in inventar:
                        print("PLACEHOLDER_GOOD_ENDING")
                        return
                    else:
                        print("PLACEHOLDER_BAD_ENDING")
                        return
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
        if "hák" in volba:
            if "hák" in inventar:
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
                        if "klíč(alfa)" in inventar:
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
                        if "klíč(beta)" in inventar:
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
                        if "klíč(gama)" in inventar:
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
        if "průchod" or "kuchyně" in volba:
            KUCHYNET()
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
    if volba=="inventář" or volba=="inventar":
        print(inventar)
        KUCHYNEV()
    if "prozkoumej" in volba:
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
        if "průchod" in volba or "pokoj" in volba:
            OPT2()
        if "trezor" in volba:
            if trezor_zamcen==1:
                C1=int(input("První číslo:"))
                C2=int(input("Druhé číslo:"))
                C3=int(input("Třetí číslo:"))
                C4=int(input("Čtvrté číslo:"))
                if C1==6 and C2==8 and C3==3 and C4==1:
                    trezor_zamcen==0
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
        BLANKV()
    
