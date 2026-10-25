"""Domain parsing adapted from the original SNJ coursework; see PROVENANCE.json."""
import re

import unicodedata

def normalize_vi(text):
    text = str(text).lower().strip()
    text = unicodedata.normalize('NFD', text)
    text = ''.join(ch for ch in text if unicodedata.category(ch) != 'Mn')
    text = text.replace('đ', 'd')
    text = re.sub(r'\s+', ' ', text)
    return text

def phrase_in_text(text, phrase):
    t = normalize_vi(text)
    p = normalize_vi(phrase)
    if not p:
        return False
    # Unicode \w với tiếng Việt đã bỏ dấu, dùng ranh giới để tránh 'cap' khớp nhầm trong 'cao cap'.
    pattern = r'(?<!\w)' + re.escape(p) + r'(?!\w)'
    return re.search(pattern, t) is not None

def contains_any_phrase(text, keywords):
    return any(phrase_in_text(text, k) for k in keywords)

PRODUCT_INTENT_RULES = {
    'stone_bracelet': {
        'categories': ['bracelet'],
        'keywords': ['lắc đá', 'lắc tay', 'chuỗi đá', 'chuỗi đeo tay', 'vòng tay đá', 'bracelet'],
        'boost_terms': ['lắc đá', 'lắc tay', 'chuỗi đá', 'lắc', 'chuỗi']
    },
    'jade_bangle': {
        'categories': ['jade_bangle'],
        'keywords': ['vòng đá', 'vòng cẩm thạch', 'vòng nguyên khối', 'vòng jade', 'vòng ngọc'],
        'boost_terms': ['vòng đá', 'vòng cẩm thạch', 'vòng']
    },
    'loose_stone': {
        'categories': ['loose_stone'],
        'keywords': [
            'đá rời', 'rời', 'loose stone', 'viên đá', 'cặp đá', 'đôi đá',
            'đá làm nhẫn', 'làm nhẫn', 'gắn nhẫn',
            'đá làm mặt dây', 'làm mặt dây', 'gắn mặt dây',
            'đá làm bông tai', 'làm bông tai', 'gắn bông tai',
            'carat', 'ct'
        ],
        'boost_terms': ['viên', 'cặp đá', 'đôi đá', 'ct', 'carat']
    },
    'ring': {
        'categories': ['ring'],
        'keywords': ['nhẫn', 'nhẫn nam', 'nhẫn nữ'],
        'boost_terms': ['nhẫn']
    },
    'pendant': {
        'categories': ['pendant'],
        'keywords': ['mặt dây', 'mặt dây chuyền', 'mặt phật', 'mặt tỳ hưu', 'dây chuyền'],
        'boost_terms': ['mặt dây', 'mặt dây chuyền', 'mặt phật', 'dây chuyền']
    },
    'earrings': {
        'categories': ['earrings'],
        'keywords': ['bông tai', 'hoa tai', 'khuyên tai'],
        'boost_terms': ['bông tai', 'hoa tai', 'khuyên tai']
    }
}

STONE_SYNONYMS = {
    'ruby': ['ruby', 'hồng ngọc', 'hong ngoc'],
    'sapphire': ['sapphire'],
    'citrine': ['citrine', 'thạch anh vàng', 'thach anh vang'],
    'amethyst': ['amethyst', 'thạch anh tím', 'thach anh tim'],
    'aquamarine': ['aquamarine'],
    'garnet': ['garnet'],
    'moonstone': ['moonstone', 'moonstones', 'đá mặt trăng', 'da mat trang'],
    'chalcedony': ['chalcedony'],
    'tiger_eye': ['mắt hổ', 'mat ho', "tiger's eye", 'tiger eye'],
    'jade': ['cẩm thạch', 'cam thach', 'jade'],
    'quartz_hair': ['thạch anh tóc', 'thach anh toc'],
    'topaz': ['topaz'],
    'opal': ['opal'],
    'onyx': ['onyx'],
}

