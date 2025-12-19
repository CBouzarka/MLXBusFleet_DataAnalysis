import pandas as pd
import zipfile

class GTFSLoader:
    def __init__(self, path: str, zipped: bool = False):
        self.path = path
        self.zipped = zipped

    def load(self):
        if self.zipped:
            return self._load_from_zip()
        return self._load_from_folder()
    
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
            "stop_amenities": pd.read_csv(f"{self.path}/stop_amentities.txt"),
        }

    def _load_from_zip(self):
        with zipfile.ZipFile(self.path, "r") as z:
            return {
                "routes": pd.read_csv(z.open("routes.txt")),
                "trips": pd.read_csv(z.open("trips.txt")),
                "stops": pd.read_csv(z.open("stops.txt")),
                "stop_times": pd.read_csv(z.open("stop_times.txt")),
                "calendar": pd.read_csv(z.open("calendar_dates.txt")),
                "calendar_dates": pd.read_csv(z.open("calendar_dates.txt")),
                "shapes": pd.read_csv(z.open("shapes.txt")),
                "transfers": pd.read_csv(z.open("transfers.txt")),
                "feed_info": pd.read_csv(z.open("feed_info.txt")),
                "fare_rules": pd.read_csv(z.open("fare_rules.txt")),
                "fare_attributes": pd.read_csv(z.open("fare_attributes.txt")),
                "agency": pd.read_csv(z.open("agency.txt")),
                "stop_amenities": pd.read_csv(z.open("stop_amentities.txt"))
          }
