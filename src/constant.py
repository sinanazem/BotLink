from types import SimpleNamespace
from src.keyboard import create_keyboard


keys = SimpleNamespace(
    add='Add Link',
    get='Get Link'
)

keyboards = SimpleNamespace(
    main = create_keyboard(keys.add,keys.get)
)