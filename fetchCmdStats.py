import redis
import time

client = redis.Redis(host="redis-19877.c16.us-east-1-3.ec2.cloud.redislabs.com", port=19877, password="HrhH98ZVvhPMShhnzpPiarE7Q3sXYJpI")

# for key in client.info("commandstats"):
#     print (key)

while (1):
    print("CMDSTAT_GET: " + str(client.info("commandstats").get("cmdstat_get"))) 
    print("CMDSTAT_SET: " + str(client.info("commandstats").get("cmdstat_set")))
    time.sleep(10)