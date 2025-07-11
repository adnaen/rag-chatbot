scrap:
	PYTHONPATH=./api python scripts/scrap_data.py

index:
	PYTHONPATH=./api python scripts/indexing.py

download-model:

	PYTHONPATH=./api python scripts/download_model.py

run:
	PYTHONPATH=./api uvicorn src.main:app --reload --host localhost --port 8000
