from datetime import datetime
import os

def limpar_tela():
    """Limpa a tela do terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def obter_valor(mensagem):
    """Obtém um valor numérico válido do usuário"""
    while True:
        try:
            valor = float(input(mensagem))
            if valor < 0:
                print("❌ Valor não pode ser negativo!")
                continue
            return valor
        except ValueError:
            print("❌ Por favor, digite um valor numérico válido!")

def formatar_moeda(valor):
    """Formata valor para moeda brasileira"""
    return f"R$ {valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

def obter_timestamp():
    """Retorna timestamp atual formatado"""
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def exibir_menu():
    """Exibe o menu principal"""
    print("=" * 50)
    print("           🏦 SISTEMA BANCÁRIO 🏦")
    print("=" * 50)
    print()
    print("📋 OPÇÕES DISPONÍVEIS:")
    print("[1] 💰 Depositar")
    print("[2] 💸 Sacar")
    print("[3] 📄 Extrato")
    print("[4] ℹ️  Consultar Informações da Conta")
    print("[0] 🚪 Sair")
    print()
    print("=" * 50)

def depositar(saldo, extrato):
    """Realiza operação de depósito"""
    print("\n💰 DEPÓSITO")
    print("-" * 20)
    
    valor = obter_valor("Informe o valor do depósito: R$ ")
    
    if valor == 0:
        print("⚠️  Operação cancelada - valor zero não é permitido.")
        return saldo, extrato
    
    saldo += valor
    timestamp = obter_timestamp()
    extrato += f"{timestamp} | Depósito: {formatar_moeda(valor)}\n"
    
    print(f"✅ Depósito realizado com sucesso!")
    print(f"💰 Valor depositado: {formatar_moeda(valor)}")
    print(f"💳 Novo saldo: {formatar_moeda(saldo)}")
    
    return saldo, extrato

def sacar(saldo, extrato, numero_saques, limite, LIMITE_SAQUES):
    """Realiza operação de saque"""
    print("\n💸 SAQUE")
    print("-" * 20)
    
    # Verificações iniciais
    if numero_saques >= LIMITE_SAQUES:
        print(f"❌ Limite de saques diários excedido! ({numero_saques}/{LIMITE_SAQUES})")
        return saldo, extrato, numero_saques
    
    if saldo == 0:
        print("❌ Não é possível sacar - saldo zerado!")
        return saldo, extrato, numero_saques
    
    print(f"💳 Saldo disponível: {formatar_moeda(saldo)}")
    print(f"📊 Limite por saque: {formatar_moeda(limite)}")
    print(f"🔢 Saques restantes hoje: {LIMITE_SAQUES - numero_saques}")
    print()
    
    valor = obter_valor("Informe o valor do saque: R$ ")
    
    if valor == 0:
        print("⚠️  Operação cancelada - valor zero não é permitido.")
        return saldo, extrato, numero_saques
    
    # Validações
    if valor > saldo:
        print(f"❌ Saldo insuficiente! Saldo atual: {formatar_moeda(saldo)}")
    elif valor > limite:
        print(f"❌ Valor excede o limite por saque: {formatar_moeda(limite)}")
    else:
        saldo -= valor
        numero_saques += 1
        timestamp = obter_timestamp()
        extrato += f"{timestamp} | Saque: {formatar_moeda(valor)}\n"
        
        print(f"✅ Saque realizado com sucesso!")
        print(f"💸 Valor sacado: {formatar_moeda(valor)}")
        print(f"💳 Novo saldo: {formatar_moeda(saldo)}")
        print(f"🔢 Saques restantes hoje: {LIMITE_SAQUES - numero_saques}")
    
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    """Exibe o extrato da conta"""
    print("\n" + "=" * 50)
    print("           📄 EXTRATO BANCÁRIO")
    print("=" * 50)
    
    if not extrato:
        print("\n⚠️  Nenhuma movimentação foi realizada.")
    else:
        print("\n📋 HISTÓRICO DE TRANSAÇÕES:")
        print("-" * 50)
        print(extrato)
    
    print("-" * 50)
    print(f"💰 SALDO ATUAL: {formatar_moeda(saldo)}")
    print("=" * 50)

def exibir_info_conta(saldo, numero_saques, limite, LIMITE_SAQUES):
    """Exibe informações da conta"""
    print("\n" + "=" * 50)
    print("           ℹ️  INFORMAÇÕES DA CONTA")
    print("=" * 50)
    print(f"💰 Saldo atual: {formatar_moeda(saldo)}")
    print(f"📊 Limite por saque: {formatar_moeda(limite)}")
    print(f"🔢 Saques realizados hoje: {numero_saques}/{LIMITE_SAQUES}")
    print(f"🔢 Saques restantes: {LIMITE_SAQUES - numero_saques}")
    print("=" * 50)

def main():
    """Função principal do sistema"""
    # Variáveis do sistema
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    
    print("🎉 Bem-vindo ao Sistema Bancário!")
    input("Pressione ENTER para continuar...")
    
    while True:
        limpar_tela()
        exibir_menu()
        
        try:
            opcao = input("👉 Digite a opção desejada: ").strip()
            
            if opcao == "1":
                saldo, extrato = depositar(saldo, extrato)
                
            elif opcao == "2":
                saldo, extrato, numero_saques = sacar(
                    saldo, extrato, numero_saques, limite, LIMITE_SAQUES
                )
                
            elif opcao == "3":
                exibir_extrato(saldo, extrato)
                
            elif opcao == "4":
                exibir_info_conta(saldo, numero_saques, limite, LIMITE_SAQUES)
                
            elif opcao == "0":
                print("\n👋 Obrigado por usar nosso sistema!")
                print("💝 Tenha um ótimo dia!")
                break
                
            else:
                print("❌ Opção inválida! Por favor, escolha uma opção válida.")
            
            if opcao != "0":
                input("\n⏎ Pressione ENTER para continuar...")
                
        except KeyboardInterrupt:
            print("\n\n👋 Sistema encerrado pelo usuário.")
            break
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")
            input("⏎ Pressione ENTER para continuar...")

# Executa o sistema
if __name__ == "__main__":
    main()