#тема проекта, состав команды, которая будет выполнять проект, можно добавить тему и команду, удалить тему и комманду,
#изменить состав команды через пользовательский ввод, все сохраняется в файл
jornal = {}
members = []
def add_zapis(*team_member, project_name):
    with open("jornal.txt", "+a", uncoding = "utf-8") as f:
        while True:
            if team_member == input('введите участников команды (чтобы прекратить введите стоп): '):
                members.append(team_member)
            elif team_member.lower() == "стоп":
                break
        project_name = input('введите название проекта: ') 
    jornal.append(f"{project_name}: {members}")      
    f.close()
       
def show(project_name, team_member):
    with open("jornal.txt", "r", encoding = 'utf-8') as f:
        for index, (project_name, team_member) in enumerate(jornal.items()):
            yield f"{index+1}. {project_name} -> {members}"        
           
def remove_member(team_member):
    a = int(input('введите номер записи'))
    if a < 0 or a > len(jornal):
        print('такого номера нет')
    print(jornal(members)[a])
    removed = input('введите имя участника для удаления: ')
    for i in range(len(members)):
        if removed == team_member[i]:     
            jornal(members)[a] = members.pop(team_member[i])

def main():
    choise = input('что хотите сделать:\n1 - add \n2 - show \n3 - remove \n')   
    if choise == '1':
        add_zapis()
    elif choise == '2':
        show()
    elif choise == '3':
        remove_member()
    else:
        print('такой опции нет')    

   
if __name__ == "__main__":
    main()  
   # with open("jornal.txt", "+a", uncoding = "utf-8") as f
        
    