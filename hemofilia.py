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
    'XHXH(p) ==> Sehat(p)',
    'XHY(p) ==> Sehat(p)',
]))    
print(kb_hemofilia.ask_generator('XHXH(x)'))
print(kb_hemofilia.ask_generator('XHXh(x)'))
print(kb_hemofilia.ask_generator('XhXh(x)'))
print(kb_hemofilia.ask_generator('XHY(x)'))
print(kb_hemofilia.ask_generator('XhY(x)'))
print(kb_hemofilia.ask_generator('Tidak_diketahui(x)'))
print(kb_hemofilia.ask_generator('Sehat(x)'))