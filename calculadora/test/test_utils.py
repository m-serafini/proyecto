import pytest
from calculadora.utils import solicitar_numero, pedir_opcion

def test_solicitar_numero_valido(monkeypatch, inputs_validos_numero):
    # Simulamos que el usuario escribe "10.5"
    respuestas = iter(inputs_validos_numero)
    monkeypatch.setattr('builtins.input', lambda _: next(respuestas))
    
    resultado = solicitar_numero("primer")
    assert resultado == 10.5

def test_solicitar_numero_reintento(monkeypatch, inputs_invalidos_numero):
    # Simulamos: primero error, luego acierto. 
    # El loop 'while True' de tu función manejará el primer error y retornará el segundo.
    respuestas = iter(inputs_invalidos_numero)
    monkeypatch.setattr('builtins.input', lambda _: next(respuestas))
    
    resultado = solicitar_numero("segundo")
    assert resultado == 5.0

def test_pedir_opcion_valida(monkeypatch, opcion_correcta):
    monkeypatch.setattr('builtins.input', lambda _: opcion_correcta[0])
    
    resultado = pedir_opcion()
    assert resultado == "1"

def test_pedir_opcion_invalida(monkeypatch, opcion_incorrecta):
    monkeypatch.setattr('builtins.input', lambda _: opcion_incorrecta[0])
    
    resultado = pedir_opcion()
    assert resultado == "9"