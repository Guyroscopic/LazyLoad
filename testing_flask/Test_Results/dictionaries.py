
student_dictionary_a = {'Abdul Rafey' : 242863, 'Hammad Ahmed' : 266578, 'Eesha Arif': 242610,\
                        'Safi Ur Rehman': 241984, 'Syed Babar Tameez': 252769, "Martian":345632,"SirMoin":564234,\
                        "abdul bari":764986,"Gatu":547578,"FatimaAunti":876098,"SirIbrar":576952,"Ahmed Candy":348321,\
                        "Zaleeel Asif":765987}
CMS_ID_a=[]
names_a=[]
set_CMS_ID_a = set()
set_names_a=set()

for i, j in student_dictionary_a.items():
    CMS_ID_a.append(j)
    names_a.append(i)

def list_set(list,set):
    for i in list:
        set.add(i)

list_set(CMS_ID_a,set_CMS_ID_a)
list_set(names_a,set_names_a)

                         ###Dictionaries###
#marks_final_a
#marks_fall_a
#marks_spring_a

#attendance_physics_a
#attendance_chemistry_a