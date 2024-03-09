import json

def main():
    with open("Videos.json","r") as file:
        data = json.load(file)

    # print(data)
    output = {}
    output[data[0]["file_upload"].split("-")[1]] = []
    # print(data[0]["file_upload"])
    for i in range(len(data)):
        output[data[i]["file_upload"].split("-")[1]] = []
        for j in range(len(data[i]["annotations"][0]["result"])):
            sequence = data[i]["annotations"][0]["result"][j]["value"]["sequence"]
            x = sequence[0]["x"]
            y = sequence[0]["y"]
            width = sequence[0]["width"]
            height = sequence[0]["height"]
            # print(f"sequence:{sequence}")
            if data[i]["annotations"][0]["result"][j]["value"]["labels"][0] == "type":
                output[data[i]["file_upload"].split("-")[1]].append({
                    "start_frame": data[i]["annotations"][0]["result"][j]["value"]["sequence"][0]["frame"],
                    "end_frame": data[i]["annotations"][0]["result"][j]["value"]["sequence"][1]["frame"],
                    "action_type": data[i]["annotations"][0]["result"][j]["value"]["labels"][0],
                    "down_coordinate": None,
                    "up_coordinate": None,
                    "type_word": "公館" if data[i]["file_upload"].split("-")[1] == "Video1.mp4" else "中山",
                })
            if data[i]["annotations"][0]["result"][j]["value"]["labels"][0] == "click":
                output[data[i]["file_upload"].split("-")[1]].append({
                    "start_frame": data[i]["annotations"][0]["result"][j]["value"]["sequence"][0]["frame"],
                    "end_frame": data[i]["annotations"][0]["result"][j]["value"]["sequence"][1]["frame"],
                    "action_type": data[i]["annotations"][0]["result"][j]["value"]["labels"][0],
                    "down_coordinate": [x + width/2 , y + height/2],
                    "up_coordinate": [x + width/2, y + height/2],
                    "type_word": "公館" if data[i]["file_upload"].split("-")[1] == "Video1.mp4" else "中山",
                })
            if data[i]["annotations"][0]["result"][j]["value"]["labels"][0] == "swipe":
                output[data[i]["file_upload"].split("-")[1]].append({
                    "start_frame": data[i]["annotations"][0]["result"][j]["value"]["sequence"][0]["frame"],
                    "end_frame": data[i]["annotations"][0]["result"][j]["value"]["sequence"][1]["frame"],
                    "action_type": data[i]["annotations"][0]["result"][j]["value"]["labels"][0],
                    "down_coordinate": [x, y + height],
                    "up_coordinate": [x,y],
                    "type_word": "公館" if data[i]["file_upload"].split("-")[1] == "Video1.mp4" else "中山",
                })

    with open('../annotate.json', 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=4, ensure_ascii=False)
    # print(output)
            
    

if __name__ == "__main__":
    main()