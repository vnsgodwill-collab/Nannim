# Exporting the UML diagram (inheritance_uml.puml)

This repository contains `inheritance_uml.puml` (PlantUML source) in the repository root.

Options to export the PNG (`inheritance_uml.png`):

1) Locally with PlantUML installed

- If `plantuml` CLI is installed:

  plantuml -tpng inheritance_uml.puml

- Or with the JAR:

  java -jar plantuml.jar inheritance_uml.puml

2) Using Docker

- Requires Docker installed locally:

  docker run --rm -v "$PWD":/workspace plantuml/plantuml -tpng inheritance_uml.puml

3) Using the included GitHub Actions workflow (recommended for CI)

- The workflow `.github/workflows/generate-uml.yml` will run on push (when `inheritance_uml.puml` changes) and on manual dispatch. It generates `inheritance_uml.png` and commits it back to the repository automatically.

Notes
- The workflow uses a Docker image to render PlantUML, so no local setup is required if you prefer CI to produce the PNG.
- Once the workflow completes, the generated `inheritance_uml.png` will appear at the repository root.
