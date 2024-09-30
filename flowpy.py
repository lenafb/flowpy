

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required = True, help = "Path to csv file")

pre_df2 = pd.read_csv(args["input"])

df1 = pre_df1[pre_df1['Gate']==(args["gate"])]