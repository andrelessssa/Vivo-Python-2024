import functools

def duplicar(func):
    @functools.wraps(func)
    def envelope(*args, **kwargs):
        resultado = func(*args, **kwargs)
        return resultado, resultado
    
    return envelope

@duplicar
def aprender(tecnologia):
    print(f"Aprendendo {tecnologia}")
    return tecnologia.upper()

tecnologia, tecnologia_duplicada = aprender("Python")
print(tecnologia)
print(tecnologia_duplicada)