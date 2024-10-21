# -*- coding: utf-8 -*-
import re

def luhn_check(card_number):
    """Valida o número do cartão usando o algoritmo de Luhn."""
    total = 0
    reverse_digits = card_number[::-1]
    for i, digit in enumerate(reverse_digits):
        n = int(digit)
        if i % 2 == 1:  # Dobre cada segundo dígito
            n *= 2
            if n > 9:  # Se o resultado for maior que 9, subtraia 9
                n -= 9
        total += n
    return total % 10 == 0

def validar_cartao(numero_cartao):
    """
    Valida um número de cartão e descobre o tipo de cartão.
    
    Args:
        numero_cartao (str): Número do cartão.
    
    Returns:
        dict: Dicionário com informações sobre o cartão.
    """
    
    # Remover espaços e hífen do número do cartão
    numero_cartao = re.sub(r'\D', '', numero_cartao)
    
    # Verificar o comprimento do número do cartão
    if len(numero_cartao) not in (13, 15, 16):
        return {"erro": "Número do cartão inválido"}
    
    # Verificar se o número do cartão é válido usando o Luhn
    if not luhn_check(numero_cartao):
        return {"erro": "Número do cartão inválido (Luhn check falhou)"}
    
    # Descobrir o tipo de cartão
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
    """Valida o CVV de acordo com o tipo do cartão."""
    if tipo_cartao == "Mastercard":
        return len(cvv) == 3 and cvv.isdigit()
    # Adicione outras validações de CVV para diferentes tipos de cartão, se necessário
    return False

def verificar_cvv_com_numero_cartao():
    """Função principal para verificar o CVV baseado no número do cartão."""
    numero_cartao = input("Digite o número do cartão: ")
    
    # Validar o cartão
    resultado = validar_cartao(numero_cartao)
    if "erro" in resultado:
        print(resultado["erro"])
        return
    
    tipo_cartao = resultado["tipo_cartao"]
    print(f"Tipo de cartão detectado: {tipo_cartao}")
    
    cvv = input("Digite o CVV do cartão: ")
    
    if validar_cvv(cvv, tipo_cartao):
        print("CVV válido.")
    else:
        print("CVV inválido. O CVV deve ter exatamente 3 dígitos para Mastercard.")

# Executar a função de verificação de CVV com número do cartão
verificar_cvv_com_numero_cartao()