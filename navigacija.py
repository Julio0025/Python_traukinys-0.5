from lokomotyvas import Lokomotyvas
from vagonas import Vagonas
from traukinys import Traukinys
from traukinys import openTraukinys, saveTraukinys
import doctest


def Navigacija():
    """test init
	>>> a = Traukinys("Traukinys")
        >>> Navigacija()
        >>> print(a)
        traukinys: Traukinys, Dabartine sastato mase: 140,
                   galia: 500, bendra kroviniu mase 0
                   lokomotyvu = 1, vagonu = 1
        >>> 1
        
        >>> a.addLokomotyvas(" Antano_loko ",100,500)
        lokomotyvas sekmingai pridetas
        
        >>> a.addVagonas("vagons1",40,500, 350)
        vagonas sekmingai pridetas
        
        >>> print(a)
        traukinys: Traukinys, Dabartine sastato mase: 140,
                   galia: 500, bendra kroviniu mase 0
                   lokomotyvu = 1, vagonu = 1 
        
        >>> a.pakrautiKrovini(100)
        pavyko prideti krovini i vagons1 dar liko 400 vietos siame vagone
        
    """
 
    traukiniai = openTraukinys()
    ans = True
    current_train = None

    
    def choice1(ans):
        print("iveskite norima traukinio pavadinima")
        try:
            name_trauk = input()
            a = Traukinys(name_trauk)
            traukiniai.append(a)
            print("pavyko")
            return ans == True
        except ValueError:
            print("blogai ivedet")
            return ans == True

        
    def choice2(current_train, ans):
        if current_train == None:
            print("is pradziu pasirinkite/pridekite nauja traukini")
            return ans==True
        print("iveskite lokomotyvo pavadinima")
        try:
            name_lok = input()
            print("iveskite lokomotyvo: 1) mase")
            try:
                mas_lok = int(input())
                print("2) Tempiamaja galia")
                tempGalia_lok = int(input())
                if mas_lok < 0 or tempGalia_lok < 0:
                    raise ValueError
                current_train.addLokomotyvas(
                    name_lok, mas_lok, tempGalia_lok)
            except ValueError:
                print("blogai ivedet duomenis,lokomotyvas nepridetas ")
                return ans == True
        except ValueError:
            print("blogai ivedet pavadinima")
            return ans == True

            
    def choice3(current_train, ans):
        if current_train == None:
            print("is pradziu pasirinkite/pridekite nauja traukini")
            return ans == True
        print("iveskite vagono Pavadinima")
        try:
            name_vag = input()
            print("iveskite vagono: 1) Vagono mase(tonos)")
            try:
                mase_vag = int(input())
                print("2) Maksimalia mase vagono(tonos)")
                maseM_vag = int(input())
                print("3) Vagono ID")
                ID = int(input())
                if mase_vag < 0 or maseM_vag < 0:
                    raise ValueError
                current_train.addVagonas(name_vag, mase_vag, maseM_vag, ID)
            except ValueError:
                print("blogai ivedet duomenis, vagonas nepridetas")
                return ans== True
        except ValueError:
            print("blogai ivedet pavadinima")
            return ans== True

        
    def choice4(current_train, ans):
        if current_train == None:
            print("is pradziu pridekite traukini")
            return ans == True
        if current_train.vagonai == []:
            print("is pradziu pridekite vagona")
            return ans == True
        print("Iveskite mase krovinio")
        try:
            input_krov = int(input())
            if input_krov < 0:
                raise ValueError
            current_train.pakrautiKrovini(input_krov)
        except ValueError:
            print("blogai ivedet duomenis")
            return ans == True

        
    def choice5(ans):
        if traukiniai == []:
            print("nera traukiniu")
            return ans == True
        print("""pasirinkite kaip norite surusiuoti traukinius
              1) Bendra mase
              2) Bendra galia
              3) bendra Kroviniu mase
              """)
        try:
            input_sort = int(input())
            if input_sort < 0 or input_sort > 4:
                raise ValueError
            if input_sort == 1:
                def maseTrauk(traukinys):
                    return traukinys.bendraMase
                print(sorted(traukiniai, key=maseTrauk))
            if input_sort == 2:
                def galiaTrauk(traukinys):
                    return traukinys.galiaTrauk
                print(sorted(traukiniai, key=galiaTrauk))
            if input_sort == 3:
                def bendraKrovMaseTrauk(traukinys):
                    return traukinys.bendraKroviniuMase
                print(sorted(traukiniai, key=bendraKrovMaseTrauk))
        except ValueError:
            print("Netinkamai ivestas pasirinkimas")
            return ans == True
                

    def choice6(ans):
        cnt = 0
        if len(traukiniai) == 0 or len(traukiniai) == 1:
            print("Neturite is ko rinktis, pridekite nauja traukini")
            return ans == True
        for traukinys in traukiniai:
            cnt += 1
            print(cnt, " ", traukinys)
        try:
            nmber = int(input()) - 1
        except ValueError:
            print("ivedet ne skaiciu")
            return ans == True
        if nmber < 0 or nmber > len(traukiniai) - 1:
            print("tokio traukinio nera")
            return ans == True
        return traukiniai[nmber]

        
    def choice7(current_train,ans):
        if current_train == None:
            print("nepasirinktas traukinys")
            return ans == True
        print("""pasirinkite ka norite istrinti:
                 1) Dabartini traukini
                 2) Traukinio lokomotyva
                 3) Traukinio vagona
            """)
        try:
            choice_del = int(input())
        except ValueError:
            print("ivedet ne skaiciu")
            return ans == True
        if choice_del == 1:
            if current_train == None:
                print("nepasirinktas traukinys")
                return ans == True
            traukiniai.remove(current_train)
            if len(traukiniai) != 0:
                current_train = traukiniai[0]
        elif choice_del == 2:
            if current_train.lokomotyvai == []:
                print("nera lokomotyvu")
                return ans == True
            if current_train.vagonai != []:
                print("negalima trinti lokomotyvo, jei traukinys turi vagonu")
                return ans == True
            cnt_lok_del = 0
            for item in current_train.lokomotyvai:
                cnt_lok_del += 1
                print(cnt_lok_del, "  ", item)
            print("print pasirinkite kuri norite istrinti")
            try:
                choice_del_lok = int(input()) - 1
                if choice_del_lok < 0 or choice_del_lok > len(current_train.lokomotyvai) - 1:
                    print("tokio lokomotyvo nera")
                    return ans == True
                else:
                    adjust = current_train.lokomotyvai[choice_del_lok]
                    current_train.bendraMase -= adjust.mase
                    current_train.galiaTrauk -= adjust.tempGalia
                    current_train.lokomotyvai.remove(
                    current_train.lokomotyvai[choice_del_lok])
            except ValueError:
                print("blogai ivestas skaiciu")
                return ans == True
        elif choice_del == 3:
            cnt_vag_del = 0
            if current_train.vagonai == []:
                print("nera vagonu")
                return ans == True
            for item in current_train.vagonai:
                cnt_vag_del += 1
                print(cnt_vag_del, "  ", item)
            print("print pasirinkite kuri norite istrinti")
            try:
                choice_del_vag = int(input()) - 1
                if choice_del_vag < 0 or choice_del_vag > len(current_train.vagonai) + 1:
                    print("tokio vagono nera")
                    return ans == True
                else:
                    adjust = current_train.vagonai[choice_del_vag]
                    current_train.bendraMase -= adjust.mase + adjust.maseKroviniu
                    current_train.bendraKroviniuMase -= adjust.maseKroviniu
                    current_train.vagonai.remove(
                        current_train.vagonai[choice_del_vag])
                    print("istrinta")
            except ValueError:
                print("blogai ivestas skaiciu")
        else:
            print("neteisingai ivestas pasirinkimas")
            return ans == True

    while ans:
        if len(traukiniai) == 0:
            current_train = None
        if len(traukiniai) == 1:
            current_train = traukiniai[0]
            
        print ("""
        Dabartinis pasirinktas traukinys >>>>> %s
        1.Sukurti traukini
        2.Prideti lokomotyva
        3.Prideti vagona
        4.Prideti krovini
        5.Perziureti surusiuota sarasa traukinu
        6.Pasikeisti Dabartini traukini
        7.Istrinti dabartinti traukini arba jo vagona/lokomotyva
        8.Issaugoti dabartinius turimus traukinius
        9.Baigti darba

        """ % (current_train))
        try:
            choice = int(input())
            
            if choice == 1:
                choice1(ans)
            elif choice == 2:
                choice2(current_train, ans)
 
            elif choice == 3:
                choice3(current_train, ans)
        
            elif choice == 4:
                choice4(current_train, ans)
    
            elif choice == 5:
                choice5(ans)

            elif choice == 6:
                current_train = choice6( ans)

            elif choice == 7:
               choice7(current_train, ans)
  
            elif choice == 8:
                saveTraukinys(traukiniai)
            elif choice == 9:
                print("aciu kad dirbote")
                ans = False
        except ValueError:
            print("blagai ivedet pasirinkima")



if __name__ == "__main__":
    Navigacija()
    doctest.testmod()













