menu = """
1 - Depósito
2 - Saque
3 - Extrato
0 - Sair
=> """
saldo = 0
saque = 500 
LIMITE_DIARIO = 3 
extrato = ""
numero_de_saque = 0
print('''
	=============================================
	Seja bem vindo ao Banco do Dev-desenrolado !!
	Obrigado pela preferência !
	=============================================''')
while True: 
	opcao = input(menu) 
	if opcao == '1': 
		valor_deposito = float(input('Informe o valor do depósito: \n')) 

		if valor_deposito < 0: 
			print('Valor inválido ! tente novamente...')
		else:	
			saldo += valor_deposito 
			extrato += f'Depósito: R${valor_deposito:.2f}\n' 
			print("Parabéns, a operação foi realizada com sucesso !")

	elif opcao == '2':
		valor_saque = float(input('Informe o valor do saque:\n')) 
		
		if valor_saque > saque : 
			print('Excedeu o limite de saque por operação')

		elif valor_saque > saldo: 
			print('Não foi possível concluir a operação, saldo insuficiente') 

		elif numero_de_saque >= LIMITE_DIARIO: 
			print('O Limite de saque diário foi atingido, transação não realizada.') 

		else:	
			saldo -= valor_saque 
			numero_de_saque += 1
			extrato += f'Saque: R${valor_saque:.2f}\n' 
		
	elif opcao == '3': 
		print('\n===========Extrato===========')
		print('Não há nenhuma movimentação' if not extrato else extrato)
		print(f'\nSaldo: R${saldo:.2f}')
		print('=============================')
	elif opcao == '0':
		print('''Obrigado por ter usado nossos serviços😁
Volte sempre !!''')
		break
	else:
		print('Operação inválida, por favor informe a opção correta.')

		