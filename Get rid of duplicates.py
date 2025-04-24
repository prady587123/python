#Get rid of duplicates
student_data = {'id1':{'name' : ['Pradyumnan'], 'class' : ['V'],'subject integeration' : ['english,maths,science'] },
'id2':{'name' : ['Pradyu'], 'class' : ['V'],'subject integeration' : ['english,maths,science'] },
'id3':{'name' : ['Prady'], 'class' : ['V'],'subject integeration' : ['english,maths,science'] },
'id4':{'name' : ['Prad'], 'class' : ['V'],'subject integeration' : ['english,maths,science'] },}
result = {}
for key,value in  student_data.items():
    if value not in result.values():
        result[key] = value

    print(result)