from lokomotyvas import Lokomotyvas
from vagonas import Vagonas
from traukinys import Traukinys

traukiniai = []
current_train = None

ans=True
while ans:
    if len(traukiniai) == 0:
        current_train = None
    if len(traukiniai) == 1:
        current_train = traukiniai[0]
    print ("""
    ------>>>>> %s
    1.Sukurti traukini 
    2.Prideti lokomotyva
    3.Prideti vagona
    4.Prideti krovini
    5.Pasikeisti Dabartini traukini
    6.Istrinti dabartinti traukini arba jo vagona/lokomotyva
    7.Issaugoti dabartinius turimus traukinius
    8.Uzkrauti issaugotus traukinius
    
    """%(current_train))
    try:
        choice = int(input())
        if choice==1:
            print("iveskite norima traukinio pavadinima")
            try:
                name_trauk = input()
                a = Traukinys(name_trauk)
                traukiniai.append(a)
                print("pavyko")
            except ValueError:
                print("blogai ivedet")
        elif choice==2:
            if current_train == None:
                print("is pradziu pasirinkite/pridekite nauja traukini")
                continue
            print("iveskite lokomotyvo pavadinima")
            try:
                name_lok = input()
                print("iveskite lokomotyvo: 1) mase")
                try:
                    mas_lok = int(input())
                    print("2) Tempiamaja galia")
                    tempGalia_lok = int(input())
                    current_train.addLokomotyvas(name_lok,mas_lok,tempGalia_lok)
                except ValueError:
                    print("blogai ivedet duomenis")
            except ValueError:
                print("blogai ivedet pavadinima")
                
        elif choice==3:
            if current_train == None:
                print("is pradziu pasirinkite/pridekite nauja traukini")
                continue
            print("iveskite vagono Pavadinima")
            try:
                name_vag = input()
                print("iveskite vagono: 1) Vagono mase(tonos)")
                try:
                    mase_vag  = int(input())
                    print("2) Maksimalia mase vagono(tonos)")
                    maseM_vag = int(input())
                    print("3) Vagono ID")
                    ID = int(input())
                    current_train.addVagonas(name_vag,mase_vag,maseM_vag, ID)
                except ValueError:
                    print("ivedet ne skaiciu")
            except ValueError:
                print("blogai ivedet pavadinima")
            
        elif choice==4:
            if current_train.vagonai == []:
                print("is pradziu pridekite vagona")
                continue
            print("Iveskite mase krovinio")
            try:
                input_krov = int(input())
                current_train.pakrautiKrovini(input_krov)
            except ValueError:
                print("blogai ivedet duomenis")
                
        elif choice==5:
            cnt = 0
            if len(traukiniai) == 0 or len(traukiniai) == 1:
                print("Neturite is ko rinktis, pridekite nauja traukini")
                try:
                    input_mas = int(input())
                except ValueError:
                    print("ivedet ne skaiciu")
            for traukinys in traukiniai:
                cnt += 1
                print(cnt, " " , traukinys)
            try:
                nmber = int(input())
            except ValueError:
                 print("ivedet ne skaiciu")
            current_train = traukiniai[nmber-1]
            
        elif choice==6:
            if current_train == None:
                print("nepasirinktas traukinys")
                continue
            print("""pasirinkite ka norite istrinti:
                     1) Dabartini traukini
                     2) Traukinio lokomotyva
                     3) Traukinio vagona
                """)
            try:
                choice_del = int(input())
            except ValueError:
                print("ivedet ne skaiciu")
            if choice_del==1:
                traukiniai.remove(current_train)
                if len(traukiniai) != 0:
                    current_train = traukiniai[0]
            elif choice_del==2:
                if current_train.vagonai == []:
                    print("nera lokomotyvu")
                    continue
                cnt_lok_del = 0
                for item in current_train.lokomotyvai:
                    cnt_lok_del += 1
                    print(cnt_lok_del,"  ",item)
                print("print pasirinkite kuri norite istrinti")
                try:
                    choice_del_lok = int(input())-1
                    if choice_del_lok < 0 or choice_del_lok > len(current_train.lokomotyvai)-1:
                        print("tokio lokomotyvo nera")
                        continue
                    else:
                        current_train.lokomotyvai.remove(current_train.lokomotyvai[choice_del_lok])
                        print("veikia")
                except ValueError:
                    print("blogai ivestas skaiciu")
            elif choice_del==3:
                cnt_vag_del = 0
                if current_train.vagonai == []:
                    print("nera vagonu")
                    continue
                for item in current_train.vagonai:
                    cnt_vag_del += 1
                    print(cnt_vag_del,"  ",item)
                print("print pasirinkite kuri norite istrinti")
                try:
                    choice_del_vag = int(input())-1
                    if choice_del_vag < 0 or choice_del_vag > len(current_train.vagonai)+1:
                        print("tokio vagono nera")
                        continue
                    else:
                        current_train.vagonai.remove(current_train.vagonai[choice_del_vag])
                        print("istrinta")
                except ValueError:
                    print("blogai ivestas skaiciu")
##          
            else:
                print("neteisingai ivestas pasirinkimas")
                continue
                 
                
        elif choice ==10:
            print("aciu kad dirbote")
            ans=False
    except ValueError:
        print("blagai ivedet pasirinkima")


















