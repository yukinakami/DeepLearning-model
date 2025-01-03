# -*- coding: utf-8 -*-

import os
import json

data_root = 'G://news'
data_list = []

# ����ΪJSON�ļ�
def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# ��������
for date_folder in os.listdir(data_root):
    date_path = os.path.join(data_root, date_folder)
    if os.path.isdir(date_path):
        for news_folder in os.listdir(date_path):
            news_path = os.path.join(date_path, news_folder)
            if os.path.isdir(news_path):
                # ��ȡ�ı�����
                text_files = [f for f in os.listdir(news_path) if f.endswith('.txt')]
                text_contents = []
                for text_file in text_files:
                    text_path = os.path.join(news_path, text_file)
                    with open(text_path, 'r', encoding='utf-8') as file:
                        text_contents.append(file.read())
                
                # ��ȡͼƬ����
                image_files = [f for f in os.listdir(news_path) if f.endswith(('.jpg', '.jpeg', '.png', '.mp4'))]
                image_paths = [os.path.join(news_path, img) for img in image_files]
                
                # ��������ӵ��б�
                for image_path in image_paths:
                    for text_content in text_contents:
                        data_list.append({
                            "image_path": image_path,
                            "text": text_content,
                            "news_title": news_folder,
                            "news_date": date_folder
                        })

# �����ݴ�������󣬱���һ��JSON�ļ�
save_to_json(data_list, 'G://news_data.json')
