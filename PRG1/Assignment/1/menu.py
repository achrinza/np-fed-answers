class Menu:
    def __init__(self):
        pass

    def render(self, menu):
        """Renders and returns a string of the rendered menu.

        Arguments:

        menu --> The menu object.

        Example menu object:

        {
            "meta": {
                "title": ""
            },
            "sections": [
                "meta": {
                    "title": ""
                },
                "items": [
                    {
                        "meta": {
                            "title": "Item title",
                            "key": "Item key"
                        }
                    }
                ]
            ]
        }
        """
        # Get the menu title.
        try:
            menu_title = menu["meta"]["title"]
        except KeyError:
            # If menu title not found, set to a default title.
            menu_title = "??????????"

        render = "\n" + menu_title
        render += "\n" + "=" * len(menu_title) + "\n"

        # Loop through each section
        item_count_offset = 1
        for section in menu["sections"]:
            try:
                section_title = section["meta"]["title"]
            except KeyError:
                section_title = ""

            if section_title != "":
                render += f"{section_title}\n"
                render += "-" * len(section_title) + "\n"

            for item in section["items"]:
                try:
                    item_key = item["meta"]["key"]
                except KeyError:
                    item_key = item_count_offset
                    item_count_offset += 1

                item_title = item["meta"]["title"]

                render += f"[{item_key}] {item_title}\n"

            render += "\n"

        return render
