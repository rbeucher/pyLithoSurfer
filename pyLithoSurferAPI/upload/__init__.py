from pyLithoSurferAPI import *
import pandas as pd
import numpy as np

def clean_entry(item, class_type):
    new = {}

    for key, val in class_type.items():
        if isinstance(val, str):
            try:
                new[key] = item[val]
            except:
                new[key] = val
        else:
            new[key] = val
    
    return new


class UPbSHRIMP(object):

    def __init__(self, dataframe, datapoint, location, sample, shrimp):

        self.df = dataframe
        self.datapoint = datapoint
        self.location = location
        self.sample = sample
        self.shrimp = shrimp

    def check(self):
        return

    def upload(self):

        self.errors = pd.DataFrame()

        for index, item in self.df.iterrows():
            item = item.to_dict()
            
            print(f"Doing item {index}")

            try:
                # Create DataPoint
                args = clean_entry(item, self.data_point)
                data_point = DataPoint(**args)
                data_point.new()
                data.loc[index, "datapoint.id"] = data_point.id

                # Create location
                args = clean_entry(item, self.location)
                location = Location(**args)
                _ = location.new()
                # Should check that location does not exist.
                data.loc[index, "location.id"] = location.id

                # Create sample
                # Tectonic unit (rock) needs to be updated
                args = clean_entry(item, self.sample)
                args["locationId"] = location.id
                sample = Sample(**args)
                _ = sample.new()
                data.loc[index, "sample.id"] = sample.id

                # Create shrimp
                args = clean_entry(item, self.shrimp)
                shrimp_data = SHRIMPDataPoint(**args)
                _ = shrimp_data.new()
                data.loc[index, "shrimp.id"] = shrimp_data.id

                # update DataPoint
                data_point.dataEntityId = shrimp_data.id
                #data_point.locationId = location.id
                data_point.sampleId = sample.id
                data_point.update()

            except:
                self.errors = self.errors.append(self.df.loc[index])
                pass
            
        return



