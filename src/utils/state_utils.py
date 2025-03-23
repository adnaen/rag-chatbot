import pickle
import os
from typing import Any
from src.config import paths

STATE_FILE = paths.CONFIG_DIR / "state.pkl"

default_state = {"data_ingestion": False, "data_preprocessing": False}


def _init_state() -> None:
    with open(STATE_FILE, "wb") as file:
        pickle.dump(default_state, file)


def _load_state() -> Any:
    if not os.path.exists(STATE_FILE):
        _init_state()
    with open(STATE_FILE, "rb") as file:
        return pickle.load(file)


def _save_state(state) -> None:
    if not os.path.exists(STATE_FILE):
        _init_state()
    with open(STATE_FILE, "wb") as file:
        pickle.dump(state, file)


def is_completed(task: str) -> bool:
    state = _load_state()
    return True if state.get(task, False) else False


def mark_completed(task: str) -> None:
    state = _load_state()
    state[task] = True
    _save_state(state)
