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

    #Relasi
    
]))      
