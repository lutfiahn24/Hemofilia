from logic import *

class FolKB(KB):
    def __init__(self, initial_clauses=[]):
        self.clauses = [] 
        for clause in initial_clauses:
            self.tell(clause)

    def tell(self, sentence):
        if is_definite_clause(sentence):
            self.clauses.append(sentence)
        else:
            raise Exception("Not a definite clause:{}".format(sentence))

    def ask_generator(self, query):
        q = expr(query)
        test_variables = variables(q)
        answers = fol_bc_ask(self, q)
        return sorted([dict((x, v) for x, v in list(a.items()) if x in test_variables) for a in answers], key=repr)

    def retract(self, sentence):
        self.clauses.remove(sentence)
    
    def fetch_rules_for_goal(self, goal):
        return self.clauses

kb_hemofilia = FolKB(map(expr, [
    'Laki(Rahmat)','Laki(Budi)','Laki(Ade)','Laki(Joko)','Laki(Dedi)','Laki(Adi)','Laki(Rizky)',

    'Perempuan(Nur)','Perempuan(Siti)','Perempuan(Reni)','Perempuan(Farah)','Perempuan(Dewi)','Perempuan(Aisyah)','Perempuan(Amira)','Perempuan(Sherly)','Perempuan(Fathia)','Perempuan(Balqis)',

    'Nikah(Rahmat,Nur)','Nikah(Budi,Siti)','Nikah(Ade,Reni)','Nikah(Joko,Dewi)','Nikah(Dedi,Aisyah)',

    'Ortu(Rahmat,Farah)','Ortu(Rahmat,Dewi)','Ortu(Nur,Farah)','Ortu(Nur,Dewi)','Ortu(Budi,Joko)','Ortu(Budi,Dedi)','Ortu(Siti,Joko)','Ortu(Siti,Dedi)','Ortu(Ade,Aisyah)','Ortu(Reni,Aisyah)','Ortu(Joko,Adi)','Ortu(Joko,Rizky)','Ortu(Joko,Amira)','Ortu(Dewi,Adi)','Ortu(Dewi,Rizky)','Ortu(Dewi,Amira)','Ortu(Dedi,Sherly)','Ortu(Dedi,Fathia)','Ortu(Dedi,Balqis)','Ortu(Aisyah,Sherly)','Ortu(Aisyah,Fathia)','Ortu(Aisyah,Balqis)',
    
    'SaudaraKandung(Farah,Dewi)','SaudaraKandung(Joko,Dedi)','SaudaraKandung(Adi,Rizky)','SaudaraKandung(Adi,Amira)','SaudaraKandung(Rizky,Amira)','SaudaraKandung(Sherly,Fathia)','SaudaraKandung(Sherly,Balqis)','SaudaraKandung(Fathia,Balqis)',
    
    'XHXH(Nur)',
    'XhXh(Siti)', 'XHXh(Reni)',

    'XHY(Rahmat)', 'XHY(Budi)', 'XhY(Ade)',
    
    #Relasi
    '(Perempuan(p) & (Ortu(i, p) & XHXH(i)) & (Ortu(j, p) & XHY(j))) ==> XHXH(p)', 
    '(Laki(p) & (Ortu(i, p) & XHXH(i)) & (Ortu(j, p) & XHY(j))) ==> XHY(p)', 

    '(Perempuan(p) & (Ortu(i, p) & XHXH(i)) & (Ortu(j, p) & XhY(j))) ==> XHXh(p)',
    '(Laki(p) & (Ortu(i, p) & XHXH(i)) & (Ortu(j, p) & XhY(j))) ==> XHY(p)',

    '(Perempuan(p) & (Ortu(i, p) & XHXh(i)) & (Ortu(j, p) & XHY(j))) ==> Tidak_diketahui(p)',
    '(Laki(p) & (Ortu(i, p) & XHXh(i)) & (Ortu(j, p) & XHY(j))) ==> Tidak_diketahui(p)',

    '(Perempuan(p) & (Ortu(i, p) & XHXh(i)) & (Ortu(j, p) & XhY(j))) ==> Tidak_diketahui(p)',
    '(Laki(p) & (Ortu(i, p) & XHXh(i)) & (Ortu(j, p) & XhY(j))) ==> Tidak_diketahui(p)',

    '(Perempuan(p) & (Ortu(i, p) & XhXh(i)) & (Ortu(j, p) & XHY(j))) ==> XHXh(p)',
    '(Laki(p) & (Ortu(i, p) & XhXh(i)) & (Ortu(j, p) & XHY(j))) ==> XhY(p)',

    '(Perempuan(p) & (Ortu(i, p) & XhXh(i)) & (Ortu(j, p) & XhY(j))) ==> XhXh(p)',
    '(Laki(p) & (Ortu(i, p) & XhXh(i)) & (Ortu(j, p) & XhY(j))) ==> XHY(p)',

    '(Ortu(i, p) & Tidak_diketahui(i)) ==> Tidak_diketahui(p)',
    'XHXH(p) & Ortu(i, p) ==> AnakPerempuanSehat(p, i)',
    'XHY(p) & Ortu(i, p) ==> AnakLakiSehat(p, i)',
    'XHXh(p) & Ortu(i, p) & Laki(i) ==> AnakPerempuanCarrier(p, i)',
    'XhY(p) & Ortu(i, p) ==> AnakLakiHemofilia(p, i)',
    'XHXH(p) ==> Sehat(p)',
    'XHY(p) ==> Sehat(p)',
]))
#Menentukan Anak Perempuan Carrier
print("1. Siapakah anak perempuan dari Rahmat yang mengidap carrier hemofilia?")
print(kb_hemofilia.ask_generator('AnakPerempuanCarrier(x, Rahmat)'), "\n")
#Menentukan Anak Laki-laki Sehat
print("2. Siapakah anak laki-laki dari Dewi yang sehat?")
print(kb_hemofilia.ask_generator('AnakLakiSehat(x, Dewi)'), "\n")
#Menentukan Anak Laki-laki Hemofilia
print("3. Siapakah anak laki-laki dari Ade yang mengidap hemofilia?")
print(kb_hemofilia.ask_generator('AnakLakiHemofilia(x, Ade)'), "\n")
#Menentukan Pengidap Hemofilia dari Anak Perempuan Carrier
print("4. Jika Amira adalah carrier hemofilia, siapa yang mengidap hemofilia?")
print(kb_hemofilia.ask_generator('AnakPerempuanCarrier(Amira, x)'), "\n")
#Menentukan Perempuan Sehat
print("5. Dalam family tree, siapa saja yang merupakan perempuan sehat?")
print(kb_hemofilia.ask_generator('XHXH(x)'), "\n")
#Menentukan Perempuan Carrier
print("6. Dalam family tree, siapa saja yang merupakan perempuan carrier?")
print(kb_hemofilia.ask_generator('XHXh(x)'), "\n")
#Menentukan Perempuan Hemofilia
print("7. Dalam family tree, siapa saja yang merupakan perempuan hemofilia?")
print(kb_hemofilia.ask_generator('XhXh(x)'), "\n")
#Menentukan Laki-laki Sehat
print("8. Dalam family tree, siapa saja yang merupakan laki-laki sehat?")
print(kb_hemofilia.ask_generator('XHY(x)'), "\n")
#Menentukan Laki-laki Hemofilia
print("9. Dalam family tree, siapa saja yang merupakan laki-laki hemofilia?")
print(kb_hemofilia.ask_generator('XhY(x)'), "\n")
#Menentukan Anggota yang Memiliki Beragam Kemungkinan
print("10. Dalam family tree, siapa saja yang berpotensi sehat atau carrier atau hemofilia?")
print(kb_hemofilia.ask_generator('Tidak_diketahui(x)'), "\n")

#Menentukan Anggota yang Sehat
print("11. Dalam family tree, siapa saja yang sehat?")
print(kb_hemofilia.ask_generator('Sehat(x)'), "\n")
