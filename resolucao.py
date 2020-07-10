import json

def lerArquivo():
    try:
        with open('broken-database.json', 'r', encoding='utf8') as f:
            return json.load(f)
    except NameError:
        print(NameError)




def corrigirNome(banco):
    try:
        for n in banco:
            n["name"] = n["name"].replace('\u00DF', 'b')
            n["name"] = n["name"].replace('\u00F8', 'o')
            n["name"] = n["name"].replace('\u00E6', 'a')
            n["name"] = n["name"].replace('\u00A2', 'c')
    except NameError:
        print(NameError)

def corrigirPreco(banco):
    try:
        for n in banco:
            if type(n["price"]) == type("") :
                n["price"] = float(n["price"])
    except NameError:
        print(NameError)

def corrigirQuantidade(banco) :
    try:
        for n in banco:
            if "quantity" not in n.keys() :
                n["quantity"] = 0
    except NameError:
        print(NameError)

def exportarArquivo(banco):
    try:
        with open('saida.json', 'w', encoding='utf8') as f:
            json.dump(banco, f, ensure_ascii=False , indent=4, separators=(',',':'))
    except NameError:
        print(NameError)

def imprimeNome(banco):
    try:
        banco.sort(key=lambda n: (n['category'], n['id']))
        try:
            lista = []
            for n in banco :
                lista.append(n["name"])
            print('Lista de Produtos: ',lista)
        except NameError:
            print( NameError)
    except NameError:
        print(NameError)

def calculaEstoque(banco):
    try:
        estoque = [
            {
                'category' : 'Acessórios',
                'valor' : 0
            },{
                'category' : 'Eletrodomésticos',
                'valor' : 0
            },{
                'category' : 'Eletrônicos',
                'valor' : 0
            },{
                'category' : 'Panelas',
                'valor' : 0
            }
        ]
        for n in banco:
            for e in estoque:
                if n["category"] == e["category"] :
                    e["valor"] = e["valor"] + (n["price"] *n["quantity"])
        return estoque
    except NameError:
        print(NameError)


banco = lerArquivo()
corrigirNome(banco)
corrigirPreco(banco)
corrigirQuantidade(banco)
imprimeNome(banco)
print(calculaEstoque(banco))
exportarArquivo(banco)


