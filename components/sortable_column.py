# Thanks itworkedlastime for this component!
# https://github.com/itworkedlastime/nicegui-sortable-column

from typing import Callable, Optional
from nicegui import ui
from backend import paths
import os

sortable_column_js = os.path.join(paths.components_dir, "sortable_column.js")
class SortableColumn(ui.element, component=sortable_column_js):
    sortable_list = {}
    def __init__(self, *, on_change: Optional[Callable] = None, group: str = None) -> None:
        super().__init__()
        self.on('item-drop', self.drop)
        self.on_change = on_change

        self._classes.append('nicegui-column')
        self._props['group'] = group
        SortableColumn.sortable_list[self.id] = self

    def drop(self, e) -> None:
        if self.on_change:
            self.on_change(
                e.args['new_index'], e.args['old_index'],
                #SortableColumn.sortable_list.get(e.args['new_list']),
                #SortableColumn.sortable_list.get(e.args['old_list']),
            )
        else:
            print(e.args)

    def makeSortable(self) -> None:
        self.run_method('makeSortable')

    def enable_dragging(self, enable: bool) -> None:
        self.run_method('toggleSortable', enable)