import arcpy
import os

# module for listing datasets


def list_datasets(location, arcpy=True, datatype=None, subtype=None, exclusion=None):
        """ (str[,datatype = str[,type = str][,exclusion = str]) -> list
        Takes an input string of the directory (or workspace)
        containing the datasets and recursively returns all filepaths into a list.
        Optional datatype,subtype and exlusion args can be set to limit the results.
        If you want to exclude a folder, set the 'exclusion' parameter to the directory name (or list of names).
        You may also set 'datatype' and 'type' parameters according to the arcpy.da.Walk syntax (http://resources.arcgis.com/EN/HELP/MAIN/10.2/index.html#//018w00000023000000")
        Some files (such as .las) will not be recognized by the arcpy.da.Walk method. In such cases,
        set arcpy=False to us the os module 'walk' method instead, which will retreive all filenames. 

        >>> get_features("C:/workspace",datatype = "FeatureClass",type = "Polygon",exclusions = "Projected")
        >>> [list of all polygon feature classes in 'C:/workspace', excluding all those in a subdirectory named "Projected"]
        """
        result = []
        if arcpy:
            if exclusion:
                for dirpath,dirnames,files in arcpy.da.Walk(location,datatype = datatype,type = subtype):
                    if exclusion in dirnames:
                        dirnames.remove(exclusion)
                    for filename in files:
                        result.append(os.path.join(dirpath,filename))
            else:
                for dirpath,dirnames,files in arcpy.da.Walk(location,datatype = datatype,type = subtype):
                    for filename in files:
                        result.append(os.path.join(dirpath,filename))
        else:
            if exclusion:
                for dirpath,dirnames,files in os.walk(location):
                    if exclusion in dirnames:
                        dirnames.remove(exclusion)
                    for filename in files:
                        result.append(os.path.join(dirpath,filename))
            else:
                for dirpath,dirnames,files in os.walk(location):
                    for filename in files:
                        result.append(os.path.join(dirpath,filename))
            
        return result
        

