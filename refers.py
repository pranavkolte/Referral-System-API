from fastapi import FastAPI, HTTPException
import config
import json

def get_user_info(email : str):
    database = config.get_database()
    cursor = database.cursor()
    cursor.execute(config.SQL_GET_CURRENT_USER_ID, (email,))
    result = cursor.fetchall()
    return {"id" : result[0][0],
    "email" : email,
    "name" : result[0][1],
    "referral_id" : result[0][2],
    "referral_points" : result[0][3],
    }



def get_refer_info(email:str):
    details = get_user_info(email=email)
    referral_id = details["referral_id"]
    database = config.get_database()
    cursor = database.cursor()
    print(referral_id)
    cursor.execute(config.SQL_GET_REFERED_USER, (referral_id,))
    result = cursor.fetchall()
    if list :
        return convert(result)
    

def convert(result):
    raw = []
    for record in result:
        raw.append(list(record))
    new_dict = {}
    count = 0
    for item in raw:
        id = 'none'
        email = 'none'
        name = 'none'
        time = 'none'
        for idx, val in enumerate(item):
            if idx == 0:
                id = str(val)
            if idx == 1:
                email = str(val)
            if idx == 2:
                name = str(val)
            if idx == 3:
                time = str(val)
        count +=1 
        new_dict[count] = {"id": id, "email": email, "name": name, "time" : time}
    return json.dumps(new_dict)


if __name__ == "__main__":
    print(get_refer_info("kolaajshs@gmail.com"))