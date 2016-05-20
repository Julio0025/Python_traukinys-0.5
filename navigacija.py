from lokomotyvas import Lokomotyvas
from vagonas import Vagonas
from traukinys import Traukinys

traukiniai = []
current_train = None

ans=True
while ans:
    if len(traukiniai) == 1:
        current_train = traukiniai[0]
    print ("""
    ------>>>>> %s
    1.Sukurti traukini 
    2.Prideti lokomotyva
    3.Prideti vagona
    4.Issaugoti Traukinius
    5.Uzkrauti issaugotus traukinius
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
            
            print("y")
        elif choice==4:
            print("y")
        elif choice ==10:
            print("aciu kad dirbote")
            ans=False
    except ValueError:
        print("blagai ivedet pasirinkima")