COLOR_TERMS = {
    'vàng': ['vàng', 'vang'],
    'đen': ['đen', 'den'],
    'đỏ': ['đỏ', 'do'],
    'tím': ['tím', 'tim'],
    'xanh': ['xanh'],
    'trắng': ['trắng', 'trang'],
    'nâu': ['nâu', 'nau'],
}

GENDER_TERMS = {
    'male': ['nam', 'cho nam', 'đàn ông'],
    'female': ['nữ', 'cho nữ', 'phụ nữ', 'chị em']
}

def detect_product_intent(query):
    loose_priority = [
        'đá rời', 'rời', 'loose stone', 'viên đá', 'cặp đá', 'đôi đá',
        'đá làm nhẫn', 'làm nhẫn', 'gắn nhẫn',
        'đá làm mặt dây', 'làm mặt dây', 'gắn mặt dây',
        'đá làm bông tai', 'làm bông tai', 'gắn bông tai',
        'carat', 'ct'
    ]
    if contains_any_phrase(query, loose_priority):
        return 'loose_stone'
    if contains_any_phrase(query, PRODUCT_INTENT_RULES['jade_bangle']['keywords']):
        return 'jade_bangle'
    if contains_any_phrase(query, PRODUCT_INTENT_RULES['stone_bracelet']['keywords']):
        return 'stone_bracelet'
    for intent in ['ring', 'pendant', 'earrings']:
        if contains_any_phrase(query, PRODUCT_INTENT_RULES[intent]['keywords']):
            return intent
    return None

def extract_query_sizes(query):
    q=normalize_vi(query)
    values=[]
    for m in re.finditer(r'(?<!\d)(\d{1,2}(?:[.,]\d+)?)\s*(?:ly|mm)(\d)?(?!\w)',q):
        value=float(m.group(1).replace(',','.'))
        if m.group(2) and '.' not in m.group(1) and ',' not in m.group(1): value+=int(m.group(2))/10
        values.append(value)
    for m in re.finditer(r'(?:size|tay)\s*(\d{1,2}(?:[,.]\d+)?)\b(?!\s*(?:ly|mm))',q):
        values.append(float(m.group(1).replace(',','.')))
    return sorted(set(values))

def extract_budget(query):
    q = normalize_vi(query)
    # dưới 2 triệu / duoi 2 trieu
    m = re.search(r'(?:duoi|<|nho hon|khong qua)\s*(\d+(?:[,.]\d+)?)\s*(?:trieu|tr)', q)
    if m:
        return int(float(m.group(1).replace(',', '.')) * 1_000_000)
    m = re.search(r'(?:duoi|<|nho hon|khong qua)\s*(\d{5,})', q)
    if m:
        return int(m.group(1))
    return None

def extract_query_domain_terms(query):
    stones, colors, genders = [], [], []
    for canonical, aliases in STONE_SYNONYMS.items():
        if contains_any_phrase(query, aliases):
            stones.append(canonical)
    for color, aliases in COLOR_TERMS.items():
        if contains_any_phrase(query, aliases):
            colors.append(color)
    for gender, aliases in GENDER_TERMS.items():
        if contains_any_phrase(query, aliases):
            genders.append(gender)
    return stones, colors, genders

def parse_query(query):
    return {
        'product_intent': detect_product_intent(query),
        'stones': extract_query_domain_terms(query)[0],
        'colors': extract_query_domain_terms(query)[1],
        'genders': extract_query_domain_terms(query)[2],
        'sizes': extract_query_sizes(query),
        'max_price': extract_budget(query),
        'certificate_required': contains_any_phrase(query, ['kiểm định', 'chứng nhận', 'PNJ', 'SJC']),
        'earring_purpose': contains_any_phrase(query, ['bông tai', 'hoa tai', 'khuyên tai', 'làm bông tai', 'gắn bông tai']),
        'ring_or_pendant_purpose': contains_any_phrase(query, ['làm nhẫn', 'gắn nhẫn', 'làm mặt dây', 'gắn mặt dây']),
    }
