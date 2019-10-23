class AdapterTypes():
    control = "CONTROL"
    display = "DISPLAY"

class AdapterManager():
    def __init__(self):
        # Initialize the adapter list
        self._adapters = []

    def add(self, adapter):
        # Check if an adapter has already been initialized
        if len(self._adapters) > 0:
            # Check if an incompatible adapter type is added
            if adapter.ADAPTER_TYPE != self._adapters[0]["type"]:
                raise TypeError("Adapter type mismatch.")

        self._adapters.append({
            "title": adapter.ADAPTER_TITLE,
            "type": adapter.ADAPTER_TYPE,
            "cls": adapter()
        })

    def flush(self):
        self._adapters = []

    def call(self, *args, **kwargs):
        for adapter_count, adapter in enumerate(self._adapters, 1):
            try:
                return adapter["cls"].call(args, kwargs)
            except Exception as e:
                # If all adapters have been exhausted and raised an error,
                # raise the last adapter's error.
                if adapter_count >= len(self._adapters):
                    raise e
