novo_arquivo = open('pagina_atualizada.html', 'w', encoding='utf-8')

novo_arquivo.write('''
<DOCTYPE HTML>
<html lang="pt-BR">
<head>
    <meta charset="utf-8">
    <title>Nova Página</title>
    <style>
    body{
        color: red;
        background-color: grey;
    }
    #imagens-site{
        display: flex;
    }
    #imagens-iguais{
        padding: 20px;
    }
    #titulo-pagina{
        display: flex;
        justify-content: center;
        padding-top: 2%;
        height: 10%;
    }
    button{
        background-color: grey;
        border: solid black 2px;
        border-radius: 20px;
        padding: 5px 50px;
        transition: 0.3s;
    }
    button:hover{
        transition: 0.3s;
        color: white;
        background-color: orange;
        border-color: orange;
        padding: 10px 60px;
    }
    img{
        border: solid black 3px;
        border-radius: 10px;
        margin: 20px;
        transition: transform 0.5s ease;
    }
    img:hover{
        transform: translateY(-10px);
    }
    </style>
</head>
<body>
    <div id="titulo-pagina">
        <div>
            <button>Botão</button>
        </div>
    </div>
    <div id="imagens-site">
        <div>
            <img src="teste.png"/>
        </div>
        <div id="imagens-iguais">
            <div>
                <img src="teste2.jpg"/>
            </div>
            <div>
                <img src="teste2.jpg"/>
            </div>
        </div>
    </div>
</body>
</html>
''')

novo_arquivo.close()
