import xml.etree.ElementTree as ET
import csv

tree = ET.parse("20250529_skyhoppers-libsyn.rss")

root = tree.getroot()

ep_num = len(root.findall('channel/item'))

with open("episodes.csv", "w", newline='') as episodes_file:

    writer = csv.writer(episodes_file, delimiter=',')

    writer.writerow(["episode_number", "episode_file_name", "episode_title", "pub_date", "description", "libsyn_link"])

    for item in root.iter('item'):

        file_name = ""

        for enclosure in item.iter('enclosure'):
           if enclosure.attrib.get('url') == None:
                continue
           else:
                file_name = enclosure.attrib['url'].split("skyhopperspodcast/")[1].split("?")[0].replace("_", " ")

        episode_info = []

        title = item[0].text
        pub_date = item[2].text
        libsyn_link = item[4].text

        if "<p>" in item[6].text.split("<ul>")[0]:
            desc = item[6].text.split("<ul>")[0].split("<p>", 1)[1].split("</p>", 1)[0].strip()
        else:
            desc = item[6].text.split("<ul>")[0]

        episode_info.append(ep_num)
        episode_info.append(file_name)
        episode_info.append(title)
        episode_info.append(pub_date)
        episode_info.append(desc)
        episode_info.append(libsyn_link)

        writer.writerow(episode_info)

        ep_num -= 1