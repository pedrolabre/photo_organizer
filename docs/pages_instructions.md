# Publicar `version1_documentation.html` como GitHub Pages

Siga estes passos para servir o arquivo `docs/version1_documentation.html` como uma página do GitHub Pages.

1. Confirme que o arquivo existe em `docs/version1_documentation.html`.
2. Já adicionamos um `index.html` em `docs/` que redireciona para o arquivo.
3. Faça commit e push das alterações locais:

```bash
git add docs/index.html docs/pages_instructions.md
git commit -m "Add GitHub Pages index redirect for documentation"
git push origin main
```

4. No GitHub (repositório https://github.com/pedrolabre/photo_organizer):
   - Vá em _Settings → Pages_.
   - Em _Source_, escolha a branch `main` e a pasta `/docs`.
   - Salve.

5. A página estará disponível em:

```
https://pedrolabre.github.io/photo_organizer/version1_documentation.html
```

Se preferir publicar automaticamente numa branch `gh-pages`, posso adicionar uma GitHub Action para isso—quer que eu crie? 
