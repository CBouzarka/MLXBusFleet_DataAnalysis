class GTFSDataValidator:
  def __init__(self):
    pass
    
  def remove_duplicates(self, dfs: dict):
    dfs["routes"].drop_duplicates(inplace=True)
    dfs["trips"].drop_duplicates(inplace=True)
    dfs["stops"].drop_duplicates(inplace=True)
    dfs["stop_times"].drop_duplicates(inplace=True)
    dfs["calendar_dates"].drop_duplicates(inplace=True)
    dfs["shapes"].drop_duplicates(inplace=True)
    dfs["transfers"].drop_duplicates(inplace=True)
    dfs["feed_info"].drop_duplicates(inplace=True)
    dfs["fare_rules"].drop_duplicates(inplace=True)
    dfs["fare_attributes"].drop_duplicates(inplace=True)
    dfs["agencies"].drop_duplicates(inplace=True)
    dfs["stop_amenities"].drop_duplicates(inplace=True)
