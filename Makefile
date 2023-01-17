.ONESHELL:

py := poetry run
python := $(py) python

package_dir := src
tests_dir := tests

code_dir := $(package_dir) $(tests_dir)


define setup_env
    $(eval ENV_FILE := $(1))
    @echo " - setup env $(ENV_FILE)"
    $(eval include $(1))
    $(eval export)
endef

.PHONY: reformat
reformat:
	$(py) black $(code_dir)
	$(py) isort $(code_dir) --profile black --filter-files
	find -name "*.py" | xargs add-trailing-comma --py36-plus;
	$(py) black $(code_dir)

.PHONY: go-to-db
go-to-db:
	docker compose -f=docker-compose-dev.yml --env-file=.env exec db \
	psql --username=testuser --dbname=testdatabase 


.PHONY: dev-bot
dev-bot:
	$(call setup_env, .env)
	python -m src.tgbot 

.PHONY: dev-docker
dev-docker:
	docker compose -f=docker-compose-dev.yml --env-file=.env.dev up


.PHONY: generate-typings
generate-typings:
	i18n -ftl src/tgbot/locales/uk-UA/main.ftl -stub typings/fluentogram_stubs.pyi

.PHONY: tests
tests:
	$(call setup_env, .env.test)
	$(py) pytest $(tests_dir) --tb=long 
