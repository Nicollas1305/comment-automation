# Instagram auto comment Bot

Este projeto é um bot automatizado que utiliza **Selenium** para realizar comentários em publicações do Instagram. Ele faz login em uma conta, acessa uma publicação específica e comenta mencionando seguidores definidos em um arquivo JSON.

## ⚙️ Funcionalidades

- Login automatizado no Instagram.
- Comentários em publicações específicas.
- Mapeamento de seguidores a partir de um arquivo JSON.
- Suporte a múltiplos comentários sequenciais.

---

## 📂 Estrutura do Projeto

```plaintext
.
├── followers.json    # Arquivo contendo a lista de seguidores (detalhado abaixo)
├── main.py           # Script principal com a automação
├── chromedriver      # Driver do Chrome para Selenium
├── README.md         # Documentação do projeto
```

---

## 📋 Pré-requisitos

- **Python 3.9+**
- **Google Chrome** instalado.
- **Chrome Driver compatível** instalado.
- **Selenium**:
  Instale utilizando o comando:
  ```bash
  pip install selenium
  ```

- **ChromeDriver**:
  Faça o download da versão correspondente ao seu navegador [aqui](https://googlechromelabs.github.io/chrome-for-testing/) e atualize o caminho no script.

---

## 💧 Configuração do Arquivo `followers.json`

O arquivo `followers.json` deve conter uma lista de objetos no formato abaixo:

```json
[
  {
    "string_list_data": [
      {
        "value": "username1"
      }
    ]
  },
  {
    "string_list_data": [
      {
        "value": "username2"
      }
    ]
  },
  {
    "string_list_data": [
      {
        "value": "username3"
      }
    ]
  }
]
```

### Detalhes:
- Cada seguidor é representado como um objeto com a chave `string_list_data`.
- A chave `value` dentro de `string_list_data` contém o nome de usuário (`username`) que será mencionado nos comentários.

---

## 🚀 Como Usar

1. **Configurar Credenciais**:
   - Abra o arquivo `main.py` e substitua:
     ```python
     username_input.send_keys("SEU_USUARIO")
     password_input.send_keys("SUA_SENHA")
     ```

2. **Configurar URL do Post**:
   - Substitua `post_url` no script pelo link da publicação onde os comentários serão feitos:
     ```python
     post_url = "https://www.instagram.com/p/EXEMPLO/"
     ```

3. **Executar o Script**:
   Execute o script com o seguinte comando:
   ```bash
   python main.py~~~~
   ```

4. **Comentários Automáticos**:
   O bot fará login na conta, navegará para a publicação e realizará os comentários utilizando os dados do arquivo `followers.json`.

---

## ⚠️ Observações

- **Segurança**: Nunca compartilhe suas credenciais. Use variáveis de ambiente ou bibliotecas como `python-decouple` para armazenar credenciais de forma segura.
- **Bloqueios do Instagram**: Use intervalos maiores entre comentários (`time.sleep`) para evitar ser sinalizado pelo Instagram.
- **Manter a Sessão Ativa**: Para evitar fazer login a cada execução, use o armazenamento de cookies (detalhes explicados abaixo).

---

## 🧠 Melhorias Futuras

- Implementar o armazenamento de cookies para manter a sessão ativa.
- Adicionar logs mais detalhados.
- Integrar com APIs do Instagram para substituir Selenium onde possível.
- Adicionar interface gráfica para configurar os dados do bot.

---

Se precisar de mais informações, fique à vontade para entrar em contato!

