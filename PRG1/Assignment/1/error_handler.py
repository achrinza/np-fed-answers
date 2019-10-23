from di_container import DIContainerKeys, inject
from adapter_manager import AdapterManager, AdapterTypes
from display_adapter import DisplayAdapterCalls

class ErrorHandler:
    def __init__(self):
        self.display_manager = inject(DIContainerKeys.display_manager, AdapterManager)

    def new_error(self, error, errorPretty = "See FULL ERROR below."):
        error_msg = f"ERROR ====================\n{errorPretty}"
        if error != "":
            error_msg += f"\nFULL ERROR ==========\n{error}"
                
        error_msg += "\n=========================="
        return self.display_manager.call(DisplayAdapterCalls.show_text, error_msg)
