print('Script para msotrar informações dos valores digitados')
valor = input('Digite algo: ')
print('Informações obtidas de {}...'.format(valor))
print('É alfanumérico: {} \nÉ alfabético: {} \nÉ decimal: {} \nÉ um dígito: {} \nÉ identificador: {} '
      '\nÉ minúsculo: {} \nÉ número: {} \nÉ imprimível: {} \nÉ espaço: {} \nÉ título: {} \nÉ maiúsculo: {} '
      '\nÉ do tipo: {}'.format(valor.isalnum(), valor.isalpha(), valor.isdecimal(), valor.isdigit(),
      valor.isidentifier(), valor.islower(), valor.isnumeric(), valor.isprintable(),
      valor.isspace(), valor.istitle(), valor.isupper(), type(valor)))﻿