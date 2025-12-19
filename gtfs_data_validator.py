class GTFSDataValidator:
  def __init__(self):
    pass
    
  # remove duplicates
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
    dfs["agency"].drop_duplicates(inplace=True)
    dfs["stop_amenities"].drop_duplicates(inplace=True)

  # handle missing values
  def handle_missing_values(self, dfs: dict):
    dfs["routes"].fillna("Unknown", inplace=True)
    dfs["trips"].drpona(subset=["trip_headsign"], inplace=True)
    dfs["trips"].fillna({"trip_short_name":"Unknown", "trip_short_name":"Unknown", "direction_id":"Unknown", "block_id":"Unknown", "shape_id":"Unknown", "wheelchair_accessible":"Unknown", "bikes_allowed":"Unknown", "route_variant":"Unknown"}, inplace=True)
    dfs["stops"].dropna(subset=["stop_lat", "stop_lon"], inplace=True)
    dfs["stop_times"].dropna(subset=["arrival_time", "departure_time", "stop_id", "stop_sequence", "pickup_type", "drop_off_type", "stop_headsign"], inplace=True)
    dfs["calendar_dates"].dropna(subset=["date", "exception_type"], inplace=True)
    dfs["shapes"].dropna(subset=["shape_pt_lat", "shape_pt_lon", "shapre_pt_sequence"], inplace=True)
    dfs["transfers"].fillna("Unknown", inplace=True)
    dfs["feed_info"].fillna("Unknown", inplace=True)
    dfs["fare_rules"].fillna("Unknown", inplace=True)
    dfs["fare_attributes"].dropna(subset=["price", "transfers"], inplace=True)
    dfs["fare_attributes"].fillna({"currency_type":"Unknown", "payment_method":"Unknown"}, inplace=True)
    dfs["agency"].fillna("Unknown", inplace=True)
    dfs["stop_amenities"].dropna(subset=["shelter", "washroom", "bike_rack", "bench"], inplace=True)

  # find and summarize duplicates
  def duplicates_summary(self, dfs: dict):
    duplicates_summary = {name: df.duplicated().sum() for name, df in dfs.items()}
    return duplicates_summary

  # find and summarize missing values
  def missing_values_summary(self, dfs: dict):
    missing_values = {name: df.isnull().sum() for name, df in dfs.items()}
    return missing_values

  def validate(self, dfs: dict):
    self.remove_duplicates(dfs)
    self.handle_missing_values(dfs)
    return dfs
