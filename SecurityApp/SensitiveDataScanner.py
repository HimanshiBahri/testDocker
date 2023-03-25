import docker
from docker_registry_client import DockerRegistryClient, Repository, Image
from docker_registry_client._BaseClient import BaseClientV1, BaseClientV2
import json
import re
import ast
from sh import grep, cat
import requests
import subprocess 
import os


url = "http://localhost:5000/"
client = DockerRegistryClient(url)

#print(client.repositories())
#print(client.repository("app-frontend"))
#print(client.api_version)
client.refresh()

rep = Repository(BaseClientV2(url), 'firstimage')
#print(rep.tags)

content = rep.manifest('latest')[0]
#print(content)
manif = eval(str(content))
#print(manif)
#print(manif["history"])

f = open("newfile.txt","w")
f.write(str(manif))
f.close()

f = open("his.txt","w")
f.write(str(manif["history"]))
f.close()

#print(manif["history"])

#print(len(manif["history"]))
#print(manif["history"][1])


"""
for each in manif["history"]:
print(str(each)+"\n")
grep('-i','-e',"secret", str(each))	#detect here

"""

json_url = "https://jsonformatter.curiousconcept.com/process"
data = {'data':str(manif["history"]), 'process': 'true', 'jsontemplate':'1', 'jsonspec':'4', 'jsonfix':'on', 'version':'2'}

#print(data)

r = requests.post(json_url, data, verify=False)


f = open("response.txt","w")
f.write(r.text)
f.close()
#print(r.text)

os.system("mkdir files && cd files && git init && git config --global user.name 'test' && git config --global user.email 'test@dockersecurity.com'")

os.system("touch files/response3.txt")


cmd = "cat response.txt | jq . > files/response3.txt"

os.system(cmd)

#os.system("cat response3.txt")

os.system('color')

os.system("cd files && git add . && git commit -m 'commit'")

#os.system("cd files && sudo gittyleaks --find-anything ./")

#os.system("rm -rf ./files")





