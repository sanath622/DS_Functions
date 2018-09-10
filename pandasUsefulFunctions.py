def whichColumnsNA(df):
    """
    Returns the list of columns which have NAN or NA values
    """
    return df.columns[df.isna().any()].tolist()
