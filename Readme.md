# Todo Tasks - API - DRF

Uma API criada em DRF com uso de generics data para criaçao de dados.



## Referência

 - [Documentação DRF](https://www.django-rest-framework.org/)





## 🚀 Sobre mim

Sou um desenvolvedor com 4 anos de carreira, passando por grandes empresas como Stefanini e Magna Sistemas. Atuando para clientes como : Banco do Brasil e Prodesp.

Sempre gostei do foco maior no "coração" do sistema e trabalhar com Backend me proporciona isto. Amo trabalhar com Python por conta de sua simplicidade e velocidade de leitura de dados.

Ao criar qualquer ferramenta como esta API que vocês verão o funcionamento, sempre penso em 3 pilares : Desempenho, facilidade de codificação e escalibilidade.
Então ao ver essa API você poderá notar que esse foco foi dado!


## Escolhas no projeto

Ao você ver o projeto, verá que ele foi feito do método mais simples possível. Confiando 101% no framework. O motivo disto foi me dado o tempo para codificação. Tive menos de 24 horas para construir uma API totalmente funcional e com recursos de pesquisa textual, além de ordenação. 

Então antes de tentar fazer um projeto do qual poderia dar problemas ou funcionar incorretamente, optei por confiar nos recursos genéricos da próprio Framework. Fazendo tudo que foi possível para extrair o máximo do DRF e consumo da API. Abaixo você poderá ler todas as rotas e funções.


## Documentação da API

#### Retorna todos os itens

```http
  GET /api
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `none` | `-` | Retorna todos os itens |

#### Retorna um item

```http
  GET /api/${id}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `id` | **Obrigatório**. O ID do item que você quer |

#### Cria um item
```http
  POST /api/create
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `string` | **Obrigatório**. Gerado automáticamente |
| `Task name`      | `string` | **Obrigatório**. Nome da Task. |
| `Descriptions`      | `string` | **Obrigatório**. Descricao da Task.|
| `Done`      | `boolean` | Validar de a tarefa foi concluída. |

#### Atualiza um item
```http
  PUT /api/update/${id}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `string` | **Obrigatório**. Gerado automáticamente |
| `Task name`      | `string` | **Obrigatório**. Nome da Task. |
| `Descriptions`      | `string` | **Obrigatório**. Descricao da Task.|
| `Done`      | `boolean` | Validar de a tarefa foi concluída. |

#### Deleta um item
```http
  DELETE /api/delete/${id}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `string` | **Obrigatório**. Necessário para informar qual item deverá ser deletado. |




## Funcionalidades

- Procurar uma tarefa via texto.
- Ordenação por data de escrita, sendo por ordem crescente ou decrescente.


## Funcionalidades - Procurar tasks via Texto.


```http
  GET /api/?search={var}
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `var` | `string` | Argumento variável de pesquisa. |

Para usar essa ferramenta você precisa acessar a home da api. http://127.0.0.1:8000/api/

Funcao que busca o seu texto para tentar encontrar um título igual ao que você digitou.

Aqui você pode ver como ela funciona https://www.django-rest-framework.org/api-guide/filtering/ , porém podemos resumir a função em dois passos. o primeiro ela colhe o que você escrever e segundo tenta fazer um parsing nos objetos. Além disso, ela cria uma rota por padrão ou seja, pode ser consumido facilmente pelo front end.

## Funcionalidades - Ordenação por data de escrita, sendo por ordem crescente ou decrescente.
```http
  GET /api/?ordering={var}
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `Updated` | `string` | Argumento variável de ordenação |
| `-Updated` | `string` | Argumento variável de ordenação |


Para usar essa ferramenta você precisa acessar a home da api. http://127.0.0.1:8000/api/

Aqui vamos fazer o processo de ordenação, voce pode ler a referencia aqui:https://www.django-rest-framework.org/api-guide/filtering/ 

Essa função gera ordenação de forma automática e gera também url que pode ser consumida por um frontend.


## Instalação do Projeto

Primeiro comando para Instalação de itens necessários.
```bash
  pip install -r requeriments.txt
  
```


Agora crie um banco de dados no PgAdmin abrindo: 
- Nome do banco: **TaskList**
- User: **postgres**
- Password: **123**
- Host: **127.0.0.1**
- PORT: **5432**

*obs: Nos settings do projeto voce pode alterar as consultas.*



Vá até a raiz do projeto e execute: 
```bash
  python manage.py createsuperuser
  
```

Após criar um super usuário, execute o comando de migração.

Vá até a raiz do projeto e execute: 
```bash
  python manage.py makemigrations
  
```
Agora inicie com o comando de migração.

Vá até a raiz do projeto e execute: 
```bash
  python manage.py migrate
  
```

Inicie o servidor com : 
```bash
  python manage.py runserver
  
```

Acesse: 
http://127.0.0.1:8000/api/
## Melhorias

Se eu tivesse um pouco mais tempo, queria fazer itens como Handlers e trativas de erros mais personalizadas. 

Gostaria de fazer uma melhoria geral no código com itens personalizados, pesquisas melhores.

Eu queria muito ter incluído o Docker, porém devido a falta de tempo nao consegui implementar de uma forma funcional e
100% confiável.


## Stack utilizada

**Back-end:** Python, Django Rest
