# Makefile

DOMAINS_FILE = domains.txt
GIT_MSG = "update"
EDITOR ?= nano  # Можно заменить на vim, code, или любой другой

.PHONY: edit push

# Обновление репозитория и открытие редактора
edit:
	git pull
	$(EDITOR) $(DOMAINS_FILE)
	git add $(DOMAINS_FILE)
	git commit -m "$(GIT_MSG)"
	git push
