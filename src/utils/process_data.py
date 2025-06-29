from pathlib import Path
from src.config import logger, Settings
from src.utils.file_utils import _load_json
from src.utils.data_utils import _generate_chunks
from src.utils.state_utils import mark_completed


def process_data():
    GLOBAL_METADATA_PATH = Settings.DATA_DIR / "raw" / "metadata.json"
    content = _load_json(GLOBAL_METADATA_PATH)
    for item in content:
        sub_metadata = _load_json(Path(item["stored_path"]) / "metadata.json")
        for each in sub_metadata:
            _generate_chunks(
                processed_path=each["processed_path"],
                file_name=each["file_name"],
                category=item["category"],
            )
        logger.info(f"Successfully generate chunks on {item['category']} data.")

    mark_completed("data_preprocessing")
