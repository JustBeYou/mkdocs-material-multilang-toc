from mkdocs.plugins import BasePlugin
from mkdocs.structure.nav import Section

LANGUAGES = ['zh', 'en']
LANGUAGES_DIR = {l + '/': l for l in LANGUAGES}

class Plugin(BasePlugin):
    config_scheme = ()
    saved_nav_items = None

    def on_page_context(self, context, page, config, nav):
        if self.saved_nav_items == None:
            self.saved_nav_items = nav.items.copy()

        curr_lang = next((v for k, v in LANGUAGES_DIR.items()
                if page.file.url.startswith(k)),None)
        if curr_lang == None:
            return context

        section = next((item for item in self.saved_nav_items
                if isinstance(item, Section) and item.title.lower() == curr_lang), None)
        if section == None:
            raise Exception(f"[mkdocs-material-multilang-toc] No ToC section for language {curr_lang}")

        new_toc = [item for item in self.saved_nav_items if not isinstance(item, Section)] + section.children
        nav.items = new_toc

        return context
