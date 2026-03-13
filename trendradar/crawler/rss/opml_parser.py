# coding=utf-8
"""OPML 解析器"""

import xml.etree.ElementTree as ET
from typing import List, Dict


def parse_opml(file_path: str) -> List[Dict[str, str]]:
    """解析 OPML 文件，提取 RSS 源信息"""
    tree = ET.parse(file_path)
    root = tree.getroot()
    feeds = []
    
    for outline in root.findall(".//outline[@type='rss']"):
        xml_url = outline.get('xmlUrl')
        if xml_url:
            text = outline.get('text', '')
            feed_id = text.replace('.', '-').replace(' ', '-').lower()
            feeds.append({
                'id': feed_id,
                'name': outline.get('title', text),
                'url': xml_url
            })
    
    return feeds
