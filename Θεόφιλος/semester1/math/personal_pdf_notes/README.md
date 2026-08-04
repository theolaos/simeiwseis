User Settings `.json` for VScodium LaTeX Workshop with whole TEX-live environment installed (μάλλον δεν θα χρειαστείς όλα τα πακέτα).

```json
    "latex-workshop.latex.tools": [
        {
            "name": "xelatex",
            "command": "xelatex",
            "args": [
                "-synctex=1",
                "-interaction=nonstopmode",
                "-file-line-error",
                "%DOC%"
            ],
            "env": {}
        }
    ],
    "latex-workshop.latex.recipes": [
        {
            "name": "xelatex",
            "tools": [
                "xelatex"
            ]
        },
        {
            "name": "xelatex -> xelatex",
            "tools": [
                "xelatex",
                "xelatex"
            ]
        }
    ],
    "latex-workshop.latex.recipe.default": "first"
```