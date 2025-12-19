import pandas as pd

class GTFSLoader:
    def __init__(self, path: str):
        self.path = path

    # load data into dataframes
    def _load_from_folder(self):
        return {
            "routes": pd.read_csv(f"{self.path}/routes.txt"),
            "trips": pd.read_csv(f"{self.path}/trips.txt"),
            "stops": pd.read_csv(f"{self.path}/stops.txt"),
            "stop_times": pd.read_csv(f"{self.path}/stop_times.txt"),
            "calendar_dates": pd.read_csv(f"{self.path}/calendar_dates.txt"),
            "shapes": pd.read_csv(f"{self.path}/shapes.txt"),
            "transfers": pd.read_csv(f"{self.path}/transfers.txt"),
            "feed_info": pd.read_csv(f"{self.path}/feed_info.txt"),
            "fare_rules": pd.read_csv(f"{self.path}/fare_rules.txt"),
            "fare_attributes": pd.read_csv(f"{self.path}/fare_attributes.txt"),
            "agency": pd.read_csv(f"{self.path}/agency.txt"),
            "stop_amenities": pd.read_csv(f"{self.path}/stop_amenities.txt"),
        }
