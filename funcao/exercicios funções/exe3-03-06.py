traducao =  {
    'hello': 'hola',
    'good morning' : 'buen día',
    'ate logo' : 'comío logotipo',
    'have a good trip' : 'ten un ben veiaje', 
}

palavra_ingles = input("digite uma palavra em ingles: ").strip().lower()

palavra_espahol = traducao.get(palavra_ingles, "palavra não encontrada")
print(f"a palavra {palavra_ingles} em espanhol é: {palavra_espahol}")