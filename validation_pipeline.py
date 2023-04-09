from configs import *
from data_transformation import *

logging.info("The Pipeline to ingest data is being started")
logging.info("Checking the input parameters")
if len(validation_para)!=5:
    logging.info("Pipeline Failed! As the parameters some of the parameters are missing")
else:
    logging.info("Checking at these location if files are present or not!")
    file_location_status_dict=check_parameters(validation_para)
    for k,v in file_location_status_dict.items():
        if k!='validated_file_location' and v==False:
            logging.info(f'The location of {k} is not valid, please check')
    logging.info("All files have valid location and they exists.")
        
    logging.info("Loading the json file and extracting the required fields")
    json_data_dict=read_json(validation_para["json_location"])
    logging.info("Loading the catgory names along with Ids")
    category_names_id_dict=getting_category_name(json_data_dict)
    logging.info(f'Loading the Csv files from {validation_para["csv_location"]}')
    data_csv=pd.read_csv(validation_para['csv_location'])
    data_csv=data_csv.sort_values("likes",ascending=False)
    cat_ids=data_csv.category_id.unique()
    logging.info("Mapping the category names with the category ids")
    data_csv["category_Name"]=data_csv["category_id"].map(category_names_id_dict)
    logging.info("Extracting the date from publish time and adding it to the same columns")
    data_csv["publish_time"]=data_csv.publish_time.apply(lambda x:convert_datetime_to_date(x))
    data_csv["publish_time"] = data_csv["publish_time"].astype("datetime64[ns]")
    logging.info("Conveting the datetype from string to date")
    data_csv.trending_date=data_csv.trending_date.map(lambda x: convert_to_date(x))
    logging.info("Converting the datetime for trending date")
    data_csv["trending_date"]=data_csv.trending_date.astype("datetime64[ns]")
    logging.info("Calculating the average days differnece between the trending date and publish date")
    data_csv["day_diff"]=abs(data_csv.trending_date-data_csv.publish_time)
    logging.info("Let us calculate the average earning for the vedios depending on the vedios")
    data_csv["total_income($)"]=data_csv.views.map(lambda x : x/1000)
    # Creating a seperate CSV files for the collecting the Average Income per Category
    # Let us find the aggregated income of each category
    data_cat_income=pd.DataFrame(data_csv.groupby("category_Name")["total_income($)"].sum().to_frame(name=' Total Income $').reset_index())
    # Since the Required Directory is not present therefore we will try to create the directory if it does not exist
  

    validated_file_location=validation_para["validated_file_location"]+validation_para["banner"]+"/Validated/Succesful/"

    if os.path.exists(validated_file_location):
        logging.info("Since the file directorys is already present so no need to create the directory locally")
    else:
        cmd=f'mkdir -p {validated_file_location}'
        os.system(cmd)

    logging.info(f"Saving the Income file at{validated_file_location}/data_cat_income")
    data_cat_income.to_csv(f'{validated_file_location}/data_cat_income.csv')
    
    # Since the Api is not responding so the above code is commented out.[Still In development process]
#     top_channels["channel_title(English)"]=top_channels.channel_title.map(lambda x: translate_to_english(x))
#     top_channels["channel_title"].map(lambda x:key_generation(x))
#     # Using this function we can create a dictionary using two column which are one normally names and other name locally.
#     mydict = dict(zip(top_channels.channel_title,top_channels["channel_title(English)"]))
#     data_csv["channel_title_english"]=data_csv.channel_title.map(lambda x: return_english_name(x,mydict))
#     data_csv=get_columns(data_csv,"channel_title_english",4)
#     # If we use this function on this completely we can get the category tags like ['BIGHIT', 'Big Hit', 'BTS', 'BTS', 'BANGTAN', 'Bangtan', 'FAK'] what we will do then
#     # is fining the count of unique_tags and iterating it from list.

#     data_csv["parent_Country"]=data_csv.tags.map(lambda x: trans_to_eng_sep(x))
#     codes_dict=get_language_codes_from_url(base_url,tags)
#     try:
#         data_csv["lang_code"]=data_csv.parent_Country.map(lambda x: get_lang_from_code(x,codes_dict))
#         data_csv["tags_eng"]=data_csv.parent_Country.map(lambda x: get_tags_from_code(x))
#         data_csv.drop(columns="parent_Country")
#     except:
#         print("Since the code is run for one time therfore the column parent_Country has been droppend")
#     lang_codes=data_csv.lang_code.unique().tolist()
#     data_csv["video_language"]=data_csv.lang_code.map(lambda x:get_lang_from_codes(x,codes_dict))
    
#     try:
#         data_csv=data_csv.drop(columns="lang_code")
#         print("Congratulation! Columns has been dropped")
#     except:
#         print("The column lang_codes has already been dropped so no ne columns is available")
        
#     """Since we have different tags assosciated with the channel let us find the most common tags for a 
# trending youtube vedio and finding some of the values of finding the values """
#     # Let us define a fucnton which will converts the tags into a dictionary 
#     data_csv["Updated_tags"]=data_csv.tags_eng.map(lambda x: convert_tags_to_dict(x))
    
    # Saving the Updated_final_data
    final_file_location=validated_file_location+'final_validated.csv'
    logging.info(f"Saving the final CSV File in the location {final_file_location}")
    data_csv.to_csv(final_file_location)
    

    # Saving the final validation data to postgres core DB
    conn_string=create_conn_string('postgres','9760869634','localhost','test')
    insertion_to_sql(conn_string,data_csv,validation_para['table_name'])
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
            
    
    