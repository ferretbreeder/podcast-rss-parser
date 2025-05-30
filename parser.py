import xml.etree.ElementTree as ET
import csv

tree = ET.parse("/home/silver/_dev/rss-parser/20250529_skyhoppers-libsyn.rss")

root = tree.getroot()

ep_num = 169

with open("episodes.csv", "w", newline='') as episodes_file:

    writer = csv.writer(episodes_file, delimiter=',')

    writer.writerow(["episode_number", "episode_title", "description"])

    for item in root.iter('item'):

        episode_info = []

        title = item[0].text
        desc = item[6].text.split("<ul>")[0]

        episode_info.append(ep_num)
        episode_info.append(title)
        episode_info.append(desc)

        writer.writerow(episode_info)

        ep_num += 1

        print(title + " " + desc)