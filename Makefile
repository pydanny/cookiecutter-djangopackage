bake:
	cookiecutter --no-input . --overwrite-if-exists

watch: bake
	watchmedo shell-command -p '*.*' -c 'make bake' -W -R -D \{{cookiecutter.repo_name}}/
