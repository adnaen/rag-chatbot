scrap:
	PYTHONPATH=. python scripts/scrap_data.py

index:
	PYTHONPATH=. python scripts/indexing.py

download-model:

	PYTHONPATH=. python scripts/download_model.py

run:
	PYTHONPATH=./src uvicorn main:app --reload --host localhost --port 8000
