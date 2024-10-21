# -*- coding: utf-8 -*-
import re

def luhn_check(card_number):
    """Valida o n�mero do cart�o usando o algoritmo de Luhn."""
    total = 0
    reverse_digits = card_number[::-1]
    for i, digit in enumerate(reverse_digits):
        n = int(digit)
        if i % 2 == 1:  # Dobre cada segundo d�gito
            n *= 2
            if n > 9:  # Se o resultado for maior que 9, subtraia 9
                n -= 9
        total += n
    return total % 10 == 0

def validar_cartao(numero_cartao):
    """
    Valida um n�mero de cart�o e descobre o tipo de cart�o.
    
    Args:
        numero_cartao (str): N�mero do cart�o.
    
    Returns:
        dict: Dicion�rio com informa��es sobre o cart�o.
    """
    
    # Remover espa�os e h�fen do n�mero do cart�o
    numero_cartao = re.sub(r'\D', '', numero_cartao)
    
    # Verificar o comprimento do n�mero do cart�o
    if len(numero_cartao) not in (13, 15, 16):
        return {"erro": "N�mero do cart�o inv�lido"}
    
    # Verificar se o n�mero do cart�o � v�lido usando o Luhn
    if not luhn_check(numero_cartao):
        return {"erro": "N�mero do cart�o inv�lido (Luhn check falhou)"}
    
    # Descobrir o tipo de cart�o
    tipo_cartao = ""
    if numero_cartao.startswith(("34", "37")):
        tipo_cartao = "American Express"
    elif numero_cartao.startswith(("6011", "65")):
        tipo_cartao = "Discover"
    elif numero_cartao.startswith(("5018", "5020", "5038", "6304")):
        tipo_cartao = "Maestro"
    elif numero_cartao.startswith(("51", "52", "53", "54", "55")):
        tipo_cartao = "Mastercard"
    elif numero_cartao.startswith(("4",)):
        tipo_cartao = "Visa"
    
    return {
        "tipo_cartao": tipo_cartao,
        "numero_cartao": numero_cartao
    }

def validar_cvv(cvv, tipo_cartao):
    """Valida o CVV de acordo com o tipo do cart�o."""
    if tipo_cartao == "Mastercard":
        return len(cvv) == 3 and cvv.isdigit()
    # Adicione outras valida��es de CVV para diferentes tipos de cart�o, se necess�rio
    return False

def verificar_cvv_com_numero_cartao():
    """Fun��o principal para verificar o CVV baseado no n�mero do cart�o."""
    numero_cartao = input("Digite o n�mero do cart�o: ")
    
    # Validar o cart�o
    resultado = validar_cartao(numero_cartao)
    if "erro" in resultado:
        print(resultado["erro"])
        return
    
    tipo_cartao = resultado["tipo_cartao"]
    print(f"Tipo de cart�o detectado: {tipo_cartao}")
    
    cvv = input("Digite o CVV do cart�o: ")
    
    if validar_cvv(cvv, tipo_cartao):
        print("CVV v�lido.")
    else:
        print("CVV inv�lido. O CVV deve ter exatamente 3 d�gitos para Mastercard.")

# Executar a fun��o de verifica��o de CVV com n�mero do cart�o
verificar_cvv_com_numero_cartao()