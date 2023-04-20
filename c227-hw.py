import json
data_from_csv=[]
file=open('data_set.txt','r')
data=json.load(file)
print(data)
with file as f:
    data_from_text=json.loads(f.read())
feild_names=['throttle','brake','handbrake','steer']
csvfilestore=open('data_set.csv','w',newline='')
writer=csv.DictWriter(csvfilestore,fieldnames=feild_names)
writer.writeheader()
writer.writerows(feild_names)