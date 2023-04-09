
# Python program to read
# json file

def read_json(json_file_location):
    import json
    # Opening JSON file
    f = open('/home/aryan/Music/YouTube_Analysis_Data/DE_category_id.json')
    # returns JSON object as 
    # a dictionary
    data = json.load(f)
    return data

def getting_category_name(data_dict):
 
    b={}
    for i in range(len(data_dict["items"])):
        id=int(data_dict["items"][i]["id"])
        #print(type(id))
        value=data_dict["items"][i]["snippet"]["title"]
        if "id" not in b.keys():
            b[id]=value        
    return b

def convert_datetime_to_date(datetime_series):
    import re
    regex_pattern=re.compile(f"[\d]+-[\d]+-[\d]+")
    res=str(re.findall(regex_pattern,datetime_series))
    date="".join(res[2:12])
    return date

def check_parameters(dict_name):
    import os
    import regex
    status_dict={}
    regex_patters=re.compile("^.*_location")
    for key,value in dict_name.items():
        if check_file_exists(key):
            if os.path.exists(value):
                status_dict[key]=True
            else:
                status_dict[key]=False
    return status_dict

def convert_to_date(data):
    res=data.split(".")
    new_pattern="20{}-{}-{}".format(res[0],res[2],res[1])
    return new_pattern

def check_file_exists(string):
    reg_pattern=re.compile(r"[a-zA-Z,_)]+_location")
    return bool(re.match(reg_pattern,string))



def translate_to_english(text):
    translator = Translator(service_urls=['translate.googleapis.com'])
    res=translator.translate(text, dest='en')
    #print(type(res))
    #print(res.text)
    return res.text

def key_generation(x):
    b={}
    if x not in b.keys():
        b[x]=""
    return b

def return_english_name(name,mydict):
    return mydict[name]

def get_columns(dataframe,column_name,required_position):
    index_cols=dataframe.columns.to_list()
    print(index_cols)
    index=len(index_cols)-1
    print(index)
    temp_index=index_cols[:required_position]+[column_name]+index_cols[required_position:len(index_cols)-1]
    dataframe=dataframe[temp_index]
    return dataframe

def trans_to_eng_sep(text):   
    res=Translator.translate(text, dest='en')
    #print(type(res))
    #print(res.text)
    pa_lang=res.src
    trans_text=res.text.replace('"',"")
    #print(trans_text)
    tags=list(trans_text.split("|"))
    #print(pa_lang)
    return  pa_lang

from configs import *

def get_language_codes_from_url(base_url,tags):
    
    #regex_for_name=re.compile("https://www.familyeducation.com/baby-names/name-meaning/[a-z]+")
    common_last_names=[]
    new_dict={}
    req=requests.get(base_url)
    soup=BeautifulSoup(req.content,"html.parser")
    li = soup.find_all(tags)
    for word in li:
        words_list=word.get_text()
        common_last_names.append(words_list)
    
    # We have to segregate the even and odd names as even names 
    i=0
    while i<len(common_last_names):
        new_dict[common_last_names[i+1]]=common_last_names[i]
        i=i+2
    return new_dict

# From codes_dict we can create a function which takes code as input and after chencking from dictionary , it can
# return the language as outut
def get_lang_from_code(pandas_Series,code_dict):
    code=pandas_Series[0]
    return code

def get_tags_from_code(pandas_Series):
    code=pandas_Series[1]
    return code

def non_lang_codes(lang_codes,codes_dict):
    non_added_keys=[]
    for lang in lang_codes:
        try:
            if codes_dict[lang]:
                pass
        except:
            non_added_keys.append(lang)
# codes_dict["jw"]="javanese"
# codes_dict["zh-CN"]="Chinese (PRC)"

def get_lang_from_codes(codes,codes_dict):
    return codes_dict[codes]

def convert_tags_to_dict(tags_array):
    global max_v
    
    tags_count_dict={}
    for i in tags_array:
        if i in tags_count_dict.keys():
            tags_count_dict[i.lower()]+=1
        else:
            tags_count_dict[i.lower()]=1
    if max_value<len(tags_count_dict):
        max_value=len(tags_count_dict)
    #print(len(tags_count_dict))
    return tags_count_dict


#  FUnctions for Pushing the data to Core DB

def create_conn_string(username,password,host,database_name):
    conn_string=f"postgresql://{username}:{password}@{host}/{database_name}"
    return conn_string

# Function to push data to a database from
def insertion_to_sql(conn_string,dataframe_name,table_name):
    import pandas as pd
    from sqlalchemy import create_engine
    db = create_engine(conn_string)
    conn = db.connect()
    dataframe_name.to_sql(table_name,con=conn,if_exists='replace',index=False)
    
def check_data_inserted(table_name,conn_string):
    conn=psycopg2.connect(conn_string)
    conn.autocommit=True
    cursor=conn.cursor()
    sql1=f"select * from {table_name};"
    cursor.execute(sql1)
    res=cursor.fetchall()
    print(res.head(10))
    
    








            



        
