run:
	@echo "Change directory to '$(SERVICE)' and run '$(SERVICE)' on '$(PORT)'."
	cd $(SERVICE) && uvicorn $(SERVICE).main:app --host 0.0.0.0 --reload --port=$(PORT)

install:
	@echo "Change directory to '$(SERVICE)' and install '$(LIBRARY)'."
	poetry add $(LIBRARY)

update:
	@echo "Change directory to '$(SERVICE)' and update dependencies."
	poetry update

delete:
	@echo "Change directory to '$(SERVICE)' and delete '$(LIBRARY)'."
	poetry remove $(LIBRARY)

commit:
	@echo "Change directory to '$(SERVICE)' and create commit."
	cd $(SERVICE) && alembic revision --autogenerate -m "$(COMMIT)"

upgrade:
	@echo "Change directory to '$(SERVICE)' and run upgrade."
	cd $(SERVICE) && alembic upgrade head
