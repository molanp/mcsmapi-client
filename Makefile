.PHONY: docs

docs:
    @echo "Generating API documentation..."
    sphinx-apidoc -o docs/source/api/ mcsmapi/ -f
    @echo "Building Chinese docs..."
    sphinx-build -b html -D language=zh_CN docs/source/ docs/build/zh_CN/
    @echo "Building English docs..."
    sphinx-build -b html -D language=en docs/source/ docs/build/en/
    @echo "Documentation generated in docs/build/"