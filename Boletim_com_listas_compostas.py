noteList_student = []
data = []
reckon = 0

while True:

    reckon += 1
    print('---' * 15)
    student = str(input(f'Digite o nome do {reckon} Aluno: ')).upper().strip()
    data.append(student)
    print('===' * 15)

    for _ in range (2):

        while True:
            try:
                note_student = float(input(f'Informe a nota da avaliação {_ + 1}: '))
                
                if note_student >= 0 and note_student <= 10:
                    data.append(note_student)
                    break
            
            except ValueError:
                print('~~~' * 15)
                print('Verificamos um erro. Por favor, digite novamente.')

            else:
                print('~~~'*15)
                print('Por favor, digite somente notas entre 0 e 10.')


    noteList_student.append(data[:])
    data.clear()

    print('===' * 15)
    cont = str(input(f'Deseja cadastrar mais alunos? Digite [S/N]: ')).strip().upper()
    if cont != 'N' and cont != 'S':
        while True:

            print('~~~' * 15)
            print('Por favor, digite apenas [S/N].')
            cont = str(input(f'Deseja cadastrar mais alunos? Digite [S/N]: ')).upper().strip()
            
            if cont == 'N' or cont == 'S':
                break

    if cont == 'S':
        while True:
            print('===' * 15)
            student = str(input('Digite o nome do Aluno: ')).upper().strip()
            data.append(student)

            for _ in range (2):
                while True:    
                    try:
                        note_student = float(input(f'Informe a nota da avaliação {_ + 1}: '))
                        
                        if note_student >= 0 and note_student <= 10:
                            data.append(note_student)
                            break
                    
                    except ValueError:
                        print('~~~' * 15)
                        print('Verificamos um erro. Por favor, digite novamente.')
                    
                    else:
                        print('~~~' * 15)
                        print('Por favor, digite somente notas entre 0 e 10.')


            noteList_student.append(data[:])
            data.clear()


            print('===' * 15)
            cont = str(input(f'Deseja cadastrar mais alunos? Digite [S/N]: ')).strip().upper()
           
            if cont == 'N':
                for m in noteList_student:
                    print('===' * 15)
                    print(f'{m[0]} teve {(m[1] + m[2]) / 2} pontos de média.')
                break

    elif cont == 'N':
        print('===' * 15)
        
        for m in noteList_student:
            print(f'{m[0]} teve {(m[1] + m[2]) / 2} pontos de média.')


    print('===' * 15)
    check_student = str(input(f'Deseja conferir a nota de algum aluno? Digite [S/N]: ')).upper().strip()
            
    
    if check_student == 'S':
        while True:
            try:
                print('===' * 15)
                check_note = str(input(f'Digite o nome do aluno no qual deseja conferir a nota: ')).upper().strip()
                found = False

                for v in noteList_student:
                    print('===' * 15)

                    if v[0] == check_note:
                        found = True
                        print(f'Na avaliação 1 o(a) {v[0]} obteve {v[1]} pontos e na avalição 2 conseguiu {v[2]} pontos.')
                        break

                    elif v[0] != check_note:
                        while found == False:
                            print('~~~' * 15)
                            print('Aluno não encontrado. Digite o nome novamente.')
                            check_note = str(input(f'Digite o nome do aluno no qual deseja conferir a nota: '))
                            
                            if v[0] == check_note:
                                print(f'Na avaliação 1 o(a) {v[0]} obteve {v[1]} pontos e na avalição 2 conseguiu {v[2]} pontos.')
                                break

                print('===' * 15)
                cont = str(input('Deseja vericar a nota de mais alunos? Digite [S/N]: ')).upper().strip()
                
                if cont != 'S' and cont != 'N':
                    while True:
                        print('~~~' * 15)
                        print('Por favor, digite apenas [S/N].')
                        cont = str(input('Deseja verificar a nota de mais alunos? Digite [S/N]: ')).upper().strip()
                        
                        if cont == 'N' and cont == 'S':
                                break    
                        
                if cont == 'N':
                    break

            except:
                print('~~~' * 15)
                print('Nome incorreto. Por favor, digite novamente.')

    elif check_student == 'N':
        break

    elif check_student != 'N' or check_student != 'S':
        while True:
            
            print('~~~' * 15)
            print('Por favor, digite apenas [S/N].')
            check_student = str(input(f'Deseja Conferir a nota de algum aluno? Digite [S/N]: ')).upper().strip()

            if check_student == 'N': 
                break

            elif check_student == 'S':
                while True:
                    try:
                        print('===' * 15)
                        check_note = str(input(f'Digite o nome do aluno no qual deseja conferir a nota: ')).upper().strip()

                        for v in noteList_student:
                            print('===' * 15)

                            if v[0] == check_note:
                                print(f'Na avaliação 1 o(a) {v[0]} obteve {v[1]} pontos e na avalição 2 conseguiu {v[2]} pontos.')
                                break

                            elif v[0] != check_note:
                                while True:
                                    print('~~~' * 15)
                                    print('Aluno não encontrado. Digite o nome novamente.')
                                    check_note = str(input(f'Digite o nome do aluno no qual deseja conferir a nota: '))
                                    
                                    if v[0] == check_note:
                                        print(f'Na avaliação 1 o(a) {v[0]} obteve {v[1]} pontos e na avalição 2 conseguiu {v[2]} pontos.')
                                        break

                        print('===' * 15)
                        cont = str(input('Deseja vericar a nota de mais alunos? Digite [S/N]: ')).upper().strip()
                        
                        if cont != 'S' and cont != 'N':
                            while True:
                                print('~~~' * 15)
                                print('Por favor, digite apenas [S/N].')
                                cont = str(input('Deseja verificar a nota de mais alunos? Digite [S/N]: ')).upper().strip()
                                
                                if cont == 'N' and cont == 'S':
                                        break    
                                
                        if cont == 'N':
                            break

                    except:
                        print('~~~' * 15)
                        print('Nome incorreto. Por favor, digite novamente.')
   

    print('===' * 15)
    cont = str(input(f'Deseja cadastrar outros alunos? Digite [S/N]: ')).upper().strip()
    if cont != 'N' and cont != 'S':
        while True:

            print('~~~' * 15)
            print('Por favor, digite apenas [S/N].')
            cont = str(input(f'Deseja cadastrar outros alunos? Digite [S/N]: ')).upper().strip()
            
            if cont == 'N' and cont == 'S':
                break
    if cont == 'S':
        print()

    elif cont == 'N':
        break