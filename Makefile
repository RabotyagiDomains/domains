DOMAINS_FILE = domains.txt
GIT_MSG ?= update
EDITOR ?= nano

.PHONY: edit push

push:
	python convert.py
	git add .
	git commit -m "$(GIT_MSG)" || true
	git push

edit:
	git pull
	$(EDITOR) $(DOMAINS_FILE)
	$(MAKE) push