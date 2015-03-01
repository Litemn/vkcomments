import vkontakte
import time
import math


group_id = '-76982440'


vktoken = raw_input("Enter VK token: ")
vk = vkontakte.API(token=vktoken)

userid = raw_input("Enter userid: ")

user = vk.users.get(user_ids=userid)

#sultan = vk.users.get(user_ids='sultee')
posts = vk.wall.get(owner_id=group_id)

#comms = vk.wall.getComments(owner_id='-76982440', post_id = '83033', offset=75, count=100)

comms = []
for i in posts[1:]:
    comms.append([i['id'], i['comments']['count']])


def checkcomms(postid, offst):
    stena = vk.wall.getComments(owner_id = group_id, post_id = postid, count=100, offset = offst)
    for j in stena[1:]:
            if j['from_id']== user[0]['uid']:
                print j['text']
    time.sleep(0.4)

comm_counter = 0


for k in comms:
    comm_counter = int(math.ceil(k[1]/100))
    for l in range(comm_counter+1):
        checkcomms(k[0], l*100)
#    stena = vk.wall.getComments(owner_id = group_id, post_id = i[0], count=100)
#    for j in stena[1:]:
#            if j['from_id']== user[0]['uid']:
#                print j['text']
#    time.sleep(0.4)
