from datetime import datetime

class ItemsViewModel:

    def __init__(self, items):
        self._items = items
        #self._status = status

    @property
    def items(self):
        return self._items
    

    def get_item_done(self, filter_period):
        filteredItems = []
        todaysDate = datetime.today().date()
        DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%fZ'

        if filter_period == "today":
            for x in self._items:
                if x['status'] == "Done":
                    itemLastActivityDate = datetime.strptime(x['dateLastActivity'],DATETIME_FORMAT).date()
                    if itemLastActivityDate == todaysDate:
                        filteredItems.append(x)
            self._items = filteredItems
        elif filter_period == "all":
            for x in self._items:
                if x['status'] == "Done":
                    filteredItems.append(x)
            self._items = filteredItems
        elif filter_period == "older":
            for x in self._items:
                if x['status'] == "Done":
                    itemLastActivityDate = datetime.strptime(x['dateLastActivity'],DATETIME_FORMAT).date()
                    if itemLastActivityDate < todaysDate:
                        filteredItems.append(x)
            self._items = filteredItems

        return self._items
    
    def get_item_thingstodo(self):
        filteredItems = []
        for x in self._items:
            if x['status'] == "Things To Do":
                filteredItems.append(x)
        self._items = filteredItems
        return self._items
    
    def get_item_doing(self):
        filteredItems = []
        for x in self._items:
            if x['status'] == "Doing":
                filteredItems.append(x)
        self._items = filteredItems
        return self._items

    def show_all_done_items(self): 
        #which will keep track of if we should show all the completed items, or just the most recent ones.
        allDoneItems = []
        allDoneItems = self.get_item_done("all")
        return allDoneItems
        
    def recent_done_items(self): 
        #which will return all the tasks that have been completed today.
        todayDoneItems = []
        todayDoneItems = self.get_item_done("today")
        return todayDoneItems

    def older_done_items(self): 
        #which will return all of the tasks that were completed before today.
        olderDoneItems = []
        olderDoneItems = self.get_item_done("older")
        return olderDoneItems